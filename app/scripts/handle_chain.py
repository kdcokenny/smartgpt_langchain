from app.scripts import (
    create_answer_chain,
    create_researcher_chain,
    create_resolver_chain,
    create_smart_chain,
)


def handle_smartgpt_chain(query: str):
    model = "gpt-3.5-turbo"

    answer_output_keys = ["answer_one", "answer_two", "answer_three"]
    answer_chains = []
    for output_key in answer_output_keys:
        answer_chain = create_answer_chain(model, output_key)
        answer_chains.append(answer_chain)

    researcher_chain = create_researcher_chain(model)

    resolver_chain = create_resolver_chain(model)

    smart_chain = create_smart_chain(
        answer_chains, researcher_chain, resolver_chain
    )

    return smart_chain({"question": query})
