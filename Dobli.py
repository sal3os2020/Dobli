# -*- coding: utf-8 -*-
import platform, os, sys

def cetak(x, e=0):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\033[%s;1m' % str(31 + j))
    x += '\033[0m'
    x = x.replace('!0', '\033[0m')
    if e != 0:
        sys.stdout.write(x)
    else:
        sys.stdout.write(x + '\n')

if platform.python_version().split('.')[0] != '3':
    cetak('!m[!] يرجى استخدام Python 3.x لتشغيل هذا الكود.')
    sys.exit()

import cookielib, re, urllib.request, urllib.parse, threading
try:
    import mechanize
except ImportError:
    cetak('!m[!] يبدو أن المكتبة !cmechanize!m غير مثبتة...\n!h[!] pip install mechanize')
    sys.exit()

# تعريف المتصفح
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_cookiejar(cookielib.LWPCookieJar())
br.set_handle_redirect(True)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')]

def login():
    """وظيفة تسجيل الدخول إلى فيسبوك"""
    email = input('[?] أدخل البريد الإلكتروني أو رقم الهاتف: ')
    password = input('[?] أدخل كلمة المرور: ')
    try:
        br.open('https://m.facebook.com')
        br.select_form(nr=0)
        br.form['email'] = email
        br.form['pass'] = password
        br.submit()
        if 'save-device' in br.geturl() or 'm_sess' in br.geturl():
            cetak('!h[*] تسجيل الدخول ناجح.')
        elif 'checkpoint' in br.geturl():
            cetak('!m[!] الحساب مقيد أو يواجه مشكلة "Checkpoint".')
            sys.exit()
        else:
            cetak('!m[!] فشل تسجيل الدخول. تأكد من صحة البيانات.')
            sys.exit()
    except Exception as e:
        cetak(f'!m[!] حدث خطأ أثناء تسجيل الدخول: {e}')
        sys.exit()

def main_menu():
    """عرض القائمة الرئيسية"""
    cetak("\n!h[1] جمع معرفات الأصدقاء\n[2] جمع معرفات المجموعة\n[3] الخروج")
    choice = input('[?] اختر خياراً: ')
    if choice == '1':
        cetak('!h[*] هذه الميزة قيد التطوير.')
    elif choice == '2':
        cetak('!h[*] هذه الميزة قيد التطوير.')
    elif choice == '3':
        cetak('!m[!] الخروج.')
        sys.exit()
    else:
        cetak('!m[!] خيار غير صحيح. حاول مرة أخرى.')
        main_menu()

if __name__ == "__main__":
    cetak('!h[*] بدء البرنامج...')
    login()
    main_menu()
