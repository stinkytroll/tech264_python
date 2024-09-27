import requests
from pprint import pprint

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

pprint(post_codes_req)

pprint(f"Status code: {post_codes_req.status_code}")
pprint(f"Headers: {post_codes_req.headers}")
pprint(f"Content: {post_codes_req.content}")
pprint(f"JSON: {post_codes_req.json()}")
pprint(f"Data type of JSON: {type(post_codes_req.json())}")

data_dict = post_codes_req.json()['result']
pprint(f"Region: {data_dict['region']}")
