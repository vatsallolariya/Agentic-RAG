from langchain_openai import AzureOpenAIEmbeddings
from config.settings import AZURE_OPENAI_EMBED_DEPLOYMENT, AZURE_OPENAI_API_VERSION


embeddings = AzureOpenAIEmbeddings(
    azure_deployment=AZURE_OPENAI_EMBED_DEPLOYMENT,
    api_version=AZURE_OPENAI_API_VERSION
)
