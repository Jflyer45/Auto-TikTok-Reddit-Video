from moviepy.editor import *

def chopIntoSegments(videoPath, segLength, fileName):
    baseVideoClip = VideoFileClip(videoPath)
    print(f"Video is {baseVideoClip.duration} long")

    clipsToMake = int(baseVideoClip.duration/segLength)

    currentTime = 0
    for i in range(0, clipsToMake):

        videoclip = baseVideoClip.subclip(currentTime, currentTime + segLength)
        videoclip.write_videofile(f"{fileName}{i+1}.mp4", threads=10)
        currentTime += segLength
    print("Clips complete")

chopIntoSegments("Utls/finalMinecraft.mp4", 180, "clip")