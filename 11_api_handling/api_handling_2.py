import requests

def fetch_api():
  url ="https://api.freeapi.app/api/v1/public/randomproducts/product/random"
  response = requests.get(url)
  data = response.json()

  if data["success"] and "data" in data:
    user_data = data["data"]
    brand = user_data["brand"]
    category = user_data["category"]
    description = user_data["description"]
    return brand, category, description
  else:
    raise Exception("Failed to fetch user data.")
  



def main():
  try:
    brand, category, description = fetch_api()
    print(f"{brand}\n{category}\n{description}")
  except Exception as e:
    print(str(e))

if __name__ == "__main__":
  main()