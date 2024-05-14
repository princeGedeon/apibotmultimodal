from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

class Config():
    """
    Contains the configuration of the LLM.
    """
    #model = 'gpt-3.5-turbo-16k-0613'
    model="gpt-3.5-turbo"
    llm = ChatOpenAI(temperature=0, model=model)