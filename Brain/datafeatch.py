import requests
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk import download
from TTS.fast_df import speak

# Download NLTK resources required
download('punkt')
download('stopwords')


def get_search_results(query):
    # Replace spaces with '+' for URL encoding
    query = query.replace(' ', '+')
    url = f"https://www.google.com/search?q={query}"

    # Setting a user agent to avoid request rejection by Google
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }

    try:
        # Send the request to Google Search
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Parse the response HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []

        # Find search result divs and extract the necessary information
        for g in soup.find_all('div', class_='tF2Cxc')[:2]:  # Extract the first two results
            title = g.find('h3').text if g.find('h3') else "No Title"
            snippet = g.find('div', class_='VwiC3b').text if g.find('div', class_='VwiC3b') else "No snippet"
            link = g.find('a')['href'] if g.find('a') else "No Link"
            
            if len(snippet) > 50:  # Avoid overly short or irrelevant snippets
                results.append({
                    "title": title,
                    "snippet": snippet,
                    "link": link
                })

        return results

    except Exception as e:
        print(f"Error fetching search results: {e}")
        return []


def summarize_text(text):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words("english"))

    # Rank sentences based on the number of significant words they contain
    ranked_sentences = {}
    for i, sentence in enumerate(sentences):
        words = sentence.split()
        rank = sum(1 for word in words if word.lower() not in stop_words)
        ranked_sentences[i] = rank

    # Extract the top 2 ranked sentences as the summary
    top_sentences = sorted(ranked_sentences, key=ranked_sentences.get, reverse=True)[:2]
    summary = " ".join([sentences[i] for i in sorted(top_sentences)])

    return summary


def main(query):
    search_results = get_search_results(query)

    if not search_results:
        speak("No results found.")
        return

    speak("\nSearch Results:\n")
    for idx, result in enumerate(search_results):
        print(f"Result {idx + 1}:")
        print(f"Title: {result['title']}")
        print(f"URL: {result['link']}")
        print(f"Snippet: {result['snippet']}\n")

        summarized_snippet = summarize_text(result['snippet'])
        print(f"Summary: {summarized_snippet}\n")


