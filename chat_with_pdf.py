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

model_name = "TheBloke/Llama-2-7B-Chat-GGML"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)