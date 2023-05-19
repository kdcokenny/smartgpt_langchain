from typing import List
from dotenv import load_dotenv
import langchain
from langchain import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.chat_models import ChatOpenAI

load_dotenv()
langchain.verbose = True


def create_answer_chain(model: str, output_key: str):
    # Note three outputs for one question
    template = """Question. {question}
    
    Answer. Let's think step by step: """

    prompt = PromptTemplate(input_variables=["question"], template=template)

    llm = ChatOpenAI(model_name=model)

    chain = LLMChain(llm=llm, prompt=prompt, output_key=output_key)

    return chain


def create_researcher_chain(model: str):
    # Note combined three outputs into one question
    template = """Question. {question}

    Answer option 1. '''{answer_one}'''

    Answer option 2. '''{answer_two}'''

    Answer option 3. '''{answer_three}'''
    
    You are a researcher tasked with investigating the three response options provided. List the flaws and faulty logic of each answer option. Let's work this out in a step by step way to be sure we have all the errors: """

    prompt = PromptTemplate(
        input_variables=[
            "question",
            "answer_one",
            "answer_two",
            "answer_three",
        ],
        template=template,
    )

    llm = ChatOpenAI(model_name=model)

    chain = LLMChain(llm=llm, prompt=prompt, output_key="flaws")

    return chain


def create_resolver_chain(model: str):
    # Note Find which of the three answers are ideal step by step
    template = """Question. {question}
    
    {flaws}
    
    You are a resolver tasked with 1) finding which of the three answer options the researcher thought was best 2) improving that answer, and 3) Printing the improved answer in full. Let's work this out in a step by step way to be sure we have the right answer: """

    prompt = PromptTemplate(
        input_variables=["question", "flaws"], template=template
    )

    llm = ChatOpenAI(model_name=model)

    chain = LLMChain(llm=llm, prompt=prompt, output_key="final_answer")

    return chain


def create_smart_chain(
    answer_chains: List[LLMChain],
    researcher_chain: LLMChain,
    resolver_chain: LLMChain,
):
    print("Answer Chains: ", answer_chains)
    print("Researcher Chain: ", researcher_chain)
    print("Resolver Chain: ", resolver_chain)
    # Note Combines the three chains into one
    combined_chains = answer_chains + [researcher_chain] + [resolver_chain]

    chain = SequentialChain(
        chains=combined_chains,
        input_variables=["question"],
        output_variables=["final_answer"],
    )

    return chain
