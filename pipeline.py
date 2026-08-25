from agents import build_reader_agent, build_search_agent, critic_chain, writer_chain

def run_research_pipeline(topic : str) -> dict:
    state = {}

    # step 1 : search agent working
    print("\n"+"="*50)
    print("step 1 - search agent is working...")
    print("="*50)

    search_agent = build_search_agent()
    search_result = search_agent.invoke({
    "messages": [
        (
            "user",
            f"""
            Research this topic:

            {topic}

            Use the web search tool.

            IMPORTANT:
            - Find recent and reliable sources.
            - Preserve the exact URLs returned by the search tool.
            - In your final answer, include the title, URL, and key information for each source.
            - Do not omit the URLs.
            """
                    )
                ]
            })
    state["search_results"] = search_result['messages'][-1].content
    print("\n search result ", state['search_results'])

    # step 2 : reader agent

    print("\n"+"="*50)
    print("step 2 - reader agent is scraping top resources ...")
    print("="*50)

    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages" : [("user",
            f"Based on the following search result about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"search results:\n{state['search_results']}"
        )]
    })

    state['scraped_content'] = reader_result['messages'][-1].content

    print("\n Scraped content", state['scraped_content'])

    #step 3 : writer chain
    print("\n"+"="*50)
    print("step 3 - writer is drafting the report ...")
    print("="*50)

    research_combined = (
        f"SEARCH RESULTS : \n {state['search_results']}\n\n"
        f"DETAILED SCRAPED CONTENT : \n {state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic" : topic,
        "research" : research_combined
    })
    print("\n Final Report \n", state['report'])

    #critic report
    print("\n"+"="*50)
    print("step 4 - critic is reviewing the report ...")
    print("="*50)

    state["feedback"] = critic_chain.invoke({
        "report" : state['report']
    })
    print("\n critic report \n", state['feedback'])

    return state


if __name__ == "__main__":
    topic = input("\n Enter a research topic : ")
    run_research_pipeline(topic)