from flask import Flask, request, jsonify, render_template_string
from app.resume_parser import extract_text_from_pdf
from app.job_matcher import match_resume_with_job

app = Flask(__name__)

# Simple HTML form
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Resume Screener</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        h1 { color: #2c3e50; }
        form { margin-top: 20px; }
        textarea, input { width: 100%; padding: 10px; margin: 8px 0; }
        button { padding: 10px 20px; background: #2ecc71; border: none; color: white; cursor: pointer; }
        button:hover { background: #27ae60; }
        .result { margin-top: 20px; padding: 15px; border: 1px solid #ccc; background: #f9f9f9; }
    </style>
</head>
<body>
    <h1>🚀 AI Resume Screener</h1>
    <form action="/match" method="post" enctype="multipart/form-data">
        <label>Upload Resume (PDF):</label>
        <input type="file" name="resume" required>

        <label>Paste Job Description:</label>
        <textarea name="job_description" rows="6" required></textarea>

        <button type="submit">Match Resume</button>
    </form>

    {% if score %}
    <div class="result">
        <h2>Match Score: {{ score }}%</h2>
        <p><b>Key Matching Skills:</b> {{ keywords }}</p>
    </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route("/match", methods=["POST"])
def match_resume():
    if "resume" not in request.files:
        return "⚠️ No resume uploaded"

    file = request.files["resume"]
    job_desc = request.form.get("job_description", "")

    resume_text = extract_text_from_pdf(file)
    score, keywords = match_resume_with_job(resume_text, job_desc)

    return render_template_string(HTML_TEMPLATE, score=round(score, 2), keywords=", ".join(keywords))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
