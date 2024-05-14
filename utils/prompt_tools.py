from langchain_core.prompts import PromptTemplate

from utils.constants import summary_template
from utils.parser import agent_output_parser

summary_prompt_template = PromptTemplate(
    input_variables=["reponse", "question"],
    template=summary_template,
    partial_variables={'format_instruction': agent_output_parser.get_format_instructions()}
)