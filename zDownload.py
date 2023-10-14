import youtube_dl

def download_douyu_video(video_url):
  """Downloads a Douyu video."""

  ydl_opts = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s',
  }

  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

if __name__ == '__main__':
  video_url = 'https://v.douyu.com/show/yVY8WwdnagAvLOz9'
  download_douyu_video(video_url)
