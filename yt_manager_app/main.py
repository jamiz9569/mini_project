
import json 

def list_all_videos(videos):
    print("\n")
    print("*" * 50)
    for index , video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} - Duration: {video['time']}")
        # print me the list of videos in a formatted way, where each video is displayed with its index (starting from 1), name, and duration. The enumerate() function is used to get both the index and the video details from the list of videos. The f-string is used to format the output for better readability.

def load_data():
    try:
        with open("videos.json", "r") as file:
            test = json.load(file)
            return test
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



def delete_video(videos):
   list_all_videos(videos)  # Display the list of videos to the user before asking for the index of the video to delete. This helps the user to see the available videos and their corresponding indices, making it easier to choose which video they want to delete.
   video_index = int(input("Enter the index of the video you want to delete: "))
   if 0 < video_index <= len(videos):  # This condition checks if the entered index is valid (greater than 0 and less than or equal to the number of videos in the list). If the index is valid, it proceeds to delete the video; otherwise, it prints an error message indicating that the index is invalid.
        del videos[video_index - 1]  # Delete the video at the specified index from the list. The index is adjusted by subtracting 1 because list indices start at 0, while the user is likely entering a 1-based index.
        save_data_helper(videos)  # Save the updated list of videos after deleting a video.
   else:
        print("Invalid index. Please try again.")




def update_video_details(videos):  
   list_all_videos(videos)  # Display the list of videos to the user before asking for the index of the video to update. This helps the user to see the available videos and their corresponding indices, making it easier to choose which video they want to update.
   video_index = int(input("Enter the index of the video you want to update: "))
   if 0 < video_index <= len(videos):  # This condition checks if the entered index is valid (greater than 0 and less than or equal to the number of videos in the list). If the index is valid, it proceeds to update the video details; otherwise, it prints an error message indicating that the index is invalid.
        video_name = input("Enter the new video name: ")
        video_time = input("Enter the new video duration: ")
        videos[video_index - 1] = {"name": video_name, "time": video_time}  # Update the video details at the specified index in the list. The index is adjusted by subtracting 1 because list indices start at 0, while the user is likely entering a 1-based index.
        save_data_helper(videos)  # Save the updated list of videos after modifying the details of an existing video.
   else:
          print("Invalid index. Please try again.")



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

