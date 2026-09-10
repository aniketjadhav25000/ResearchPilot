from dotenv import load_dotenv
load_dotenv()

from bs4 import BeautifulSoup
import requests
import os

from tavily import TavilyClient
from langchain.tools import tool

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


@tool
def web_search(query: str) -> str:
    """Search the web for recent and reliable information."""

    results = tavily.search(
        query=query,
        max_results=5
    )

    out = []

    for i, r in enumerate(results["results"], 1):
        out.append(
            f"""
RESULT {i}
TITLE: {r["title"]}
URL: {r["url"]}
CONTENT: {r["content"][:500]}
"""
        )

    return "\n--------------------\n".join(out)


@tool
def scrape_url(url: str) -> str:
    """Scrape clean structured content from a URL."""

    try:
        resp = requests.get(
            url,
            timeout=15,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, "html.parser")

        for tag in soup([
            "script", "style", "nav", "footer",
            "header", "aside", "noscript",
            "svg", "iframe", "form"
        ]):
            tag.decompose()

        content = []

        for tag in soup.find_all([
            "h1", "h2", "h3", "p", "li", "pre"
        ]):
            text = tag.get_text(" ", strip=True)

            if not text:
                continue

            if tag.name == "h1":
                content.append(f"# {text}")
            elif tag.name == "h2":
                content.append(f"## {text}")
            elif tag.name == "h3":
                content.append(f"### {text}")
            elif tag.name == "li":
                content.append(f"- {text}")
            elif tag.name == "pre":
                content.append(f"```text\n{text}\n```")
            else:
                content.append(text)

        return "\n\n".join(content)[:10000]

    except Exception as e:
        return f"Could not scrape URL: {e}"

