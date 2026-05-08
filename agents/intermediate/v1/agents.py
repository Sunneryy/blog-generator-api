import os
from crewai import Agent
from crewai.llm import LLM
from crewai_tools import EXASearchTool
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model="openrouter/openai/gpt-4o-mini",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

exa_tool = EXASearchTool(
    api_key=os.getenv("EXA_API_KEY"),
    num_results=2,        # only fetch 2 results instead of default 5
    text_length_limit=500 # limit each result to 500 characters
)
# Agent 1: Researches trending keywords and top articles
keyword_researcher = Agent(
    role="SEO Keyword Researcher",
    goal="Research trending keywords and top-ranking articles for a given topic",
    backstory=(
        "You are an SEO expert with 10 years of experience finding high-traffic "
        "keywords and analysing what makes content rank on Google. You know how "
        "to identify search intent and find content gaps."
    ),
    llm=llm,
    tools=[exa_tool],
    verbose=False,
    max_iter=3,
    max_rpm=10,
)

# Agent 2: Writes the blog post using research context
blog_writer = Agent(
    role="Blog Post Writer",
    goal="Write a complete, engaging blog post based on keyword research",
    backstory=(
        "You are a professional content writer who specialises in creating "
        "informative, engaging blog posts. You know how to structure articles "
        "with clear headings, compelling introductions, and strong conclusions."
    ),
    llm=llm,
    verbose=False,
    max_iter=3,
    max_rpm=10,
)

# Agent 3: Optimises the draft for SEO
seo_optimizer = Agent(
    role="SEO Content Optimizer",
    goal="Optimize the blog post for SEO — improve keyword density, headings, and readability",
    backstory=(
        "You are an SEO optimization specialist who knows exactly how to structure "
        "content to rank on Google. You improve keyword placement, add meta descriptions, "
        "restructure headings, and score readability using proven SEO frameworks."
    ),
    llm=llm,
    verbose=False,
    max_iter=3,
    max_rpm=10,
)