from graph.workflow import create_workflow


chain = create_workflow()


def ask_question(question: str):
    state = {
        "question": question,
        "documents": [],
        "answer": "",
        "needs_retrieval": False
    }
    return chain.invoke(state)

if __name__ == "__main__":
    print(ask_question("Explain LangGraph."))
