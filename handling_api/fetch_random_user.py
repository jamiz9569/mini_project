import requests
import json

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username ,country
    else:
        raise Exception("API request failed with status code: {}".format(response.status_code)) 
    

# health check 

import http.client

conn = http.client.HTTPSConnection("api.freeapi.app")

#conn.request("GET", "/api/v1/healthcheck")
#conn.request("PUT", "/api/v1/healthcheck")

#response = conn.getresponse()
#print(response.read().decode())

#conn.close()

conn.request("GET", "/api/v1/user")
res = conn.getresponse()
print(res.read())
res.close()

conn.request("POST", "/api/v1/healthcheck")
res = conn.getresponse()
print(res.read())
res.close()
        
def random_user():
    try:
        result = fetch_random_user()
        print(result)
    except Exception as e:
        print("An error occurred: {}".format(e))

    
if __name__ == "__main__":
    random_user()


