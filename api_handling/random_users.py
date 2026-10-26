import requests

def fetch_random_users():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        user_name = user_data["login"]["username"]
        country = user_data["location"]["country"]
        firstname = user_data["name"]["first"]
        return user_name, country
    else:
        raise Exception("error in API calling")

def main():
    try:
        user_name, country = fetch_random_users()
        print(f"username: {user_name} \n country: {country}")
    except Exception as e:
        print(str(e))


if __name__ =="__main__":
    main()
