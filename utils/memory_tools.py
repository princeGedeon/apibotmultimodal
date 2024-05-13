from typing import Tuple, Dict

from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import MessagesPlaceholder
from dotenv import load_dotenv

load_dotenv()

def setup_memory() -> Tuple[Dict, ConversationBufferMemory]:
    """
    Sets up memory for the open ai functions agent.
    :return a tuple with the agent keyword pairs and the conversation memory.
    """
    agent_kwargs = {
        "extra_prompt_messages": [MessagesPlaceholder(variable_name="memory")],
    }
    memory = ConversationBufferMemory(memory_key="memory", return_messages=True)

    return agent_kwargs, memory