import warnings
warnings.filterwarnings("ignore")

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="SEO Blog Generator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class BlogRequest(BaseModel):
    topic: str

@app.get("/")
def health_check():
    return {"status": "running", "message": "SEO Blog Generator API is live"}

@app.post("/generate")
@app.post("/generate")
async def generate_blog(request: BlogRequest):
    try:
        import sys
        sys.path.insert(0, r"C:\Users\sunda\Desktop\Basic test AI Agent\Test 1-main\agents\intermediate\v1")

        from agents import keyword_researcher, blog_writer, seo_optimizer
        from tasks import research_task, writing_task, optimization_task
        from crewai import Crew, Process

        crew = Crew(
            agents=[keyword_researcher, blog_writer, seo_optimizer],
            tasks=[research_task, writing_task, optimization_task],
            process=Process.sequential,
            verbose=False,
        )

        result = crew.kickoff(inputs={"topic": request.topic})
        return {"success": True, "result": str(result)}

    except Exception as e:
        return {"success": False, "error": str(e)}