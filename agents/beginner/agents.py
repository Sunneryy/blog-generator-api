import os
from crewai import Agent
from crewai.llm import LLM
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

resume_screener = Agent(
    role="Resume Screener",
    goal="Evaluate a candidate's resume against a job description and determine their fit level",
    backstory=(
        "You are an expert recruiter with 15 years of experience screening candidates "
        "across tech, finance, and operations roles. You are objective, consistent, and "
        "can quickly identify whether a candidate's skills and experience match a role."
    ),
    llm=llm,
    verbose=True,
)