import requests

def search_web(query):
    '''simple web search using DuckDuckGo API'''
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    response = requests.get(url)
    return response.json()
