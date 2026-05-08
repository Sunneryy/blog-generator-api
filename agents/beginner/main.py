import os
from crewai import Crew
from agents import resume_screener
from tasks import resume_screening_task

crew = Crew(
    agents=[resume_screener],
    tasks=[resume_screening_task],
    verbose=True,
)

job_description = """
We are looking for a Python Backend Developer with 3+ years of experience.
Requirements:
- Strong Python skills
- Experience with REST APIs and FastAPI or Django
- Familiarity with PostgreSQL or MySQL
- Experience with Docker and CI/CD pipelines
- Good communication skills
"""

resume = """
John Doe
Python Developer — 4 years experience

Skills: Python, Flask, REST APIs, MySQL, Git
Experience:
- Built REST APIs for e-commerce platform using Flask
- Managed MySQL databases for 3 production apps
- Collaborated with frontend team on 5 projects

Education: B.Sc Computer Science
"""

result = crew.kickoff(inputs={
    "job_description": job_description,
    "resume": resume,
})

print("Screening Result:", result)