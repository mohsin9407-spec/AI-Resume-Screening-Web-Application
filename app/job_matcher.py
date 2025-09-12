import spacy

nlp = spacy.load("en_core_web_sm")

def match_resume_with_job(resume_text: str, job_description: str):
    resume_doc = nlp(resume_text)
    job_doc = nlp(job_description)

    score = resume_doc.similarity(job_doc) * 100

    resume_tokens = {t.lemma_.lower() for t in resume_doc if t.is_alpha}
    job_tokens = {t.lemma_.lower() for t in job_doc if t.is_alpha}
    matching_keywords = list(resume_tokens.intersection(job_tokens))

    return score, matching_keywords[:15]
