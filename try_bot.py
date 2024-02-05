import google.generativeai as genai
from IPython.display import Markdown
import textwrap

# Replace with your actual API key
genai.configure(api_key="AIzaSyDjOG1cat93gpFw4AylJWt9QU6IwnbBzE8")

model = genai.GenerativeModel('gemini-pro')
paragraph = """"""

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

while True:
    question = input("Enter your query: ")
    prompt = f"""Answer the following question based on the information in this paragraph:

    {paragraph}

    Question: {question}
    """
    response = model.generate_content(prompt)
    print(to_markdown(response.text).data)