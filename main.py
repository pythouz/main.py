import yt_dlp
import sys

def download_video(url):
    # إعدادات المكتبة للتحميل المباشر
    ydl_opts = {
        'format': 'best',
        'outtmpl': '/home/pulseuser/%(title)s.%(ext)s',
    }
    
    try:
        print(f"بدء عملية تحميل الفيديو من: {url}", flush=True)
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("تم التحميل بنجاح في المسار المحلي داخل الحاوية", flush=True)
    except Exception as e:
        print(f"حدث خطأ أثناء التحميل: {str(e)}", flush=True)

if __name__ == "__main__":
    # الرابط الذي ستمرره من الواجهة (Args)
    video_url = sys.argv[1] if len(sys.argv) > 1 else "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    download_video(video_url)
