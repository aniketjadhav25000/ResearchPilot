# ResearchPilot

ResearchPilot is a **Generative AI-powered multi-agent research system** that searches the web, analyzes relevant sources, generates a structured research report, and critically reviews the final result.

## Live Demo

https://research-pilott.streamlit.app/

## Features

- AI-powered web research
- Specialized Search Agent
- Reader Agent for deep content extraction
- Writer Chain for report generation
- Critic Chain for report evaluation
- Interactive Streamlit UI
- Sources, Deep Read, Report, and Critic Review sections

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

- Python
- Generative AI / LLMs
- LangChain
- `create_agent`
- Streamlit
- Tavily Web Search
- Beautiful Soup
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

    git clone https://github.com/aniketjadhav25000/ResearchPilot.git
    cd ResearchPilot
    pip install -r requirements.txt

## Environment Variables

Create a `.env` file:

    OPENAI_API_KEY=your_openai_api_key
    TAVILY_API_KEY=your_tavily_api_key

## Run Locally

    streamlit run app.py

## Workflow

1. Enter a research topic.
2. Search Agent finds relevant sources.
3. Reader Agent extracts useful information.
4. Writer Chain generates the research report.
5. Critic Chain reviews the report.
6. Results are displayed in the Streamlit interface.

## License

MIT License
