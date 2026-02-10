
import json 

def list_all_videos(videos):
    for index , video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} - Duration: {video['time']}")

def load_data():
    try:
        with open("videos.json", "r") as file:
            return json.load(file)
    except FileNotFoundError: 
        return []

def save_data_helper(videos):  # This function takes a list of videos as an argument and saves it to a JSON file named "videos.json". It uses the json.dump() function to write the data to the file, with an indentation of 4 spaces for better readability. This helper function can be called whenever there is a need to save the updated list of videos after adding, deleting, or updating video details.
    with open("videos.json", "w") as file: 
        json.dump(videos, file) 


def add_video(videos):
    video_name = input("Enter the video name: ")
    video_time = input("Enter the video duration: ")
    videos.append({"name": video_name, "time": video_time})
    save_data_helper(videos)  # Save the updated list of videos after adding a new



def delete_video():
    pass

def update_video_details():  
    pass 

def main():
    videos = load_data()  # Load existing videos from a file or database

    while True:
        print("\n Youtube Manager | choose an option")
        print("1. list all youtube videos ")
        print("2. add a youtube video")
        print("3. delete a youtube video")
        print("4. update a youtube video details")
        print("5. exit")

        choice = input("Enter your choice: ")
        print(videos)  # This line is for debugging purposes, it prints the current list of videos to the console. You can remove this line in production code.
   
        # other option to use choice is to use match case statement which is more cleaner and easy to read
        match choice:
            case '1':
                list_all_videos(videos)
                print("Listing all youtube videos...")
                # Code to list all youtube videos goes here
            case '2':
                add_video(videos)
                print("Adding a new youtube video...")
                # Code to add a new youtube video goes here
            case '3':
                delete_video(videos)
                print("Deleting a youtube video...")
                # Code to delete a youtube video goes here
            case '4':
                update_video_details(videos)
                print("Updating youtube video details...")
                # Code to update youtube video details goes here
            case '5':
                print("Exiting the application. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__": # This line checks if the script is being run directly (as the main program) rather than imported as a module in another script. If this condition is true, it executes the code block that follows, which in this case is calling the main() function to start the application.
    main()

