import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

cursor.execute('''
  CREATE TABLE IF NOT EXISTS videos(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL)
''')

def list_videos():
  cursor.execute("SELECT * FROM videos")
  print("-" * 50)
  print("Duration \t Course Name")
  print("-" * 50)
  for row in cursor.fetchall():
    print(f"{row[0]}. {row[2]}\t{row[1]}")
  

def add_video(name, time):
  cursor.execute("INSERT INTO videos(name, time) VALUES(?,?)", (name, time))
  conn.commit()
  print(f"{name}. {time} Added!")


def update_video(video_id, new_name, new_time):
  cursor.execute("UPDATE videos SET name = ? , time = ? WHERE id = ?", (new_name, new_time, video_id))
  conn.commit()
  print(f"{new_name} Updated!")

def delete_video(video_id):
  cursor.execute("DELETE FROM videos WHERE id=?",(video_id,))
  conn.commit()
  print(f"{video_id} Deleted!")


def main():
  while True:
    print("\n Youtube manager App with DB")
    print("1. List Videos")
    print("2. Add Video")
    print("3. Update Video")
    print("4. Delete Video")
    print("5. Exit App")

    choice = input("Please enter your choice: ")
    if choice == '1':
      list_videos()
    elif choice == '2':
      name = input("Enter the Video Name: ")
      time = input("Enter the Video Time: ")
      add_video(name, time)
    elif choice == '3':
      video_id = int(input("Enter vidoe ID to update: "))
      name = input("Enter the Video Name: ")
      time = input("Enter the Video Time: ")
      update_video(video_id, name, time)
    elif choice == '4':
      video_id = int(input("Enter vidoe ID to be Deleted: "))
      delete_video(video_id)
    elif choice =='5':
      break
    else:
      print("Invalid Choice")  
  conn.close()
  
if __name__ =="__main__":
  main()