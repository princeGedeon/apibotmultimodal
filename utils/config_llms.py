import os

from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI

load_dotenv()

class Config():
    """
    Contains the configuration of the LLM.
    """


    #model = 'gpt-3.5-turbo-16k-0613'
    model="gpt-4-turbo"
    llm = ChatOpenAI(temperature=0.1, model=model,)