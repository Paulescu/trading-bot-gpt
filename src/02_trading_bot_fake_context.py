import os
from typing import Dict, List

from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
from dotenv import load_dotenv
from comet_llm import Span, end_chain, start_chain

load_dotenv()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

def retrieve_technical_indicators() -> Dict[str, float]:
    """Retrieve technical indicators from a database."""
    return {'RSI': 0.5, 'MACD': 0.5, 'SMA': 0.5}


def retrieve_recent_news() -> List[str]:
    """Retrieve recent news from a database."""
    return [
        'ETH is about to upgrade its protocol',
        'DeFI sector growing faster than expected.'
    ]

def get_llm_chain() -> LLMChain:

    # prompte template
    template = """Question: {question}
    Answer: Let's think step by step."""

    prompt = PromptTemplate(template=template, input_variables=["question"])

    # llm
    llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0)

    # llm chain
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    return llm_chain

def main(question: str):

    llm_chain = get_llm_chain()

    start_chain(inputs={"question": question})

    with Span(
        category="llm-reasoning",
        inputs={"question": question},
    ) as span:
        response = llm_chain.run(question)
        print(response)
        span.set_outputs(outputs={"response": response})

    end_chain(outputs={"response": response})

question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"
main(question)