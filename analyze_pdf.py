import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()

api_key= os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

configuartion= {
    "temperature":1,
    "top_p":0.95,
    "top_k":40,
    "max_output_tokens": 8192,
    "response_mime_type":"text/plain"
}

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config=configuartion
)


def analyse_resume_gemini(resume_content,job_description):
    prompt= f"""
    You are a Professional resume analyser. 

    Resume:
    {resume_content}

    Job Description:
    {job_description}

    Task:
    -Analyze the resume against the job description. 
    -Give a match score out of 100. 
    -Strengths
    -weakness
    -Highlight missing skills or experience. 
    -Suggest improvements. 

    Return the result in sructure format:
    ATS Score:XX/100
    Missing Skills:
    -...
    Suggestions:
    -...
    Summary:
    -===
    """

    response= model.generate_content(prompt)
    return response.text