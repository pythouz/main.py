import yt_dlp
import sys
import os

def download_video(url):
    # المجلد المربوط بـ Volumes هو /home/pulseuser
    # أي شيء تحمله هنا سيظهر في المجلد الذي ربطته في جهازك
    save_path = "/home/pulseuser"
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
    }
    
    try:
        print(f"--- بدء التحميل من: {url} ---", flush=True)
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("--- تم التحميل بنجاح في المجلد المحدد ---", flush=True)
    except Exception as e:
        print(f"--- خطأ محاسبي: {str(e)} ---", flush=True)

if __name__ == "__main__":
    # هذا السطر هو الذي يستقبل الرابط من الـ args
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
        download_video(video_url)
    else:
        print("خطأ: لم يتم تزويد رابط الفيديو.", flush=True)
