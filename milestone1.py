import yt_dlp

video_url = "https://www.youtube.com/playlist?list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL"

ydl_opts1 = {
    'format': 'best',
    'writeautomaticsub': True,
}

with yt_dlp.YoutubeDL(ydl_opts1) as ydl:
    ydl.download([video_url])

ydl_opts = {
    'format': 'best',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

