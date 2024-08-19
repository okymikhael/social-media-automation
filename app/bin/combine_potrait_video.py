import os
import glob
from moviepy.editor import VideoFileClip, concatenate_videoclips
import shutil

def combine_tiktok_videos(selected_folder):
    # Define directories
    base_dir = os.path.join('app', 'video', selected_folder)
    input_dir = os.path.join(base_dir, 'original')  # Change this line
    export_dir = os.path.join(base_dir, 'tiktok', 'export')
    processed_dir = os.path.join(base_dir, 'tiktok', 'processed')
    minutes_dir = os.path.join(base_dir, 'tiktok', 'minutes_video')
    
    # Ensure all directories exist
    for dir in [input_dir, export_dir, processed_dir, minutes_dir]:  # Add input_dir here
        os.makedirs(dir, exist_ok=True)

    while True:
        # Get all video files from input directory
        video_files = glob.glob(os.path.join(input_dir, '*.mp4'))

        if not video_files:
            print("No more video files in the input directory. Processing complete.")
            break

        clips = []
        total_duration = 0
        processed_files = []

        for video_file in video_files:
            clip = VideoFileClip(video_file)
            
            if clip.duration > 55:
                # Move to minutes_video directory
                shutil.move(video_file, os.path.join(minutes_dir, os.path.basename(video_file)))
                clip.close()
                continue
            
            if total_duration + clip.duration > 55:
                clip.close()
                break
            
            clips.append(clip)
            total_duration += clip.duration
            processed_files.append(video_file)

            if total_duration >= 55:
                break

        if not clips:
            print("No suitable videos found for combination.")
            continue

        # Combine video clips
        final_clip = concatenate_videoclips(clips, method="compose")

        # Generate output filename
        import random
        import string

        def generate_random_string(length=8):
            return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

        random_string = generate_random_string()
        output_filename = f"combined_tiktok_{random_string}.mp4"
        output_path = os.path.join(export_dir, output_filename)

        # Write the final video
        final_clip.write_videofile(output_path)

        # Close clips
        final_clip.close()
        for clip in clips:
            clip.close()

        # Move processed files
        for video_file in processed_files:
            shutil.move(video_file, os.path.join(processed_dir, os.path.basename(video_file)))

        print(f"Combined video saved as {output_path}")

def main():
    # Get list of folders in app/video
    video_folders = [f for f in os.listdir('app/video') if os.path.isdir(os.path.join('app/video', f))]
    
    print("Available folders:")
    for i, folder in enumerate(video_folders, 1):
        print(f"{i}. {folder}")
    
    # Get user input
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
    
    combine_tiktok_videos(selected_folder)

if __name__ == "__main__":
    main()