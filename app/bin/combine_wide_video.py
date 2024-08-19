import os
from moviepy.editor import VideoFileClip, concatenate_videoclips, ImageClip, CompositeVideoClip

def overlay_image_on_video(video, image_path):
    # Resize the video
    original_width = video.w
    new_height = 720
    new_width = int((new_height * 9) / 16)
    video = video.resize(newsize=(new_width, new_height))
    
    # Load the image
    image = ImageClip(image_path).set_duration(video.duration)
    image = image.resize(newsize=(1280, 720)).set_position(("center", "center"))
    
    # Create a composite with the image and the video
    final = CompositeVideoClip([image, video.set_position(("center", "center"))])
    
    return final

def combine_videos(video_files, image_path):
    combined_clips = []
    for video_file in video_files:
        clip = VideoFileClip(video_file)
        clip_with_overlay = overlay_image_on_video(clip, image_path)
        combined_clips.append(clip_with_overlay)

    return concatenate_videoclips(combined_clips)

def process_folder(folder_path, image_path):
    original_folder = os.path.join(folder_path, "original")
    video_files = [os.path.join(original_folder, f) for f in os.listdir(original_folder) if f.endswith(".mp4")]

    combined_video = combine_videos(video_files, image_path)

    youtube_folder = os.path.join(folder_path, "youtube")
    os.makedirs(youtube_folder, exist_ok=True)
    final_output_path = os.path.join(youtube_folder, "final_combined.mp4")
    combined_video.write_videofile(final_output_path, codec="libx264", audio_codec="aac")

def main():
    base_folder_path = "app/video"
    image_path = "app/image.png"

    folders = [f for f in os.listdir(base_folder_path) if os.path.isdir(os.path.join(base_folder_path, f))]

    print("Select a folder to process:")
    for i, folder in enumerate(folders):
        print(f"{i + 1}. {folder}")

    selected_index = int(input("Enter the number of the folder you want to process: ")) - 1
    if selected_index < 0 or selected_index >= len(folders):
        print("Invalid selection.")
        return

    selected_folder = folders[selected_index]
    folder_path = os.path.join(base_folder_path, selected_folder)
    process_folder(folder_path, image_path)

if __name__ == "__main__":
    main()