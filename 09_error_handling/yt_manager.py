import json

def load_data():
  try:
    with open("youtube.txt",'r') as file:
      return json.load(file)
  except FileNotFoundError:
    return [1,2]

def save_data_helper(videos):
  with open("youtube.txt",'w') as file:
    json.dump(videos, file)

def list_all_videos(videos):
  print("*" * 50)
  for index, videos in enumerate(videos, start = 1):
    print(f"{index}. {videos['name']}\tDur: {videos['time']}")
  print("*" * 50)
 
def add_video(videos):
  name = input("Enter Video Name: ")
  time = input("Enter Video time: ")
  videos.append({'name':name, 'time':time})
  save_data_helper(videos)

def update_video(videos):
  list_all_videos(videos)
  index = int(input("Enter the video number to update "))
  if 1 <= index <= len(videos):
    name = input("Input new Video Name: ")
    time = input("Input new Video time: ")
    videos[index-1] = {'name':name, 'time':time}
    save_data_helper(videos)
  else:
    print("Invalid Index Selected") 

def delete_video(videos):
  list_all_videos(videos)
  index = int(input("Enter the video number to update be deleted "))
  if 1 <= index <= len(videos):
    del videos[index-1]
    save_data_helper(videos)
  else:
    print("Invalid Index Selected") 


def main():
  videos = []
  while True:
    print("\nYouTube Manager | Choose an option ")
    print("1. List all youtube videos ") 
    print("2. Add a youtube video ") 
    print("3. Update a youtube video details ") 
    print("4. Delete a youtube vidoe ") 
    print("5. Exit App") 

    choice = input("Enter your choice:\t")
    match choice:
      case '1': 
        list_all_videos(videos)
      case '2': 
        add_video(videos)
      case '3': 
        update_video(videos)
      case '4': 
        delete_video(videos)
      case '5': 
        break
      case _:   
        print("Invalid Choice")


if __name__ == "__main__":
  main()