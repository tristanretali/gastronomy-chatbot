import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Optional, Type
import requests
import json

# Load environment variables from .env file
load_dotenv(dotenv_path="/Users/tristanretali/Documents/development/gastronomy-chatbot/backend/.env.local")
# 100 request per day and is free to create an account
SPOONACULAR_API_KEY = os.getenv("FOOD_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BASIC_URL = "https://api.spoonacular.com/recipes/"

LLM = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    temperature=0.0
)


def find_by_ingredients(ingredients: str) -> json:
    url = f"{BASIC_URL}findByIngredients?apiKey={SPOONACULAR_API_KEY}&ingredients={ingredients}&number=1"
    response = requests.get(url)
    response_json = response.json()
    return response_json


def recipe_details(id: str) -> json:
    url = f"{BASIC_URL}/{id}/information?apiKey={SPOONACULAR_API_KEY}"
    response = requests.get(url)
    response_json = response.json()
    return response_json


def format_recipe(recipe_detail: str) -> str:
    ingredients = json.dumps(recipe_detail[0])
    prompt_template = PromptTemplate.from_template("""
    <context>You are a chef and want to make your recipe clear as possible</context>
    ---
    I will provide you a JSON follow by a text with these information: the name of the recipe, the ingredients and the instructions.
    Your answer will be structure in three parts.
    ---
    In first part you will introduce the recipe with her name.
    ---
    In the second part you will add each ingredient in a bullet list. You should provide these information:
    - The name
    - The amount
    - The unit
    ---
    In the third part you will detail the instructions in a numbered list to help the user to prepare the recipe. 
    You should details the instructions.
    ---
    This is the content of the JSON and instructions: ### {recipe} ###
    """)
    prompt = prompt_template.format(recipe=recipe_detail)
    response = LLM.invoke(prompt)
    return response


class FindByIngredientsCheckInput(BaseModel):
    ingredients: str = Field(...,
                             ingredients="The ingredients who will be use for the recipe separate by a comma")


class FindByIngredientsTool(BaseTool):
    """ Tool use to find recipe based on ingredients"""

    name = "FindByIngredients"
    description = "Useful when you need to find recipes based on ingredients"

    def _run(self, ingredients: str) -> str:
        response = find_by_ingredients(ingredients)
        recipes = []
        for recipe in response:
            recipe_info = {
                "id": recipe["id"],
                "title": recipe["title"]
            }
            recipes.append(recipe_info)
        return str(recipes)

    def _arun(self):
        raise NotImplementedError("This tool does not support async")

    args_schema: Optional[Type[BaseModel]] = FindByIngredientsCheckInput


class RecipeDetailsCheckInput(BaseModel):
    id: str = Field(..., str="The id of the recipe")


class RecipeDetailsTool(BaseTool):
    name = "RecipeDetails"
    description = "Useful when you need to find recipe details"

    # Try to remove it later
    # return_direct = True

    def _run(self, id: str) -> tuple:
        response = recipe_details(id)
        recipe_ingredients = []
        for ingredient in response["extendedIngredients"]:
            ingredient_infos = {
                "name": ingredient["name"],
                "amount": ingredient["amount"],
                "unit": ingredient["unit"]
            }

            recipe_ingredients.append(ingredient_infos)
        return response["title"], recipe_ingredients, response["instructions"]

    def _arun(self):
        raise NotImplementedError("This tool does not support async")

    args_schema: Optional[Type[BaseModel]] = RecipeDetailsCheckInput


class FormatRecipeCheckInput(BaseModel):
    """ Input for finding recipe with ingredients"""

    recipe_detail: str = Field(...,
                               recipe_detail="All information about the recipe")


class FormatRecipeTool(BaseTool):
    name = "FormatRecipe"
    description = "Useful when you need to convert a recipe details to better format"
    return_direct = True

    def _run(self, recipe_detail: str):
        response = format_recipe(recipe_detail)
        return response

    def _arun(self):
        raise NotImplementedError("This tool does not support async")

    args_schema: Optional[Type[BaseModel]] = FormatRecipeCheckInput


tools = [FindByIngredientsTool(), RecipeDetailsTool(), FormatRecipeTool()]

agent = initialize_agent(tools=tools, llm=LLM,
                         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)


def find_recipe(input: str) -> str:
    return agent.run(input).content


if __name__ == "__main__":
    query = "I would like to cook something with steak and rice"
    res = find_recipe(query)
    print(res)
    # print(agent.agent.llm_chain.prompt.template)
