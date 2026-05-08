from crewai import Task
from agents import resume_screener

resume_screening_task = Task(
    description=(
        "Evaluate the following resume against the job description.\n\n"
        "Job Description:\n{job_description}\n\n"
        "Resume:\n{resume}\n\n"
        "Follow these steps:\n"
        "1. Identify the key requirements from the job description.\n"
        "2. Check how many requirements the resume meets.\n"
        "3. Note any gaps or mismatches.\n"
        "4. Assign a verdict: Strong Fit, Moderate Fit, or Weak Fit."
    ),
    expected_output=(
        "A verdict of exactly one of: 'Strong Fit', 'Moderate Fit', or 'Weak Fit'. "
        "Followed by 2-3 sentences explaining the reasoning."
    ),
    agent=resume_screener,
)