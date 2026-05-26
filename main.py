import yt_dlp
import sys
import os

def run_download_tool(url):
    # المجلد المربوط في الحاوية (لا تغيره)
    save_path = "/home/pulseuser"
    
    # خيارات التحميل (جودة عالية + حفظ بالعنوان)
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'quiet': False,
    }
    
    print(f"--- [PulseEngine] بدء معالجة الرابط: {url} ---", flush=True)
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        # التأكد من نجاح العملية محاسبياً (Audit)
        files = os.listdir(save_path)
        print(f"--- [PulseEngine] تم التحميل بنجاح. المحتويات الحالية: {files} ---", flush=True)
        
    except Exception as e:
        print(f"--- [PulseEngine] خطأ أثناء التشغيل: {str(e)} ---", flush=True)

if __name__ == "__main__":
    # استلام الرابط من الـ Arguments
    if len(sys.argv) > 1:
        run_download_tool(sys.argv[1])
    else:
        print("--- [PulseEngine] خطأ: يرجى إدخال رابط يوتيوب في حقل الـ Arguments ---", flush=True)
