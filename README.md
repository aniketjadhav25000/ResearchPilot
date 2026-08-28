# ResearchPilot

ResearchPilot is a **Generative AI-powered multi-agent research system** that searches the web, reads relevant sources, generates a structured research report, and critically reviews the final result.

## Features

- AI-powered web research
- Specialized Search Agent for finding recent and reliable sources
- Reader Agent for deeper content extraction
- Writer Chain for structured report generation
- Critic Chain for reviewing the generated report
- Responsive dark-themed Streamlit UI
- Research progress animation
- Automatic smooth scrolling
- Report, Sources, Deep Read, and Critic Review sections

## Architecture

Research Topic
      ↓
Search Agent
      ↓
Reader Agent
      ↓
Writer Chain
      ↓
Critic Chain
      ↓
Final Research Report

## Tech Stack

- Generative AI / LLMs
- LangChain
- create_agent — specialized AI agent creation
- Python
- Streamlit
- Web Search
- Web Scraping
- Prompt Engineering
- AI Agent Orchestration

## Project Structure

ResearchPilot/
├── app.py
├── pipeline.py
├── agents.py
├── tools.py
├── requirements.txt
└── README.md

## Installation

```bash 
git clone https://github.com/aniketjadhav25000/ResearchPilot.git
cd ResearchPilot
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file and add the API keys required by your agents and tools:

OPENAI_API_KEY=your_api_key
TAVILY_API_KEY=your_api_key

Use the exact environment variable names required by your implementation.

## Run Locally
```bash
streamlit run app.py
```
Open the local Streamlit URL and enter a research topic to start the pipeline.

## Deployment

ResearchPilot can be deployed on Render or other Python-compatible hosting platforms.

### Render

Build Command:

pip install -r requirements.txt

Start Command:

streamlit run app.py --server.address 0.0.0.0 --server.port $PORT

Add your API keys as environment variables in the deployment platform.

## License

This project is licensed under the MIT License.