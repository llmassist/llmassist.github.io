import cv2
from moviepy.editor import VideoFileClip


def split_video(input_video_path):
    # Read the video
    cap = cv2.VideoCapture(input_video_path)

    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Define the codec and create VideoWriter objects
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out1 = cv2.VideoWriter("temp_video_part1.avi", fourcc, fps, (frame_width // 2, frame_height))
    out2 = cv2.VideoWriter("temp_video_part2.avi", fourcc, fps, (frame_width // 2, frame_height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Split the frame into two parts
        left_side = frame[:, : frame_width // 2]
        right_side = frame[:, frame_width // 2 :]

        # Write the split frames
        out1.write(left_side)
        out2.write(right_side)

    # Release everything when done
    cap.release()
    out1.release()
    out2.release()
    cv2.destroyAllWindows()

    # Convert to MP4 using MoviePy for better compatibility
    clip1 = VideoFileClip(f"temp_video_part1.avi")
    clip1.write_videofile(f"{input_video_path[:-4]}_pdm_closed.mp4", codec="libx264")

    clip2 = VideoFileClip("temp_video_part2.avi")
    clip2.write_videofile(f"{input_video_path[:-4]}_llm_assist.mp4", codec="libx264")

    # Optional: Remove temporary AVI files
    import os

    os.remove("temp_video_part1.avi")
    os.remove("temp_video_part2.avi")


# Usage
split_video("static/qualitative/scenario_4.mp4")
split_video("static/qualitative/scenario_5.mp4")
