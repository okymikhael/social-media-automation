import os
import glob

def rename_videos_in_sequence(folder_name):
    # Construct the path to the export folder
    export_folder = os.path.join('app', 'video', folder_name, 'export')
    
    # Check if the folder exists
    if not os.path.exists(export_folder):
        print(f"The folder {export_folder} does not exist.")
        return

    # Get all video files in the export folder
    video_files = glob.glob(os.path.join(export_folder, '*.mp4'))
    
    # Sort the files to ensure consistent ordering
    video_files.sort()

    # Rename the files
    for index, video_file in enumerate(video_files, start=1):
        # Construct the new filename
        new_filename = f"{index}.mp4"
        new_filepath = os.path.join(export_folder, new_filename)
        
        # Rename the file
        os.rename(video_file, new_filepath)
        print(f"Renamed {os.path.basename(video_file)} to {new_filename}")

def main():
    # Get list of folders in app/video
    video_folders = [f for f in os.listdir('app/video') if os.path.isdir(os.path.join('app/video', f))]
    
    print("Available folders:")
    for i, folder in enumerate(video_folders, 1):
        print(f"{i}. {folder}")

    # Get user input for folder selection
    while True:
        try:
            choice = int(input("Enter the number of the folder you want to process: "))
            if 1 <= choice <= len(video_folders):
                selected_folder = video_folders[choice - 1]
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    # Rename videos in the selected folder
    rename_videos_in_sequence(selected_folder)

if __name__ == "__main__":
    main()
