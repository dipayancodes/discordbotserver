from pytrends.request import TrendReq
import asyncio
import time

pytrends = TrendReq()
cache = {}  # Simple cache dictionary
cache_duration = 300  # Cache duration in seconds

async def get_trends(message, keyword):
    current_time = time.time()
    cache_key = keyword.lower()

    if cache_key in cache and current_time - cache[cache_key]['time'] < cache_duration:
        # Send cached response
        await message.reply(cache[cache_key]['data'])
        return

    try:
        pytrends.build_payload(kw_list=[keyword])
        related_queries = pytrends.related_queries()
        top_queries = related_queries[keyword]['top']

        if top_queries is not None:
            response = "Top Related Queries:\n"
            for index, row in top_queries.iterrows():
                response += f"{index + 1}. {row['query']} (Interest: {row['value']})\n"
            cache[cache_key] = {'time': current_time, 'data': response}
        else:
            response = "No related queries found."

        await message.reply(response)
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")
