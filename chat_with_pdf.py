from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms import CTransformers
from transformers import AutoModelForCausalLM, AutoTokenizer
import sys, requests

loader=DirectoryLoader('data/', glob="*.pdf", loader_cls=PyPDFLoader)
documents=loader.load()

text_splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
text_chunks=text_splitter.split_documents(documents)

embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', model_kwargs={'device':'cpu'})
vector_store=FAISS.from_documents(text_chunks, embeddings)

query="What this pdf about?"
docs = vector_store.similarity_search(query)

llm=CTransformers(model="model\llama-2-7b-chat.ggmlv3.q4_0.bin", model_type="llama", 
                  config={'max_new_tokens':128, 'temperature':0.01})

template="""Use the following pieces of information to answer the user's question.
If you dont know the answer just say you know, don't try to make up an answer.

Context:{context}
Question:{question}

Only return the helpful answer below and nothing else
Helpful answer
"""
qa_prompt=PromptTemplate(template=template, input_variables=['context', 'question'])

chain = RetrievalQA.from_chain_type(llm=llm, chain_type='stuff', retriever=vector_store.as_retriever(search_kwargs={'k': 2}), 
                                    return_source_documents=True, chain_type_kwargs={'prompt': qa_prompt})

while True:
    user_input=input(f"prompt:")
    if query=='exit':
        print('Exiting')
        sys.exit()
    if query=='':
        continue
    result=chain({'query':user_input})
    print(f"Answer:{result['result']}")