from langchain import hub
from langchain.agents import create_tool_calling_agent, AgentExecutor, create_react_agent, create_openai_functions_agent
from langchain.chains.llm_math.base import LLMMathChain
from langchain_community.tools import GooglePlacesTool, YouTubeSearchTool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.utilities import WikipediaAPIWrapper, GooglePlacesAPIWrapper, SerpAPIWrapper
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.tools import Tool
from langchain.memory import ChatMessageHistory

from tools.tiers import get_place_info
from utils.config_llms import Config


def setup_agent():
    travsearch = TavilySearchResults()
    cfg = Config()

    # Initialiser les wrappers API
    memory = ChatMessageHistory(session_id="test-session")
    wikipedia = WikipediaAPIWrapper()
    gplace = GooglePlacesAPIWrapper()
    places = GooglePlacesTool()
    search = SerpAPIWrapper()
    dalle = DallEAPIWrapper()
    youtube = YouTubeSearchTool()

    # Initialiser la chaîne LLMMath
    llm_math_chain = LLMMathChain.from_llm(llm=cfg.llm, verbose=False)

    # Définir les outils
    tools = [
        Tool(
            name="LocalisezSite",
            func=get_place_info,
            description="Obtenir la localisation maps et les heures d'ouvertures d'un lieu à partir de son nom"
        ),
        Tool(name="Search", func=search.run,
             description="Effectue des recherches sur des informations générales, répondant aux questions spécifiques des touristes, idéal pour approfondir des connaissances sur des sites."),
        Tool(name="GoogleSearch", func=search.run,
             description="Réalise des recherches approfondies pour fournir des informations détaillées sur le Bénin, aidant à explorer sa riche histoire et culture."),
        Tool(name="GooglePlaces", func=gplace.run,
             description="Fournir des informations détaillées sur les points d'intérêt touristiques tels que restaurants, hôtels et sites culturels au Bénin."),
        Tool(name="PlacesTool", func=places.run,
             description="Accède à des détails sur des lieux touristiques, incluant recommandations et informations pratiques pour les visiteurs."),
        Tool(name="DallE", func=dalle.run,
             description="Génère des images et illustrations personnalisées pour enrichir les guides et présentations touristiques du Bénin."),
        Tool(name="YouTube", func=youtube.run,
             description="Fournit des vidéos informatives sur des sites touristiques, offrant une expérience immersive et éducative."),
        Tool(name="Calculator", func=llm_math_chain.run,
             description="Propose des outils de calcul pratique pour les conversions de monnaie et de mesure, essentiels pour les touristes en déplacement."),
        Tool(name="Wikipedia", func=wikipedia.run,
             description="Offre un accès instantané à des connaissances, idéal pour approfondir la connaissance des sites historiques et culturels du Bénin.")
    ]

    # Récupérer le prompt
    prompt = hub.pull("hwchase17/openai-functions-agent")

    # Créer l'agent
    agent = create_openai_functions_agent(cfg.llm, tools, prompt)

    # Créer l'exécuteur d'agent
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    return agent_executor