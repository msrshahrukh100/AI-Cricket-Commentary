
import cv2
import base64
from openai import OpenAI
from moviepy.editor import AudioFileClip, ImageClip, concatenate_videoclips

# import os
# os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"

# client = OpenAI()



def add_static_image_to_audio():
    
    video_clips = []
    for i in range(1, 5):
        audio_clip = AudioFileClip(f"commentary/{i}.mp3")
        image_clip = ImageClip(f"commentary/{i}.png")
        video_clip = image_clip.set_audio(audio_clip)
        # specify the duration of the new clip to be the duration of the audio clip
        video_clip.duration = audio_clip.duration
        # set the FPS to 1
        video_clip.fps = 1
        # write the resuling video clip
        video_clips.append(video_clip)
    
    final_clip = concatenate_videoclips(video_clips)
    final_clip.write_videofile("result.mp4")

add_static_image_to_audio()

# def create_audio(content, file_number):
    
#     response = client.audio.speech.create(
#       model="tts-1",
#       voice="alloy",
#       input=content
#     )

#     response.stream_to_file(f"commentary/{file_number}.mp3")


# video = cv2.VideoCapture("YuvrajSixes.mp4")

# fps = video.get(cv2.CAP_PROP_FPS)
# frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
# duration = frame_count/fps
# print(f"Duration(S): {duration} Duration: {int(duration/60)}:{int(duration%60)} FPS: {fps}")

# base64Frames = []
# while video.isOpened():
#     success, frame = video.read()
#     if not success:
#         break
#     _, buffer = cv2.imencode(".jpg", frame)
#     base64Frames.append(base64.b64encode(buffer).decode("utf-8"))

# video.release()
# print(len(base64Frames), "frames read.")

# messages = []
# just_messages = []
# i = 0
# for frame in base64Frames[::125]:
#     i += 1
#     with open(f"commentary/{i}.png", "wb") as fh:
#         fh.write(base64.decodebytes(frame.encode("utf-8")))
#     messages.append(
#         {
#             "role": "user",
#             "content": [
#                 "This is the frame from a cricket match. Generate a compelling commentary of the match. Do not include greetings at start.",
#                 {"image": frame, "resize": 768},
#             ]
#         }
#     )
    
#     params = {
#         "model": "gpt-4-vision-preview",
#         "messages": messages,
#         "max_tokens": 70,
#     }

#     result = client.chat.completions.create(**params)
#     messages.append(
#         {
#             "role": "assistant",
#             "content": result.choices[0].message.content
#         }
#     )
#     create_audio(result.choices[0].message.content, i)
#     # just_messages.append(result.choices[0].message.content)
#     if i == 4:
#         break

# print(just_messages)