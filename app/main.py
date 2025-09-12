from app.resume_parser import extract_text_from_pdf
from app.job_matcher import match_resume_with_job


def start_app():
    print("🚀 Resume Screener Started")

    resume_path = "data/sample_resume.pdf"
    job_desc_path = "data/job_description.txt"

    # Extract resume text
    resume_text = extract_text_from_pdf(resume_path)

    # Load job description
    with open(job_desc_path, "r", encoding="utf-8") as f:
        job_description = f.read()

    # Match resume with job
    score, keywords = match_resume_with_job(resume_text, job_description)

    print(f"\nMatch Score: {score:.2f}%")
    print("Key Matching Skills:", keywords)
