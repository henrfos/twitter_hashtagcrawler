# Hashtag Crawler

This Python script provides a simple yet powerful tool for crawling hashtags on Twitter using Selenium and BeautifulSoup for web scraping, and NetworkX for graph analysis. It's made to explore connections between hashtags, starting from one or multiple seed hashtags and expanding the search to find related hashtags up to a specified limit.

## Prerequisites

- Python 3.x
- Selenium
- BeautifulSoup
- NetworkX
- Webdriver (e.g., ChromeDriver for Google Chrome)

## Usage
1. Set up WebDriver: Update the script to point to the location of your WebDriver
2. Customize Parameters: Modify the start_hashtag and max_hashtags variables as needed for your search.
3. Run the Script: Execute the script in your terminal:
```bash
pip install selenium beautifulsoup4 networkx
```
4.Analyze the Results: The script outputs a .graphml file which can be imported into graph analysis software for further investigation. I personally used Gephi for the graph analysis.

##Example
Starting with the hashtag #Oslo, the script can crawl up to 20 connected hashtags, then it does the same starting from #Bergen. The results from both crawls are combined into a single graph for analysis.




