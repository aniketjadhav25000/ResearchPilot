from agents import critic_chain, writer_chain
from tools import web_search, scrape_url

import re


def run_research_pipeline(topic: str) -> dict:

    state = {}

    # =========================
    # STEP 1 - WEB SEARCH
    # =========================

    print("\n" + "=" * 50)
    print("STEP 1 - SEARCHING THE WEB...")
    print("=" * 50)

    # Direct tool call
    # NO Groq call
    search_result = web_search.invoke({
        "query": topic
    })

    state["search_results"] = str(search_result)

    print("\nSearch Results:\n")
    print(state["search_results"])


    # =========================
    # STEP 2 - SCRAPING
    # =========================

    print("\n" + "=" * 50)
    print("STEP 2 - SCRAPING TOP RESOURCE...")
    print("=" * 50)

    # Extract URLs from search results
    urls = re.findall(
        r'https?://[^\s\)\]\}>]+',
        state["search_results"]
    )

    if urls:

        selected_url = urls[0].rstrip(".,;:")

        print("\nSelected URL:")
        print(selected_url)

        # Direct tool call
        # NO Groq call
        scraped_result = scrape_url.invoke({
            "url": selected_url
        })

        state["scraped_content"] = str(scraped_result)

    else:

        selected_url = None

        state["scraped_content"] = (
            "No valid URL was found in the search results."
        )


    print("\nScraped Content:\n")
    print(state["scraped_content"])


    # =========================
    # STEP 3 - WRITER
    # =========================

    print("\n" + "=" * 50)
    print("STEP 3 - WRITER IS DRAFTING THE REPORT...")
    print("=" * 50)

    research_combined = (
        f"SEARCH RESULTS:\n"
        f"{state['search_results']}\n\n"
        f"DETAILED SCRAPED CONTENT:\n"
        f"{state['scraped_content']}"
    )

    # 1 Groq call
    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    print("\nFinal Report:\n")
    print(state["report"])


    # =========================
    # STEP 4 - CRITIC
    # =========================

    print("\n" + "=" * 50)
    print("STEP 4 - CRITIC IS REVIEWING THE REPORT...")
    print("=" * 50)

    # 1 Groq call
    state["feedback"] = critic_chain.invoke({
        "report": state["report"]
    })

    print("\nCritic Report:\n")
    print(state["feedback"])


    return state


if __name__ == "__main__":

    topic = input("\nEnter a research topic: ")

    run_research_pipeline(topic)