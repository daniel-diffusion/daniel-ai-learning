import json
from urllib import error, request

url = "https://api.agify.io?name=daniel"

try:
    with request.urlopen(url) as response:
        status = response.status
        body = response.read().decode("utf-8")

    print(status)
    print(body)

    data = json.loads(body)
    name = data.get("name")
    age = data.get("age")
    count = data.get("count")
    print(f"Name: {name}")
    print(f"Predicted Age: {age}")
    print(f"Samples used: {count}")
except error.HTTPError as http_err:
    print(f"HTTP error: {http_err.code} {http_err.reason}")
except error.URLError as url_err:
    print(f"Network error: {url_err.reason}")
