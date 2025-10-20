# import fitz 
# import google.generativeai as genai
# from analyze_pdf import analyse_resume_gemini
# #function to extract text from the resume
# def extract_text_from_resume(pdf_path):
#     doc = fitz.open(pdf_path)
#     text = ""
#     for page in doc:
#         text += page.get_text()  # Fixed: Added = for proper concatenation
#     return text

# # Make sure the PDF file is in the same directory as this script
# pdf_path = "Snehitha-resume.pdf"
# print(extract_text_from_resume(pdf_path))
# resume_content= extract_text_from_resume(pdf_path)
# job_description= """
#  we are hiring a python backend developer with ecxperience in django framework,rest apis,sql and nosql databases,cloude developmentand docker containerization.
# """
# result=analyse_resume_gemini(resume_content,job_description)
# print("Resume Analysis:\n")
# print(result)

# # from google import generativeai as genai

# # genai.configure(api_key="AIzaSyBPPE-0Au_SuxsQHbdeCtSQ6yJ9PZFGzR4")  # replace this
# # for model in genai.list_models():
# #     print(model.name, model.supported_generation_methods)


from flask import Flask, render_template, request
import fitz
from analyze_pdf import analyse_resume_gemini

app = Flask(__name__)

def extract_text_from_resume(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get uploaded file and job description
        uploaded_file = request.files["resume"]
        job_description = request.form["job_description"]

        if uploaded_file.filename != "":
            pdf_path = "uploaded_resume.pdf"
            uploaded_file.save(pdf_path)
            resume_text = extract_text_from_resume(pdf_path)
            result = analyse_resume_gemini(resume_text, job_description)
            return render_template("index.html", result=result)
    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)

