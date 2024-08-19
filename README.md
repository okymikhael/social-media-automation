# App Runner

This project allows you to list and run Python applications located in the `bin` folder. Each application should have a `main` function to be executed.

## Features

- List all Python applications in the `bin` folder.
- Display the applications with a formatted name and a random tech emoji.
- Run the selected application.

## Requirements

- Python 3.x

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/app-runner.git
    cd app-runner
    ```

2. Ensure you have a `bin` folder in the project directory with your Python applications.

## Usage

1. Run the main script:
    ```sh
    python app/main.py
    ```

2. The script will list all available applications in the `bin` folder with a formatted name and a random tech emoji.

3. Enter the number corresponding to the application you want to run.

## Example

```
Available apps:
1. Example app 💻
2. Another app 🖥️

Enter the number of the app you want to run: 1
Running example_app.py...
```

## Adding New Applications

1. Create a new Python file in the `bin` folder.
2. Ensure the file has a `main` function, which will be the entry point of the application.

Example:
```python
# bin/example_app.py

def main():
    print("Hello from Example App!")
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

# YouTube Short Mass Upload

This project allows you to mass upload videos to YouTube using the YouTube Data API. It handles authentication, video metadata, and resumable uploads with retry logic.

## Features

- Authenticate with YouTube Data API using OAuth 2.0.
- Upload multiple videos from a specified directory.
- Set video metadata such as title, description, tags, and privacy status.
- Implement exponential backoff strategy for retrying failed uploads.

## Requirements

- Python 3.x
- Google API Client Library for Python

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/youtube-short-mass-upload.git
    cd youtube-short-mass-upload
    ```

2. Install the required libraries:
    ```sh
    pip install --upgrade google-api-python-client oauth2client
    ```

3. Obtain OAuth 2.0 credentials:
    - Go to the [Google API Console](https://console.cloud.google.com/).
    - Create a new project and enable the YouTube Data API.
    - Create OAuth 2.0 credentials and download the `client_secrets.json` file.
    - Place the `client_secrets.json` file in the project directory.

## Usage

1. Place your video files in the `app/video/douyin/export` directory.

2. Run the script:
    ```sh
    python app/bin/youtube_short_mass_upload.py --description "Your video description" --category "22" --keywords "keyword1,keyword2" --privacyStatus "public"
    ```

3. The script will authenticate with YouTube, list the video files in the specified directory, and upload them one by one.

## Example

```
Uploading: video1
Uploading file...
Video id 'abc123' was successfully uploaded.
Uploading: video2
Uploading file...
Video id 'def456' was successfully uploaded.
```

## Adding New Videos

1. Place your video files in the `app/video/douyin/export` directory.
2. Run the script again with the desired options.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

# TikTok Scraper

This project allows you to scrape TikTok for videos based on a search term and download them using SnapTik.

## Features

- Set up a Chrome driver with custom options.
- Search TikTok for videos based on a search term.
- Fetch video URLs from the search results.
- Download videos using SnapTik.

## Requirements

- Python 3.x
- Selenium
- ChromeDriver

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/tiktok-scraper.git
    cd tiktok-scraper
    ```

2. Install the required libraries:
    ```sh
    pip install selenium
    ```

3. Download ChromeDriver and ensure it is in your PATH.

## Usage

1. Run the script:
    ```sh
    python app/bin/tiktok_scraper.py
    ```

2. Enter the TikTok search term and the number of videos to download when prompted.

## Example

```
Starting TikTok scraper
Enter the TikTok search term: funny cats
Enter the number of videos to download: 5
Searching TikTok for: funny cats
Attempting to fetch 5 video URLs
Found 5 img elements
Found video URL: https://www.tiktok.com/@user/video/1234567890
...
Video downloaded from https://www.tiktok.com/@user/video/1234567890 successfully
Downloaded 5 videos successfully.
TikTok scraper finished
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

# Rename TikTok Videos in Sequence

This script allows you to rename TikTok videos in a specified folder in sequential order.

## Features

- Check if the specified folder exists.
- Get all video files in the folder.
- Sort and rename the video files in sequential order.

## Requirements

- Python 3.x

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/rename-tiktok-videos.git
    cd rename-tiktok-videos
    ```

