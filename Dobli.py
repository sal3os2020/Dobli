import requests
from bs4 import BeautifulSoup

# بيانات تسجيل الدخول
email = input("أدخل البريد الإلكتروني أو رقم الهاتف: ")
password = input("أدخل كلمة المرور: ")

# إعدادات الطلب
login_url = "https://m.facebook.com/login.php"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36"
}

# إنشاء جلسة
session = requests.Session()

# تحميل صفحة تسجيل الدخول للحصول على معلومات إضافية
response = session.get(login_url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# العثور على الحقول المخفية (إن وجدت)
hidden_inputs = soup.find_all("input", type="hidden")
form_data = {input_tag["name"]: input_tag["value"] for input_tag in hidden_inputs if "name" in input_tag.attrs}

# إضافة بيانات تسجيل الدخول
form_data.update({
    "email": email,
    "pass": password,
})

# إرسال الطلب لتسجيل الدخول
login_response = session.post(login_url, data=form_data, headers=headers)

# التحقق من نجاح تسجيل الدخول
if "checkpoint" in login_response.url:
    print("تم التعرف على نقطة تحقق (Checkpoint). الرجاء التحقق من حسابك يدويًا.")
elif "save-device" in login_response.url or "home.php" in login_response.url:
    print("تم تسجيل الدخول بنجاح!")
else:
    print("فشل تسجيل الدخول. تأكد من صحة البريد الإلكتروني وكلمة المرور.")
