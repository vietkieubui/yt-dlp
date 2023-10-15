from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
def get_sec(time_str):
    """Get seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


video_name = '0910_LianHuaDao_Katarina_vs_Jayce_MT_13_19.mp4'
video_ouput_name = "cutvideo.mp4"
# video_ouput_name = "1010_Ashuai_Pyke_ft_Kaisa_vs_Gragas_ft_Ezreal_MT_13_19.mp4"
timestamp1 = '00:10:00'
timestamp2 = '00:12:21'
start_time = get_sec(timestamp1)
end_time = get_sec(timestamp2)
ffmpeg_extract_subclip(video_name, start_time, end_time, targetname=video_ouput_name)