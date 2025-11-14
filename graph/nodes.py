from typing import List, TypedDict
from langchain_core.documents import Document
from llms.router_llm import router_llm
from llms.rag_llm import rag_llm
from vectorstore.store import retriever


class State(TypedDict):
    question: str
    documents: List[Document]
    answer: str
    needs_retrieval: bool


def router(state: State) -> State:
    question = state["question"]

    prompt = f"""
    You are a router. Decide if the following question needs retrieval.
    Respond with only YES or NO.
    Question: {question}
    """
    result = router_llm.invoke(prompt).content.strip().upper()
    state["needs_retrieval"] = (result == "YES")
    return state


def retrieve(state: State) -> State:
    docs = retriever.invoke(state["question"])
    state["documents"] = docs
    return state


def generate(state: State) -> State:
    question = state["question"]
    docs = state["documents"]

    if docs:
        context = "\n\n".join(d.page_content for d in docs)
        prompt = f"""
        Context:
        {context}

        Question: {question}
        """
    else:
        prompt = f"Answer the question: {question}"

    resp = rag_llm.invoke(prompt)
    state["answer"] = resp.content
    return state
