import config
from langchain.prompts import PromptTemplate
from langchain.llms.openai import OpenAI
from langchain.chains import LLMChain
import requests
import pprint


# 100 request per day and is free to create an account
spoonacular_api_key = config.FOOD_API_KEY


FIND_RELEVANT_INFORMATIONS = """ You are a chef and your role is to find the relevant informations
in the following content: ### {user_input} ###

I will list you the different relevant informations you should extract:

1. The ingredient and if there is no food put me None as a value
Exemple: 'ingredient': "artichoke", "apple"
##

You should return the information in json format

"""

LLM = OpenAI(
    openai_api_key=config.OPENAI_API_KEY,
    temperature=0.0
)

PROMPT_TEMPLATE = PromptTemplate(
    template=FIND_RELEVANT_INFORMATIONS,
    input_variables=["user_input"]
)

LLM_CHAIN = LLMChain(
    llm=LLM,
    prompt=PROMPT_TEMPLATE,
    verbose=True
)

if __name__ == "__main__":
    print(LLM_CHAIN("I would like to find recipe with pasta and chicken"))
