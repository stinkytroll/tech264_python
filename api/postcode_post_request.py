import requests
import json
from pprint import pprint

json_body = json.dumps({'postcodes': ["PR3 0SG", "M45 6GN", "EX165BL"]})

headers = {'Content-Type': 'application/json'}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

pprint(post_multi_req.json())
