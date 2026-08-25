from dotenv import load_dotenv
load_dotenv()

from bs4 import BeautifulSoup
import requests
import os

from tavily import TavilyClient
from langchain.tools import tool
from rich import print

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query: str) -> str:
    """
    Search the web for recent and reliable information.
    Return search results including title, URL, and content.
    """

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
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(
            url,
            timeout=15,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/131.0.0.0 Safari/537.36"
                ),
                "Accept": "text/html,application/xhtml+xml",
                "Accept-Language": "en-US,en;q=0.9",
            },
        )

        resp.raise_for_status()

        if resp.apparent_encoding:
            resp.encoding = resp.apparent_encoding

        soup = BeautifulSoup(resp.text, "html.parser")

        for tag in soup([
            "script",
            "style",
            "nav",
            "footer",
            "header",
            "aside",
            "noscript"
        ]):
            tag.decompose()

        text = soup.get_text(separator=" ", strip=True)

        return text[:5000]

    except requests.exceptions.HTTPError as e:
        return f"Could not scrape URL. HTTP error: {e}"

    except requests.exceptions.RequestException as e:
        return f"Could not scrape URL. Request error: {e}"

    except Exception as e:
        return f"Could not scrape URL: {e}"
