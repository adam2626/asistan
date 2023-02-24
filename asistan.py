import mysql.connector
import datetime
import random
import re
import mysql.connector
from googlesearch import search

# MySQL veritabanı bağlantısı oluşturma
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Umut123!",
  database="chatbot"
)

# MySQL veritabanı bağlantı noktası
mycursor = mydb.cursor()
sql = "SELECT * FROM ogrenciler"
mycursor.execute(sql)
girdi = input("Lütfen bir sorgu giriniz: ")
mycursor.execute(girdi)
# Öğrenciler tablosunu oluşturma
mycursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler (id INT AUTO_INCREMENT PRIMARY KEY, isim VARCHAR(255), soyisim VARCHAR(255), yas VARCHAR(255))")


# Veritabanı işlemleri yapılacak buradan devam edebilirsiniz
# Veritabanına sorgu gönderen fonksiyon
def sorgu_gonder(sorgu):
    mycursor.execute(sorgu)
    sonuc = mycursor.fetchall()
    return sonuc

# Veritabanına veri ekleyen fonksiyon
def veri_ekle(tablo, sütunlar, değerler):
    sql = "INSERT INTO " + tablo + " (" + sütunlar + ") VALUES (" + değerler + ")"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "adet kayıt eklendi.")

# Veritabanındaki verileri güncelleyen fonksiyon
def veri_guncelle(tablo, kolon, yeni_deger, sorgu):
    sql = "UPDATE " + tablo + " SET " + kolon + " = '" + yeni_deger + "' WHERE " + sorgu
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "adet kayıt güncellendi.")

# Veritabanındaki verileri silen fonksiyon
def veri_sil(tablo, sorgu):
    sql = "DELETE FROM " + tablo + " WHERE " + sorgu
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "adet kayıt silindi.")


# SQL sorgusunu çalıştır
mycursor.execute(sql)

# Değişiklikleri kaydet
mydb.commit()


# Bağlantıyı kontrol etmek için
if mydb.is_connected():
    print("Bağlantı başarılı!")
else:
    print("Bağlantı başarısız.")

# Veritabanı işlemleri için bir cursor oluşturun
mycursor = mydb.cursor()

# Asistan karşılama mesajı
def welcome_message():
    print("Merhaba! Ben asistanınız. Nasıl yardımcı olabilirim?")

# Kullanıcı girişi
def login():
    username = input("Lütfen kullanıcı adınızı girin: ")
    password = input("Lütfen şifrenizi girin: ")
    sql = "SELECT * FROM users WHERE username = %s AND password = %s"
    val = (root, 'Umut123!')
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    if result:
        print("Giriş başarılı!")
    else:
        print("Kullanıcı adı veya şifre yanlış.")

# Kullanıcı kaydı
def register():
    username = input("Lütfen kullanıcı adınızı girin: ")
    password = input("Lütfen şifrenizi girin: ")
    sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
    val = (username, password)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Kayıt başarılı!")

    query = "Python programlama dili"
num_results = 5

for i, url in enumerate(search(query, num_results=num_results)):
    print(f"{i+1}. {url}")
# Saat sorgusu
def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Şu an saat " + current_time)

# Döviz kuru sorgusu
def get_exchange_rate():
    currency = input("Hangi döviz kuru hakkında bilgi almak istersiniz? (USD, EUR, GBP vs.): ")
    url = "https://www.tcmb.gov.tr/kurlar/today.xml"
    # urllib kütüphanesi ile XML verisini çekin
    # BeautifulSoup kütüphanesi ile XML verisini parse edin
    # İstenen döviz kurunu veri içinden çekin ve ekrana yazdırın
    print("1 " + currency + " = " + str(random.uniform(5, 10)) + " TRY")

# Arama motoru sorgusu
def search(query):
    # Google gibi bir arama motoru API'si kullanın veya
    # requests kütüphanesi ile bir arama motoruna GET isteği gönderin ve
    # BeautifulSoup kütüphanesi ile sayfa içeriğini parse edin
    # İlgili bilgileri veri içinden çekin ve ekrana yazdırın
    print("Sorgu: " + query)

# Chatbot işlevi
def chat():
    welcome_message()
    while True:
        message = input("Sana nasıl yardımcı olabilirim?: ")
        # Çıkış işlemi
        if re.search(r'\b(çıkış|kapat)\b', message, re.IGNORECASE):
            print("Hoşçakalın!")
            break
            print()
