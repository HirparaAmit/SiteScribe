import google.generativeai as genai
from IPython.display import Markdown
import textwrap

# Replace with your actual API key
genai.configure(api_key="AIzaSyDjOG1cat93gpFw4AylJWt9QU6IwnbBzE8")

model = genai.GenerativeModel('gemini-pro')
paragraph = """Amit Hirpara
§ github.com/HirparaAmit ï linkedin.com/in/hirparaamit # amitbcp57@gmail.com
Summary
Dedicated Machine Learning Engineer with exceptional proficiency in Machine Learning and Deep Learning
methodologies. Possess strong analytical abilities to uncover optimal solutions for diverse real-world problem
statements across industries. Core expertise lies in architecting high-performance models leveraging intricate
theoretical constructs, refining algorithms through rigorous evaluation, and striving for cutting-edge outcomes
aligned to project goals.
Education
Pandit Deendayal Energy University (PDEU) August 2019 - May 2023
Bachelor of Technology in Computer Science and Engineering; CGPA: 9.85/10
Experience
Jr. Machine Learning Engineer | S.S.B. Digital PVT. LTD. August 2022 - January 2024
• Developed machine learning and deep learning pipelines from inception for a range of tasks such as sentiment
analysis, computer vision, and intricate data extraction.
• Utilized TensorFlow and PyTorch to create robust and efficient models.
• Collaborated with cross-functional teams to define project objectives and deliverables.
• Employed advanced algorithms to enhance accuracy and performance of models.
• Optimized pipelines to streamline processes and achieve significant time and resource savings.
Deep Learning Intern | BISAG-N May 2022 – July 2022
• Successfully developed and implemented an innovative model for extracting intricate road and street networks from
high-resolution satellite images.
• Utilized modern Deep Learning techniques (U-Net) to cater to the needs of advanced applications.
• Demonstrated exceptional problem-solving skills in designing and optimizing the model.
• Achieved outstanding results in accurately identifying and extracting complex road and street networks from
diverse satellite images.
• Received positive feedback from colleagues and superiors for the effectiveness of the developed model.
Skills
Languages: Python, C, HTML/CSS, JavaScript, SQL
Tools: Git/GitHub, VS Code, Google Colab, Jupyter Notebook, Google Cloud Platform, PostgreSQL pgAdmin,Postman
ML and DL: TensorFlow, PyTorch, Keras, Scikit-Learn, Neural Networks, Model Creation, Model Tuning, Model
Evaluation, Model Validation
Data Science: Explorary Data Analysis, Data Preprocessing, Data Augmentation, Feature Engineering, Statistics &
Applied Mathematics
Computer Vision
Natural Language Processing
Backend/API: Django, Flask, FastAPI, PostgreSQL
Projects
SiteScribe | Llama-2, Natural Language Processing, Web Scrapping January 2024
• Developing an innovative platform called SiteScribe enabling seamless website interaction through personalized
chatbots.
• Creating user-friendly interface where users simply input website links to engage in dynamic conversations.
• SiteScribe will generate customized chatbots for each specific website.
• It will facilitate effortless communication between users and website chatbots, enhancing user experience.
ChatGauge | Python, RegEx, Flask, Data Analytics November 2023
• Developed ChatGauge, a powerful WhatsApp conversation analyzer tool
• Generated detailed reports showcasing metrics such as message count per user, emoji usage, shared links, media
files and many more.
• Demonstrated passion for data analysis and communication by creating an intuitive project.
• Empowered users to gain deeper understanding of their WhatsApp interactions through actionable data.
Lip Reading | TensorFlow, Deep Learning, Gradio, Hugging Face Spaces August 2023
• Developed a real-time LipNet-based Lip Reading system utilizing TensorFlow to improve speech recognition
accuracy.
• Integrated the LipNet model with Gradio to create a user-friendly interface for seamless interaction.
• Implemented real-time video processing to accurately analyze lip movements and convert them into text.
• Achieved significant improvements in lip reading accuracy, contributing to enhanced speech recognition technology
• Showcased strong technical proficiency in TensorFlow, Gradio, and video processing for creating a functional lip
reading system.
Sign Language Detection | TensorFlow, Deep Learning, Computer Vision June 2023
• Designed real-time Sign Language Detection system using TensorFlow and OpenCV.
• Focused on key signs: Yes, No, Hello, Thank You, and I Love You.
• Developed custom Jupyter notebook for streamlined data collection, annotation, and model training.
• Utilized transfer learning with TensorFlow to achieve high precision and recall rates for specified signs.
Tweet Sentiment Analysis | NLTK (NLP), Federated Learning, Machine Learning April 2023
• Implemented and refined a cutting-edge Tweet Sentiment Analysis system utilizing NLP techniques and classical
Machine Learning algorithms.
• Achieved exceptional results, surpassing 90% accuracy in accurately discerning Positive and Negative sentiments
from a wide range of tweets.
• Employed the innovative Federated Learning mechanism to train and optimize the LSTM model on a
comprehensive tweets dataset.
• Recognized for the significance of this work, presented and published findings at a prestigious international
conference.
Publication
Hirpara, A., Patel, S., Vakharia, V., & Kumar, Y. (2023b). A Novel Federated LSTM Model with
Conventional LSTM Model for Sentiment Analysis of Twitter Datasets. In International Journal of Advances
in Electronics and Computer Science (IJAECS), 10(2), 27–36.
Certifications
Machine Learning with Python: Zero to GBMs | Jovian
Programming for Everybody (Python) | Coursera
Achievements
• Intellify - AI Hackathon (2023): Participated in the esteemed artificial intelligence hackathon, hosted by
Marwadi University, and cracked the final round, standing out among the 80+ competing teams from across India.
• Travel Grant (2023): Successfully secured the ”Travel Grant” policy offered by Pandit Deendayal Energy
University, enabling me to present my research paper at an esteemed international conference, and representing the
university on a global platform.
• 2nd World Rank in QHack-2022: Achieved the remarkable distinction of being ranked 2nd worldwide in QHack
2022, competing against top talent and industry experts, and contributing to advancements in quantum machine
learning technology and its potential applications.
• Let’s Hack 2.0 (2019): Successfully participated in the prestigious hackathon, organized by Pandit Deendayal
Energy University in 2019, and advanced to the final round, securing a place among the top 20 teams out of
numerous participants."""

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