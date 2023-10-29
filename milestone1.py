import yt_dlp

video_url = "https://www.youtube.com/playlist?list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL"

'''
video_url =["https://youtu.be/480OGItLZNo?si=UPNt-RU-MUNgBbhk",
        "https://youtu.be/OA2Tj75T3fI?si=c1YBtcEj3DGmBYR2",
        "https://youtu.be/qrvK_KuIeJk?si=KiosPdQAE_cdYnPW",
        "https://youtu.be/oFVuQ0RP_As?si=ty7p4XCKY6blcE1a",
        "https://youtu.be/4aPp8KX6EiU?si=d22OkX8m4kgPbV67",
        "https://youtu.be/4aPp8KX6EiU?si=bLZs8RZYbg8maYdx",
        "https://youtu.be/h8PSWeRLGXs?si=ScsYIEgN7Wk02Y4m",
        "https://youtu.be/Y9nM_9oBj2k?si=nGEnVvnCihfKO90I",
        "https://youtu.be/ervLwxz7xPo?si=Bk3wGqXvzmCWNrr1",
        "https://youtu.be/ervLwxz7xPo?si=J0ZXIB5l-VexP3wi",
        "https://youtu.be/O6zdi6Q6p7o?si=F0_3SrOdHmF8vLpn",
        "https://youtu.be/YBY-CdpH0CA?si=p_0vh5kWttZtUEKF"]
'''
            
def downloader(link):
    ydl_opts1 = {
        'format': 'best',
        'writeautomaticsub': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts1) as ydl:
        ydl.download([link])
    
    ydl_opts = {
        'format': 'best',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

#for i in video_url:
#    downloader(i)

downloader(video_url)
