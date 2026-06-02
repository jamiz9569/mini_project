import sqlite3

con = sqlite3.connect("yt_sqlite.db")

cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')
con.commit()

def list_all_videos():
    cur.execute('''SELECT * FROM videos''')
    rows = cur.fetchall()
    if not rows:
        print("No videos found.")
    else:
        for row in rows:
            print(row)

def add_videos(name, time):
    cur.execute(''' INSERT INTO videos (name , time) VALUES (? , ?)''', (name, time))
    con.commit()
    

def update_videos(new_name, new_time, id):
    cur.execute(''' UPDATE videos SET name = ? , time = ? WHERE id = ?''', (new_name, new_time, id))
    con.commit()

def delete_videos(id):
    cur.execute(''' DELETE FROM videos WHERE id =?''', (id,))
    con.commit()


def main():
    while True:
        print("\nYoutube Manager | choose an option")
        print("1. list all youtube videos")
        print("2. add a youtube video")
        print("3. delete a youtube video")
        print("4. update a youtube video details")
        print("5. exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_all_videos()
        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video duration: ")
            add_videos(name, time)
        elif choice == "3":
            id = input("Enter the video ID to delete: ")
            delete_videos(id)
        elif choice == "4":
            id = input("Enter the video ID to update: ")
            new_name = input("Enter the new video name: ")
            new_time = input("Enter the new video duration: ")
            update_videos(new_name, new_time, id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    try:
        main()
    finally:
        con.close()

