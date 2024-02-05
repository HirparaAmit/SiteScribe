from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)

pdf_loader = PyPDFLoader('./Amit_Hirpara_Resume.pdf')
pages = pdf_loader.load_and_split()
context = "\n".join(str(p.page_content) for p in pages)

prompt_template = """Answer the question as precise as possible using the provided context. If the answer is
                    not contained in the context, say "answer not available in context" \n\n
                    Context: \n {context}?\n
                    Question: \n {question} \n
                    Answer:
                """
prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

stuff_chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

while True:
    question = input("Enter your query: ")
    stuff_answer = stuff_chain(
        {"input_documents": pages, "question": question}, return_only_outputs=True
    )
    print(stuff_answer['output_text'])