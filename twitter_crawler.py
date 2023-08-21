from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import networkx as nx

def crawl_hashtags(start_hashtag, max_hashtags, driver):
    graph = nx.Graph()
    queue = [(start_hashtag, 0)]
    visited = set()

    while queue and len(visited) < max_hashtags:
        current_hashtag, level = queue.pop(0)

        if current_hashtag in visited:
            continue

        visited.add(current_hashtag)
        print(f"Crawling: {current_hashtag} (Level: {level})")

        driver.get(f"https://nitter.net/search?f=tweets&q={current_hashtag}")

        html_content = driver.page_source
        soup = BeautifulSoup(html_content, "html.parser")

        connected_hashtags = []
        hashtag_links = soup.select("div.tweet-content a[href^='/search?q=%23']")
        for link in hashtag_links:
            connected_hashtag = link.text.strip()
            connected_hashtag = connected_hashtag.replace("#", "%23")  # Replace "#" with "%23"
            connected_hashtags.append(connected_hashtag)

        for connected_hashtag in connected_hashtags:
            graph.add_edge(current_hashtag, connected_hashtag)

        for connected_hashtag in connected_hashtags:
            queue.append((connected_hashtag, level + 1))

        time.sleep(2)

    return graph

if __name__ == "__main__":
    driver = webdriver.Chrome()


    step1_start_hashtag = "%23Oslo"
    step1_max_hashtags = 20
    step1_graph = crawl_hashtags(step1_start_hashtag, step1_max_hashtags, driver)

    step2_start_hashtag = "%23Bergen"
    step2_max_hashtags = 20
    step2_graph = crawl_hashtags(step2_start_hashtag, step2_max_hashtags, driver)

    combined_graph = nx.compose(step1_graph, step2_graph)

    nx.write_graphml(combined_graph, "combined_graph.graphml")


    driver.quit()


