
"""
01 - BASIC WEB REQUEST

Goal:
Understand how Python requests the HTML of a webpage.

Before using BeautifulSoup or Selenium, it is important
to understand what happens when Python connects to a website.

Flow:

Python
   ↓
Website
   ↓
HTTP Response
   ↓
HTML
"""

import requests


# ---------------------------------------------------------
# STEP 1: Website URL
# ---------------------------------------------------------

url = "https://quotes.toscrape.com/"


# ---------------------------------------------------------
# STEP 2: Send a GET request
# ---------------------------------------------------------

response = requests.get(url)

print("Request sent successfully!")


# ---------------------------------------------------------
# STEP 3: Check the HTTP status code
# ---------------------------------------------------------

print("Status code:", response.status_code)


# A status code of 200 means:
# "The request was successful."

if response.status_code == 200:
    print("Website responded successfully.")
else:
    print("Something went wrong.")


# ---------------------------------------------------------
# STEP 4: Get the HTML content
# ---------------------------------------------------------

html = response.text

print("\nFirst 500 characters of the webpage:\n")
print(html[:500])


# ---------------------------------------------------------
# STEP 5: Check how much HTML we received
# ---------------------------------------------------------

print("\nTotal HTML characters:", len(html))


# ---------------------------------------------------------
# WHAT DID WE LEARN?
# ---------------------------------------------------------

"""
We have now learned:

1. requests.get()
   → Sends a request to a website.

2. response.status_code
   → Tells us whether the request was successful.

3. response.text
   → Gives us the HTML returned by the website.

4. len(response.text)
   → Tells us how much HTML we received.

IMPORTANT:
At this stage we have NOT extracted any data.

We have only downloaded the webpage.

The next step is to understand this HTML
and extract useful information from it.

That is where BeautifulSoup comes in.
"""
```
