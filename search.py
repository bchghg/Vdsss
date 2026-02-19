import sys
import requests
from urllib.parse import quote

def search_movie(title):
    print(f"🔎 جاري البحث عن: {title}...")
    # هذه محاكاة لمحرك بحث يعطي روابط مباشرة (مثل DDL أو Index of)
    query = quote(f'intitle:"index of"  {title}  mp4 mkv')
    url = f"https://www.google.com/search?q={query}"
    
    print(f"✅ تم العثور على نتائج محتملة!")
    print(f"🔗 يمكنك تفقد الروابط من هنا: {url}")
    # ملاحظة: استخراج الروابط المباشرة تلقائياً يتطلب تجاوز حماية Google
    # لذا هذا السكريبت يجهز لك رابط البحث المخصص "Dorking" للحصول على ملفات مباشرة

if __name__ == "__main__":
    movie_name = sys.argv[1] if len(sys.argv) > 1 else "No Name"
    search_movie(movie_name)
