from langchain.agents import AgentExecutor
from utils.agent_tools import setup_agent
from dotenv import load_dotenv

# Load environment variables if needed
load_dotenv()

# Setup the agent using the defined utility function
agent_executor: AgentExecutor = setup_agent()

# Main interaction loop
print("Welcome to the Interactive Agent! Type 'q' to exit.")
while True:
    question = input("Type your question ('q' to exit): ")

    if question.lower() == 'q':
        print("Thank you for using the service. Goodbye!")
        break
    if len(question) == 0:
        continue

    try:
        response = agent_executor.run(question)

        print("Response: >>> ", response)
    except Exception as e:
        print(f"Failed to process your question: {question}")
        print(f"Error: {e}")

# Parle moi de Béhanzin
# Je suis interressé par l'hisoire des rois du Bénin, quelles sont les sites je peux visiter'
# Je suis interressée par le site touristique Toffa à porto novo, C'est situé oû? Et qui contactez pour planifiez ma visite
# Quels sont les hotels et restaurant près de cite, quel jours me conseillerais tu pour ma visite?


## Pipeline audio fon/yoruba ------------> texte français

### Pipeline text français----------> audio fon/yoruba
