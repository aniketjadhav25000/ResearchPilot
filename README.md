# ResearchPilot

ResearchPilot is a Generative AI research assistant that automates the process of searching the web, extracting useful information, generating a structured research report, and critically reviewing the final output.

## Live Project

https://research-pilott.streamlit.app/

## Features

- Web search using Tavily
- URL content extraction and cleaning
- AI-generated research reports
- Automated report critique and scoring
- Structured research workflow
- Streamlit-based interface
- Mistral AI for report generation and evaluation

## Agent Architecture

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

### Agents

**Search Agent**
- Searches the web for relevant and recent information.
- Returns useful sources and URLs.

**Reader Agent**
- Scrapes and cleans content from selected web pages.
- Removes unnecessary HTML elements and extracts readable content.

**Writer Chain**
- Combines search results and extracted content.
- Generates a structured research report with:
  - Introduction
  - Key Findings
  - Conclusion
  - Sources

**Critic Chain**
- Reviews the generated report.
- Provides a score, strengths, areas for improvement, and an overall verdict.

## Tech Stack

- Python
- Streamlit
- LangChain
- Mistral AI
- Tavily
- BeautifulSoup
- Requests
- python-dotenv

## Project Structure

    ResearchPilot/
    ├── app.py
    ├── agents.py
    ├── pipeline.py
    ├── tools.py
    ├── requirements.txt
    ├── README.md
    └── .gitignore

## Installation

### Clone the Repository

    git clone https://github.com/aniketjadhav25000/ResearchPilot.git
    cd ResearchPilot

### Install Dependencies

    pip install -r requirements.txt

## Environment Variables

Create a `.env` file in the project root and add:

    MISTRAL_API_KEY=your_mistral_api_key
    TAVILY_API_KEY=your_tavily_api_key

## Run Locally

    streamlit run app.py

## Workflow

1. User enters a research topic.
2. Tavily searches for relevant web sources.
3. The selected source is scraped and cleaned.
4. Mistral generates a structured research report.
5. The Critic Chain evaluates the report.
6. The final research output is displayed in the Streamlit application.

## Author

Aniket Jadhav
