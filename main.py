from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain.agents import AgentExecutor
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from utils.agent_tools import setup_agent
from utils.config_llms import Config
from utils.constants import summary_template
from utils.parser import agent_output_parser
from utils.prompt_tools import summary_prompt_template

load_dotenv()

# Initialisation des variables globales
app = FastAPI()
agent_executor: AgentExecutor = None
chain: LLMChain = None





class RequestModel(BaseModel):
    question: str = "Entrée de la requête"

@app.on_event("startup")
async def startup_event():
    global agent_executor, chain
    config=Config()
    agent_executor = setup_agent()
    chain = LLMChain(llm=config.llm, prompt=summary_prompt_template)


@app.post("/get_parsed_response")
async def get_parsed_response(request: RequestModel):
    """
    Endpoint pour obtenir une réponse analysée.
    """
    prompt = request.question
    response = agent_executor.invoke({"input": prompt})
    res = chain.run(reponse=response, question=prompt)
    parsed_res = agent_output_parser.parse(res)
    return {"parsed_response": parsed_res}

@app.post("/reset_agent_memory")
async def reset_agent_memory():
    """
    Endpoint pour réinitialiser la mémoire de l'agent.
    """
    global agent_executor
    agent_executor = setup_agent()
    return {"message": "Memory reset successfully."}

# Exemple d'utilisation avec Uvicorn (démarrer le serveur avec cette commande)
# uvicorn main:app --reload
