import mysql.connector
import datetime
import random
import re
import mysql.connector

# MySQL veritabanı bağlantısı oluşturma
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Umut123!",
  database="chatbot"
)

# MySQL veritabanı bağlantı noktası
mycursor = mydb.cursor()

# Öğrenciler tablosunu oluşturma
mycursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler (id INT AUTO_INCREMENT PRIMARY KEY, isim VARCHAR(255), soyisim VARCHAR(255), yas VARCHAR(255))")


# Veritabanı işlemleri yapılacak buradan devam edebilirsiniz



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
