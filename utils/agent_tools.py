from langchain.agents import AgentExecutor, initialize_agent, AgentType
from langchain.chains.llm_math.base import LLMMathChain
from langchain_community.tools import YouTubeSearchTool, GooglePlacesTool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper, WikipediaAPIWrapper, ArxivAPIWrapper, \
    GooglePlacesAPIWrapper, SerpAPIWrapper
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
from langchain_core.tools import Tool

from utils.config_llms import Config
from utils.memory_tools import setup_memory

from dotenv import load_dotenv

load_dotenv()
def setup_agent() -> AgentExecutor:
    """
    Sets up the tools for a function based chain.
    We have here the following tools:
    - wikipedia
    - duduckgo
    - calculator
    - arxiv
    - events (a custom tool)
    - pubmed
    """
    cfg = Config()
    duckduck_search = DuckDuckGoSearchAPIWrapper()
    wikipedia = WikipediaAPIWrapper()
    #events = tools_wrappers.EventsAPIWrapper()
    #events.doc_content_chars_max=5000*
    gplace=GooglePlacesAPIWrapper()
    places = GooglePlacesTool()
    search = SerpAPIWrapper()
    dalle=DallEAPIWrapper()
    youtube=YouTubeSearchTool()
    llm_math_chain = LLMMathChain.from_llm(llm=cfg.llm, verbose=False)

    tools = [



        Tool(name="Search", func=search.run,
             description="Effectue des recherches sur des informations générales, répondant aux questions spécifiques des touristes, idéal pour approfondir des connaissances sur des sites  ."),
        Tool(name="GoogleSearch", func=search.run,
             description="Réalise des recherches approfondies  pour fournir des informations détaillées sur le Bénin, aidant à explorer sa riche histoire et culture."),
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
             description="Offre un accès instantané à des connaissances , idéal pour approfondir la connaissance des sites historiques et culturels du Bénin.")
    ]

    agent_kwargs, memory = setup_memory()

    return initialize_agent(
        tools,
        cfg.llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True,
        agent_kwargs=agent_kwargs,
        memory=memory
    )