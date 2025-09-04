import os
from langchain.agents import initialize_agent, Tool
from langchain_community.llms import OpenAI  # Päivitetty import
from dotenv import load_dotenv

# Lataa ympäristömuuttujat
load_dotenv()

# Aseta OpenAI API -avain
openai_api_key = os.getenv("OPEN_API_KEY")

# Luo LLM (Large Language Model)
llm = OpenAI(temperature=0, openai_api_key=openai_api_key)

# Työkalut työnhakuagentille
def search_jobs(query):
    return f"Found job postings for: {query}"

def analyze_job_posting(job_description):
    return f"Analyzed job posting: {job_description}"

def generate_cover_letter(job_title, company_name):
    prompt = f"""
    Write a professional cover letter for the position of {job_title} at {company_name}.
    Include why I am a good fit for the role and how my skills align with the company's goals.
    """
    return llm(prompt)

tools = [
    Tool(
        name="Job Search",
        func=search_jobs,
        description="Search for job postings based on a query."
    ),
    Tool(
        name="Job Analysis",
        func=analyze_job_posting,
        description="Analyze a job posting to extract key details."
    ),
    Tool(
        name="Cover Letter Generator",
        func=lambda query: generate_cover_letter("Software Engineer", "TechCorp"),
        description="Generate a cover letter for a specific job."
    )
]

# Luo agentti
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

# Käytä Cover Letter Generator -työkalua
response = agent.invoke("Find a software engineering job and generate a cover letter.")

# Luo oikea hakukirje LLM:llä
cover_letter = generate_cover_letter("Software Engineer", "TechCorp")

# Tallenna hakukirje tiedostoon
with open("cover_letter.txt", "w") as file:
    file.write(cover_letter)

print("Agent's response:", response)
print("Cover letter saved to cover_letter.txt")