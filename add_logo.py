import moviepy.editor as mp

video = mp.VideoFileClip("cutvideo.mp4")

# logo = (mp.ImageClip("Onechamplol.png")
#           .set_duration(video.duration)
#           .resize(height=50) # if you need to resize...
#           .margin(right=8, top=8, opacity=0) # (optional) logo-border padding
#           .set_pos(("right","top")))

title = mp.ImageClip("Onechamplol.png").set_start(0).set_duration(video.duration).set_pos(("center","center")).re
          .resize(height=50, ) # if you need to resize...
          

final = mp.CompositeVideoClip([video, title])
final.write_videofile("test.mp4")

# final = mp.CompositeVideoClip([video, logo])
# final.write_videofile("test.mp4")