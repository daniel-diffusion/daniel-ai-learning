import json
from urllib import parse, request

API_BASE = "https://api.agify.io"
NAMES = ["Alice", "Bob", "Charlie", "Diana"]

# Loop over each name and call the API directly (no helper functions).
for name in NAMES:
    # Build the URL with the current name as a query parameter.
    query = parse.urlencode({"name": name})
    url = f"{API_BASE}?{query}"

    # Call the API and read the raw JSON text.
    with request.urlopen(url) as response:
        body = response.read().decode("utf-8")

    # Convert the JSON text into a Python dictionary.
    data = json.loads(body)

    # Pull out the fields we care about and print them.
    age = data.get("age")
    count = data.get("count")
    print(f"{name}: age={age}, samples={count}")
