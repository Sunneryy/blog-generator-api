from crewai import Crew, Process
from agents import keyword_researcher, blog_writer, seo_optimizer
from tasks import research_task, writing_task, optimization_task

crew = Crew(
    agents=[keyword_researcher, blog_writer, seo_optimizer],
    tasks=[research_task, writing_task, optimization_task],
    process=Process.sequential,  # agents work one after another
    verbose=True,
)

result = crew.kickoff(inputs={
    "topic": "Case Study/Social Proof - Trust Builder"
})

print("Blog post saved to blog_post.md")
print("Final Output:", result)