# YouTube Manager

A simple command-line application built in Python to manage your YouTube video collection. This tool allows you to create, read, update, and delete video entries stored in a JSON file.

## Features

- **List Videos**: View all videos in your collection with their names and durations
- **Add Video**: Add a new video to your collection
- **Delete Video**: Remove a video from your collection by its index
- **Update Video**: Modify the name or duration of an existing video
- **Persistent Storage**: All changes are automatically saved to a JSON file

## Requirements

- Python 3.10 or higher (for match-case statement support)
- No external libraries required (uses only built-in `json` and `traitlets` modules)

## Installation

1. Clone or download the project files
2. Ensure you have Python 3.10+ installed on your system
3. Place the script in your desired directory

## Usage

### Running the Application

```bash
python youtube_manager.py
```

### Menu Options

When you run the application, you'll see a menu with the following options:

```
1. List all youtube videos     - Display all videos in your collection
2. Add a youtube video          - Add a new video with name and duration
3. Delete a youtube video       - Remove a video by selecting its index
4. Update a youtube video details - Modify a video's name or duration
5. Exit                          - Close the application
```

### Example Workflow

**Adding a video:**
```
Enter your choice: 2
Enter the video name: How to Learn Python
Enter the video duration: 45 minutes
```

**Listing videos:**
```
Enter your choice: 1

****************************************************
1. How to Learn Python - Duration: 45 minutes
2. Web Development Tutorial - Duration: 60 minutes
```

**Deleting a video:**
```
Enter your choice: 3
[displays current list]
Enter the index of the video you want to delete: 1
```

**Updating a video:**
```
Enter your choice: 4
[displays current list]
Enter the index of the video you want to update: 1
Enter the new video name: Advanced Python Concepts
Enter the new video duration: 90 minutes
```

## File Structure

```
youtube_manager.py      # Main application file
videos.json            # JSON file storing video data (auto-created)
```

### videos.json Format

Videos are stored in JSON format:

```json
[
    {
        "name": "How to Learn Python",
        "time": "45 minutes"
    },
    {
        "name": "Web Development Tutorial",
        "time": "60 minutes"
    }
]
```

## Code Overview

### Key Functions

- **`load_data()`**: Loads videos from `videos.json` file. Returns an empty list if the file doesn't exist
- **`save_data_helper(videos)`**: Saves the current video list to `videos.json`
- **`list_all_videos(videos)`**: Displays all videos in a formatted list
- **`add_video(videos)`**: Prompts user for video details and adds to collection
- **`delete_video(videos)`**: Removes a video by index (1-based)
- **`update_video_details(videos)`**: Modifies an existing video's information
- **`main()`**: Main loop that displays menu and handles user input

## Notes

- Video indices are displayed starting from 1 (user-friendly) but stored from 0 (Python standard)
- All changes are automatically saved to the JSO