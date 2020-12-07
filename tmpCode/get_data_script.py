# importing libraries
import pandas as pd
import requests
import json

# api-endpoint 
URL = "https://jsonplaceholder.typicode.com/todos"

# sending get request and saving the response as response object 
data = requests.get(url = URL) 
  
# extracting data in json format 
data_json = data.json()
print(json.dumps(data_json))