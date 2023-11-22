# commands/marketing/keyword.py

import discord
import requests

def get_keyword_data(keyword, rapidapi_key, rapidapi_host):
    url = "https://twinword-keyword-suggestion-v1.p.rapidapi.com/"
    payload = {"phrase": keyword, "lang": "en", "loc": "us"}
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "x-rapidapi-key": rapidapi_key,
        "x-rapidapi-host": rapidapi_host
    }

    response = requests.post(url, data=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}")

async def keyword_search(message, keyword):
    try:
        # Replace with your actual RapidAPI key and host
        rapidapi_key = '0ae7b31190mshd2e22561b07a61dp1f643fjsn169f61a04e1a'  
        rapidapi_host = 'twinword-keyword-suggestion-v1.p.rapidapi.com'

        keyword_data = get_keyword_data(keyword, rapidapi_key, rapidapi_host)

        # Format the response based on the API response structure
        related_keywords = ', '.join(keyword_data['keywords'])

        response = (
            f"Keyword: {keyword}\n"
            f"Related Keywords: {related_keywords}"
        )

        await message.channel.send(response)
    except Exception as e:
        await message.channel.send(f"An error occurred: {str(e)}")

# Example usage
# await keyword_search(message, 'digital marketing')
