# ResearchPilot

ResearchPilot is a Generative AI **multi-agent research system** designed to simplify and automate the research process. Instead of manually searching multiple websites, reading lengthy pages, and organizing information into a report, ResearchPilot handles these steps through a structured AI workflow.

The system takes a **research topic** as input and first searches the web for relevant and recent information using Tavily. It then uses **Requests and BeautifulSoup** to extract, parse, and clean useful content from the selected web pages. The collected information is passed to the **Writer Agent**, which uses Mistral AI to generate a structured research report. Finally, the **Critic Agent** reviews the generated report, evaluates its quality, and provides a score along with strengths and areas for improvement.

This multi-agent workflow helps turn raw web information into a clear, structured, and critically evaluated research report with minimal manual effort.

## Live Project

https://research-pilott.streamlit.app/

## Features

- Web search using Tavily
- Web content extraction and cleaning
- AI-powered report generation
- Automated report evaluation and scoring
- Multi-agent research workflow
- Streamlit-based interface

## Agent Architecture

Research Topic → Search → Reader → Writer → Critic → Final Report

## Tech Stack

- **Language:** Python
- **Framework:** Streamlit
- **AI & Orchestration:** LangChain, Mistral AI
- **Search:** Tavily
- **Web Scraping:** BeautifulSoup, Requests
- **Configuration:** python-dotenv

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

Create a `.env` file in the project root:

    MISTRAL_API_KEY=your_mistral_api_key
    TAVILY_API_KEY=your_tavily_api_key

## Run Locally

    streamlit run app.py

## Workflow

1. User enters a research topic.
2. Tavily searches for relevant sources.
3. Web content is extracted and cleaned.
4. Mistral generates the research report.
5. The Critic evaluates and scores the report.
6. The final research report is displayed.

## Author

Aniket Jadhav
