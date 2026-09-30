"""
02 - HTTP STATUS CODES

HTTP status codes tell us what happened after
we sent a request to a website or API.

Common codes:

200 -> Request successful
201 -> Resource created
301 -> Resource moved permanently
302 -> Temporary redirect
400 -> Bad request
401 -> Authentication required
403 -> Forbidden
404 -> Page not found
429 -> Too many requests
500 -> Server error
503 -> Service unavailable
"""

import requests

urls = {
    "Working page": "https://quotes.toscrape.com/",
    "Not found page": "https://quotes.toscrape.com/this-page-does-not-exist",
}

for name, url in urls.items():

    response = requests.get(url)

    print(f"\n{name}")
    print("-" * 30)
    print("URL:", url)
    print("Status code:", response.status_code)

    if response.status_code == 200:
        print("✅ Request successful")

    elif response.status_code == 404:
        print("❌ Page not found")

    elif response.status_code == 403:
        print("🚫 Access forbidden")

    elif response.status_code == 429:
        print("⏳ Too many requests")

    else:
        print("⚠️ Other response")