## Usage

1. Run the script:
    ```sh
    python app/bin/rename_tiktok_video_in_sequence.py
    ```

2. The script will list all available folders in the `app/video` directory.

3. Enter the number corresponding to the folder you want to process.

## Example

```
Available folders:
1. folder1
2. folder2

Enter the number of the folder you want to process: 1
Renamed video1.mp4 to 1.mp4
Renamed video2.mp4 to 2.mp4
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

# Instagram Unfollower

This project allows you to automatically unfollow users on Instagram using Selenium.

## Features

- Authenticate with Instagram using a Chrome profile.
- Navigate to the followers list.
- Unfollow users in a loop with a specified delay.

## Requirements

- Python 3.x
- Selenium
- ChromeDriver

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/instagram-unfollower.git
    cd instagram-unfollower
    ```

2. Install the required libraries:
    ```sh
    pip install selenium python-dotenv
    ```

3. Download ChromeDriver and ensure it is in your PATH.

4. Create a `.env` file in the project directory with the following content:
    ```
    UNFOLLOW_COUNT=100
    WAIT_TIME=4500
    ```

## Usage

1. Run the script:
    ```sh
    python app/bin/instagram_unfollower.py
    ```

2. The script will authenticate with Instagram using the specified Chrome profile, navigate to the followers list, and start unfollowing users.

## Example

```
Initializing Chrome driver...
Chrome driver initialized successfully.
Navigating to Instagram...
Waiting for page to load...
Navigated to Instagram. Current URL: https://www.instagram.com
Already logged in to Instagram.
Attempting to click on the specified element...
Successfully clicked on the element.
Attempting to click on the followers link...
Successfully clicked on the followers link.
Waiting for the followers modal to load...
Followers modal loaded successfully.
Unfollowed account 1
Unfollowed account 2
...
Unfollowing process completed. Total accounts unfollowed: 100
Waiting for 4500 seconds before continuing...
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

# Combine Wide Video

This project allows you to combine multiple videos and overlay an image on them using the `moviepy` library.

## Features

- Resize videos to a specified resolution.
- Overlay an image on the videos.
- Combine multiple videos into one.

## Requirements

- Python 3.x
- moviepy

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/combine-wide-video.git
    cd combine-wide-video
    ```

2. Install the required libraries:
    ```sh
    pip install moviepy
    ```

## Usage

1. Place your video files in the `app/video/original` directory and the overlay image in the `app` directory.

2. Run the script:
    ```sh
    python app/bin/combine_wide_video.py
    ```

3. The script will list all available folders in the `app/video` directory.

4. Enter the number corresponding to the folder you want to process.

## Example

```
Select a folder to process:
1. folder1
2. folder2

Enter the number of the folder you want to process: 1
Processing folder: folder1
Combining videos...
Video combined and saved to app/video/youtube/final_combined.mp4
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

# Combine TikTok Videos

This project allows you to combine multiple TikTok videos into one using the `moviepy` library.

## Features

- Combine multiple TikTok videos into one.
- Move videos longer than 55 seconds to a separate directory.
- Ensure the total duration of combined videos does not exceed 55 seconds.

## Requirements

- Python 3.x
- moviepy

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/combine-tiktok-videos.git
    cd combine-tiktok-videos
    ```

2. Install the required libraries:
    ```sh
    pip install moviepy
    ```

## Usage

1. Place your video files in the `app/video/selected_folder/original` directory.

2. Run the script:
    ```sh
    python app/bin/combine_potrait_video.py
    ```

3. The script will list all available folders in the `app/video` directory.

4. Enter the number corresponding to the folder you want to process.

## Example

```
Available folders:
1. folder1
2. folder2

Enter the number of the folder you want to process: 1
No more video files in the input directory. Processing complete.
Combined video saved as app/video/selected_folder/tiktok/export/combined_tiktok_abc123.mp4
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.