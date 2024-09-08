import requests

def fetch_api():
  url ="https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
  response = requests.get(url)
  data = response.json()

  if data["success"] and "data" in data:
    user_data = data["data"]
    joke = user_data["content"]
    return joke
  else:
    raise Exception("Failed to fetch user data.")

def main():
  try:
    joke = fetch_api()
    print(f"{joke}")
  except Exception as e:
    print(str(e))

if __name__ == "__main__":
  main()