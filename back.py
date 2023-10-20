import config
from langchain.prompts import PromptTemplate
from langchain.llms.openai import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.agents import Tool, initialize_agent, AgentType
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Optional, Type
import requests
import pprint
import json


# 100 request per day and is free to create an account
SPOONACULAR_API_KEY = config.FOOD_API_KEY


BASIC_URL = "https://api.spoonacular.com/recipes/"


LLM = ChatOpenAI(
    openai_api_key=config.OPENAI_API_KEY,
    temperature=0.0,
    max_tokens=512
)


def find_by_ingredients(ingredients):
    url = f"{BASIC_URL}findByIngredients?apiKey={SPOONACULAR_API_KEY}&ingredients={ingredients}&number=3"
    response = requests.get(url)
    response_json = response.json()
    return response_json


class FindByIngredientsCheckInput(BaseModel):
    """ Input for finding recipe with ingredients"""

    ingredients: str = Field(...,
                             ingredients="The ingredients who will be use for the recipe")


class FindByIngredientsTool(BaseTool):
    name = "find_by_ingredients"
    description = "Useful when you need to find recipes based on ingredients."
    return_direct = True

    def _run(self, ingredients: str):
        response = find_by_ingredients(ingredients)
        recipes = []
        for recipe in response:
            recipe_info = {
                "id": recipe["id"],
                "title": recipe["title"]
            }
            recipes.append(recipe_info)
        return recipes

    def _arun(self, ingredients: str):
        raise NotImplementedError("This tool does not support async")

    args_schema: Optional[Type[BaseModel]
                          ] = FindByIngredientsCheckInput


tools = [FindByIngredientsTool()]

agent = initialize_agent(tools=tools, llm=LLM,
                         agent=AgentType.OPENAI_FUNCTIONS, verbose=True)

if __name__ == "__main__":
    query = "I would like to cook something with pasta and chicken"
    # resultat = LLM_CHAIN(query)["text"]
    # print(resultat)
    # # convert in dict
    # find_recipes(json.loads(resultat))
    # convert in string
    # find_recipes(json.dumps(resultat))
    res = agent.run(query)
