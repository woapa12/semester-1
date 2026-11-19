"""
Task 2: Fetch and display a post Using GET Request
"""

import httpx

url = "https://httpbin.io/json"

response = httpx.get(url)   # httpx object, get() method, returns a response object

code = response.status_code    
if code == 200 or code == 201:                # check if the response is successful
    print(response.json())      # response object, json() method
else:
    print(f"Error: {code}")