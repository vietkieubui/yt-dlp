from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
def get_sec(time_str):
    """Get seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)



timestamp1 = '01:00:00'
timestamp2 = '01:00:55'
start_time = get_sec(timestamp1)
end_time = get_sec(timestamp2)
ffmpeg_extract_subclip("【2023-10-09 14点场】自宇666：韩服千分顶尖局， [6Aw87O8oGKDMYGkg].mp4", start_time, end_time, targetname="test.mp4")