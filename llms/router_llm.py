from langchain_openai import AzureChatOpenAI
from config.settings import AZURE_OPENAI_CHAT_DEPLOYMENT, AZURE_OPENAI_API_VERSION


router_llm = AzureChatOpenAI(
    azure_deployment=AZURE_OPENAI_CHAT_DEPLOYMENT,
    api_version=AZURE_OPENAI_API_VERSION,
    temperature=0
)
