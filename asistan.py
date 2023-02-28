import mysql.connector
import configparser
import datetime
import logging
logging.basicConfig(level=logging.DEBUG)
import random
import re
from mysql.connector import Error
import os
from googlesearch import search

# MySQL veritabanı bağlantısı oluşturma
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Umut123!",
  database="bot"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM users")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# Asistan karşılama mesajı
def welcome_message():
    logging("Merhaba! Ben asistanınız. Nasıl yardımcı olabilirim?")

# Kullanıcı girişi
def giris():
    logging.debug("giris fonksiyonu çağrıldı")

    # Kullanıcı adı ve şifreyi kontrol etme işlemi
    if kontrol:
        logging.debug("giris fonksiyonu: kullanıcı adı ve şifre doğru")
        logging("Giriş başarılı!")
    else:
        logging.debug("giris fonksiyonu: kullanıcı adı veya şifre yanlış")
        logging("Kullanıcı adı veya şifre yanlış!")

# Kullanıcı kaydı
def register():
    username = input("Lütfen kullanıcı adınızı girin: ")
    password = input("Lütfen şifrenizi girin: ")
    sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
    val = (username, password)
    mycursor.execute(sql, val)
    mydb.commit()
    logging("Kayıt başarılı!")

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
    logging(mycursor.rowcount, "adet kayıt eklendi.")

# Veritabanındaki verileri güncelleyen fonksiyon
def veri_guncelle(tablo, kolon, yeni_deger, sorgu):
    sql = "UPDATE " + tablo + " SET " + kolon + " = '" + yeni_deger + "' WHERE " + sorgu
    mycursor.execute(sql)
    mydb.commit()
    logging(mycursor.rowcount, "adet kayıt güncellendi.")

# Veritabanındaki verileri silen fonksiyon
def veri_sil(tablo, sorgu):
    sql = "DELETE FROM " + tablo + " WHERE " + sorgu
    mycursor.execute(sql)
    mydb.commit()
    logging(mycursor.rowcount, "adet kayıt silindi.")
    return mycursor.rowcount
    # Tabloyu sil
def tablo_sil(tablo):
    sql = "DROP TABLE IF EXISTS " + tablo
    mycursor.execute(sql)
    mydb.commit()
    # bot_ogrenciler tablosunu sil
    tablo_sil("ogrenci")
    logging(tablo, "tablosu silindi.")
# Saat sorgusu
def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    logging("Şu an saat " + current_time)

# Döviz kuru sorgusu
def get_exchange_rate():
    currency = input("Hangi döviz kuru hakkında bilgi almak istersiniz? (USD, EUR, GBP vs.): ")
    url = "https://www.tcmb.gov.tr/kurlar/today.xml"
    # urllib kütüphanesi ile XML verisini çekin
    # BeautifulSoup kütüphanesi ile XML verisini parse edin
    # İstenen döviz kurunu veri içinden çekin ve ekrana yazdırın
    logging("1 " + currency + " = " + str(random.uniform(5, 10)) + " TRY")

# Arama motoru sorgusu
def search(query):
    # Google gibi bir arama motoru API'si kullanın veya
    # requests kütüphanesi ile bir arama motoruna GET isteği gönderin ve
    # BeautifulSoup kütüphanesi ile sayfa içeriğini parse edin
    # İlgili bilgileri veri içinden çekin ve ekrana yazdırın
    logging("Sorgu: " + query)

# bot işlevi
def chat():
    welcome_message()
    while True:
        message = input("Sana nasıl yardımcı olabilirim?: ")
        # Çıkış işlemi
        if re.search(r'\b(çıkış|kapat)\b', message, re.IGNORECASE):
            logging("Hoşçakalın!")
logging.exception("Hata oluştu")