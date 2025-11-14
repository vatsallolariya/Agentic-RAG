from langgraph.graph import StateGraph, START, END
from .nodes import State, router, retrieve, generate


def create_workflow():
    workflow = StateGraph(State)

    workflow.add_node("router", router)
    workflow.add_node("retrieve", retrieve)
    workflow.add_node("generate", generate)

    workflow.add_edge(START, "router")

    workflow.add_conditional_edges(
        "router",
        lambda state: "retrieve" if state["needs_retrieval"] else "generate",
        {"retrieve": "retrieve", "generate": "generate"}
    )

    workflow.add_edge("retrieve", "generate")
    workflow.add_edge("generate", END)

    return workflow.compile()
    