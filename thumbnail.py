import subprocess
import imageio
import os


def get_video_info(file_path):
    try:
        # Get video duration using ffprobe
        ffprobe_cmd = ['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'format=duration', '-of',
                       'default=noprint_wrappers=1:nokey=1', file_path]
        duration = float(subprocess.check_output(ffprobe_cmd).decode('utf-8').strip())

        # Get video thumbnail using imageio
        thumbnail_path = 'thumbnail.jpg'
        vid = imageio.get_reader(file_path)
        thumbnail = vid.get_data(0)
        imageio.imwrite(thumbnail_path, thumbnail)

        # Print or return the information
        print(f"Video Duration: {duration} seconds")
        print(f"Thumbnail saved to: {thumbnail_path}")

        # Clean up the thumbnail file
        os.remove(thumbnail_path)

    except Exception as e:
        print(f"Error: {e}")

# if __name__ == "__main__":
#     video_path = 'your_video.mp4'
#     get_video_info(video_path)
