# Définir le template de résumé pour l'attraction touristique
from dotenv import load_dotenv
from langchain.agents import AgentExecutor
from langchain.chains.llm import LLMChain
from langchain_anthropic import AnthropicLLM
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from utils.agent_tools import setup_agent
from utils.parser import agent_output_parser

if __name__=="__main__":
    load_dotenv()
    summary_template = """
            Étant donné {reponse} réponse à la question {question} au bot toursime fournir:
            1. réponse textuelle
            2. Des liens youtubes vers videos multimédias s'il en a
            3. Des liens maps s'il en a
            4. Des liens d'images s'il en a
            5. La réponse complète
            \n{format_instruction}
        """

    summary_prompt_template = PromptTemplate(
            input_variables=["reponse","question"],
            template=summary_template,
            partial_variables={'format_instruction': agent_output_parser.get_format_instructions()}
        )



    #llm = ChatOpenAI(temperature=0.5 )
    model = 'gpt-3.5-turbo-16k-0613'
    # model="gpt-4-turbo"
    llm = ChatOpenAI(temperature=0.1, model=model)
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)


    agent_executor: AgentExecutor = setup_agent()

    for _ in range(5):
        prompt = input("Votre préoccupation : ")
        response = agent_executor.invoke({"input":prompt})
        # res = chain.invoke(input={'information': linkedin_data})
        res = chain.run(reponse=response, question=prompt)
        print(res)
        print("--------")
        print(agent_output_parser.parse(res))

