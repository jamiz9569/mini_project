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
        
def main():
    try:
        result = fetch_random_user()
        print(result)
    except Exception as e:
        print("An error occurred: {}".format(e))

    
if __name__ == "__main__":
    main()

