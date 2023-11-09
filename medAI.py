import os
from langchain import HuggingFaceHub, PromptTemplate, LLMChain

os.environ['API_KEY'] = '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'
model_id = 'tiiuae/falcon-7b-instruct'
falcon_llm = HuggingFaceHub(huggingfacehub_api_token='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',
                            repo_id=model_id,
                            model_kwargs={"temperature": 0.8, "max_new_tokens": 500})


template = """
You are a medical assistant AI that provides helpful medical related answers to patients queries.
{question}
"""
prompt = PromptTemplate(template=template, input_variables=['question'])

falcon_chain = LLMChain(llm=falcon_llm,
                        prompt=prompt,
                        verbose=True)
def medAI(data):
    response = falcon_chain.run(data)
    print("Chat bot:", response)
    return response