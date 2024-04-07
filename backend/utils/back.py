import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Optional, Type
import requests
import json

# Load environment variables from .env file
load_dotenv(dotenv_path="../.env.local")
# 100 request per day and is free to create an account
SPOONACULAR_API_KEY = os.getenv("FOOD_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BASIC_URL = "https://api.spoonacular.com/recipes/"

LLM = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    temperature=0.0
)


def find_by_ingredients(ingredients: str) -> json:
    """
    Find recipes based on ingredients from the user input

    Args:
        ingredients (str): The ingredients from the user input

    Returns:
        json: return the recipes found by the call to the API
    """
    url = f"{BASIC_URL}findByIngredients?apiKey={SPOONACULAR_API_KEY}&ingredients={ingredients}&number=1"
    response = requests.get(url)
    response_json = response.json()
    return response_json


def recipe_details(id: str) -> json:
    """
    Find the details of a recipe based on the id provided

    Args:
        id (str): The recipe id

    Returns:
        json: return the details found by the call to the API
    """
    url = f"{BASIC_URL}/{id}/information?apiKey={SPOONACULAR_API_KEY}"
    response = requests.get(url)
    response_json = response.json()
    return response_json


class FindByIngredientsCheckInput(BaseModel):
    """ Input for finding recipe with ingredients"""

    ingredients: str = Field(...,
                             ingredients="The ingredients who will be use for the recipe")


class FindByIngredientsTool(BaseTool):
    """ Tool use to find recipe based on ingredients"""

    name = "FindByIngredients"
    description = "Useful when you need to find recipes based on ingredients"

    def _run(self, ingredients: str) -> str:
        """
        The run implementation of my tool

        Args:
            ingredients (str): The ingredients from the user input

        Returns:
            list: return a list of dict who contain the id and the name of the recipe
        """
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

    args_schema: Optional[Type[BaseModel]
    ] = FindByIngredientsCheckInput


class RecipeDetailsCheckInput(BaseModel):
    """ Input to get the recipe details """

    id: str = Field(..., id="The id of the recipe")


class RecipeDetailsTool(BaseTool):
    """ Tool usd to find the details of a recipe """

    name = "RecipeDetails"
    description = "Useful when you need to find recipe details"
    # Try to remove it later
    return_direct = True

    def _run(self, id: int) -> tuple:
        """
        The run implementation of my tool

        Args:
            id (int): The id of the recipe

        Returns:
            tuple: return the ingredients with their amount and the instructions
        """
        response = recipe_details(id)
        recipe_ingredients = []
        for ingredient in response["extendedIngredients"]:
            ingredient_infos = {
                "name": ingredient["name"],
                "amount": ingredient["amount"],
                "unit": ingredient["unit"]
            }

            recipe_ingredients.append(ingredient_infos)
        return recipe_ingredients, response["instructions"]

    def _arun(self):
        raise NotImplementedError("This tool does not support async")

    args_schema: Optional[Type[BaseModel]] = RecipeDetailsCheckInput


tools = [FindByIngredientsTool(), RecipeDetailsTool()]

agent = initialize_agent(tools=tools, llm=LLM,
                         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

if __name__ == "__main__":
    query = "I would like to cook something with steak and rice"
    res = agent.run(query)
    # print(agent.agent.llm_chain.prompt.template)
