# -*- coding: utf-8 -*-
"""AyaLang.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hu716C6XTHSm3usxl769ORK1TC1IySPr
"""

!pip install transformers

!pip install accelerate

!pip install einops

!pip install langchain
!pip install langchain.community

"""Load the Libraries and load the Tokenizer"""

from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM
import transformers
import torch

"""Model"""

model =  "CohereForAI/aya-23-35B"

tokenizer = AutoTokenizer.from_pretrained(model)

"""Build the Model Pipeline using HuggingFace"""

pipeline = transformers.pipeline(
    "text-generation",
    model = model,
    tokenizer = tokenizer,
    torch_dtype = torch.bfloat16,
    trust_remote_code =  True,
    device_map = "auto",
    max_length=200,
)

from langchain import HuggingFacePipeline

llm = HuggingFacePipeline(pipeline = pipeline, model_kwargs = {'temperature':0})

from langchain import PromptTemplate,  LLMChain

template = """
You are an Arabic Chatbot. You give intelligent to answers in Arabic.
Question: {question}
Answer:"""
prompt = PromptTemplate(template=template, input_variables=["question"])

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "Say a sentence that makes sense in Arabic"

print(llm_chain.run(question))
