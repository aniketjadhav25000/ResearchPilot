# ResearchPilot

ResearchPilot is a Generative AI-powered multi-agent research system that automates the process of web research, source extraction, report generation, and critical evaluation.

The application takes a research topic, searches the web for relevant information using Tavily, extracts detailed content from a selected source, generates a structured research report using Mistral AI, and evaluates the generated report using a dedicated critic chain.

## Live Demo

Try ResearchPilot here:

https://research-pilott.streamlit.app/

## GitHub Repository

https://github.com/aniketjadhav25000/ResearchPilot

---

## Overview

Researching a topic manually often requires searching through multiple websites, reading long articles, extracting useful information, organizing findings, and reviewing the final content.

ResearchPilot simplifies this workflow by combining web search, web scraping, Large Language Models, prompt engineering, and a multi-stage processing pipeline into a single application.

The system currently follows this workflow:

Research Topic
       ↓
Tavily Web Search
       ↓
Relevant Search Results
       ↓
Source Extraction
       ↓
Web Page Scraping
       ↓
Research Writer
       ↓
Research Report
       ↓
Research Critic
       ↓
Final Research Output


## Key Features

- AI-powered web research
- Real-time web search using Tavily
- Automated source extraction
- Web page content scraping
- Structured research report generation
- AI-based report evaluation
- Dedicated Writer and Critic chains
- Interactive Streamlit interface
- Source URLs included in research output
- Mistral AI integration
- Modular Python architecture
- Suitable for research, learning, technical topics, and general information gathering

---

## How It Works

ResearchPilot processes a research request through multiple stages.

### 1. Research Topic

The user enters a topic into the Streamlit application.

Example:

```text
Impact of Generative AI on Software Development
