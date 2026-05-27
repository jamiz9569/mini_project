# YouTube Video Manager (SQLite + Python)

A simple command-line YouTube Video Manager built using Python and SQLite.

This project allows users to:

- Add YouTube videos
- View all saved videos
- Update video details
- Delete videos
- Store data permanently using SQLite database

---

# Features

- SQLite database integration
- CRUD Operations
  - Create
  - Read
  - Update
  - Delete
- Simple CLI menu system
- Persistent data storage

---

# Technologies Used

- Python 3
- SQLite3

---

# Project Structure

```bash
.
├── yt_sqlite.db        # SQLite database file
├── main.py             # Main Python program
└── README.md           # Project documentation
```

---

# Database Schema

Table Name: `videos`

| Column | Type    | Description              |
|--------|---------|--------------------------|
| id     | INTEGER | Primary Key              |
| name   | TEXT    | Video name/title         |
| time   | TEXT    | Video duration           |

---

# How to Run

## 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <project-folder>
```

## 2. Run the Program

```bash
python main.py
```

---

# Menu Options

```text
1. List all youtube videos
2. Add a youtube video
3. Delete a youtube video
4. Update a youtube video details
5. Exit
```

---

# Example Usage

## Add a Video

```text
Enter the video name: Python Tutorial
Enter the video duration: 15:30
```

## List Videos

```text
(1, 'Python Tutorial', '15:30')
```

---

# Functions Overview

## `list_all_videos()`
Displays all videos stored in the database.

## `add_videos(name, time)`
Adds a new video to the database.

## `update_videos(new_name, new_time, id)`
Updates video details using video ID.

## `delete_videos(id)`
Deletes a video from the database using video ID.

---

# Learning Concepts Covered

- SQLite database connection
- SQL queries in Python
- CRUD operations
- Functions
- Loops and conditionals
- Exception handling
- Command-line applications

---

# Future Improvements

- Add search functionality
- Validate user input
- Store upload dates
- Add video categories
- Build GUI version using Tkinter or PyQt
- Convert to web app using Flask or Django

---

# Author

Made using Python and SQLite.

