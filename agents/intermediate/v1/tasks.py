from crewai import Task
from agents import keyword_researcher, blog_writer, seo_optimizer

# Task 1: Research keywords and top articles
research_task = Task(
    description=(
        "Research the following topic: {topic}\n\n"
        "1. Find the top 5 trending keywords related to this topic.\n"
        "2. Search for the top 3 ranking articles on this topic.\n"
        "3. Identify what headings and subtopics they cover.\n"
        "4. Note any content gaps or angles not yet covered.\n"
        "5. Summarise your findings clearly."
    ),
    expected_output=(
        "A research summary containing: top 5 keywords, key topics covered by "
        "competitors, content gaps, and recommended angles for the blog post."
    ),
    agent=keyword_researcher,
    output_file="research.md",  # saves Agent 1's output
)

# Task 2: Write the blog post using research
writing_task = Task(
    description=(
        "Using the research provided, write a complete blog post on: {topic}\n\n"
        "Requirements:\n"
        "- Minimum 800 words\n"
        "- Include an introduction, 4-5 main sections with H2 headings, and a conclusion\n"
        "- Naturally include the researched keywords\n"
        "- Write in a clear, engaging tone for a general audience"
    ),
    expected_output=(
        "A complete blog post with a title, introduction, clearly structured "
        "sections with H2 headings, and a conclusion. Minimum 800 words."
    ),
    agent=blog_writer,
    context=[research_task],  # builds on research from Agent 1
    output_file="draft.md",  # saves Agent 2's output
)

# Task 3: Optimise for SEO
optimization_task = Task(
    description=(
        "Optimise the blog post for SEO.\n\n"
        "1. Improve keyword density — ensure primary keywords appear naturally.\n"
        "2. Rewrite or improve H2 headings to be more SEO-friendly.\n"
        "3. Add a meta description (150-160 characters).\n"
        "4. Score readability and suggest any improvements.\n"
        "5. Output the final optimised blog post."
    ),
    expected_output=(
        "The fully optimised blog post with improved headings, keyword placement, "
        "and a meta description at the top. Ready to publish."
    ),
    agent=seo_optimizer,
    context=[writing_task],  # builds on the draft from Agent 2
    output_file="blog_post.md",  # saves final article to a file
)