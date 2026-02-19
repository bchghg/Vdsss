import sys
import requests
import re

def get_direct_links(query):
    print(f"🚀 جاري استخراج الروابط المباشرة لـ: {query}...")
    
    # استخدام محرك بحث متقدم للسيرفرات المفتوحة
    search_url = f"https://www.google.com/search?q=intitle:index.of?mkv+mp4+{query.replace(' ', '+')}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # ملاحظة: سنستخدم مكتبة قوية لجلب النتائج إذا كانت متوفرة
        response = requests.get(search_url, headers=headers)
        # استخراج أي رابط يبدأ بـ http وينتهي بامتداد فيديو
        links = re.findall(r'(https?://[^\s<>"]+\.(?:mkv|mp4|avi))', response.text)
        
        if not links:
            # محاولة البحث في محرك ملفات مباشر
            print("⚠️ لم أجد روابط مباشرة في الصفحة الأولى، جاري تجربة سيرفرات الـ DDL...")
            # هنا يمكنك إضافة API لمواقع مثل FileIndex إذا كان لديك مفتاح
            print(f"💡 نصيحة: جرب كتابة الاسم بدقة بالإنجليزية.")
        else:
            print(f"✅ وجدنا {len(links)} روابط مباشرة:")
            for link in list(set(links))[:10]: # عرض أول 10 روابط فريدة
                print(f"🔗 {link}")
                
    except Exception as e:
        print(f"❌ خطأ في الاتصال: {e}")

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else ""
    if name:
        get_direct_links(name)
    else:
        print("أدخل اسم الفيلم يا بطل!")
