import pandas as pd
import random
import requests
import mysql.connector

# Connect Database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="shopee_aff"
)

def autoPostingTelegram():
  print("\nš§ AUTO POSTING")

  mycursor = mydb.cursor(dictionary=True)
  mycursor.execute("SELECT product_name, product_price, product_rating, product_link, product_img FROM database_post")
  database_post = mycursor.fetchall()

  shopeid =1
  
  idChannelTelegrams = ['-1001658353827', '-1001866060533']

  for channelTelegram in idChannelTelegrams:
    try:
        random_index = random.randrange(len(database_post))
        statusTelegram = "ā¼ FLASH SALE ā¼\n\n{}\n\nāļø DISKON : {}\n\nCheckout Sekarang š\n{}".format(database_post[random_index]['product_name'], database_post[random_index]['product_rating'], shortLinkShopee(database_post[random_index]['product_link'], shopeid, "racunshopee", "Telegram" ))
        message = 'https://api.telegram.org/bot5479078966:AAECnT7JEy4hNpjHGUzdZtSTsgOOjN22O_8/sendPhoto?chat_id={}&photo={}&caption={}'.format(channelTelegram, database_post[random_index]['product_img'], statusTelegram)
        requests.post(message)

        print("ā - Posting Berhasil")
    except:
        pass

def shortLinkShopee(link, idshopee, akun, sosialmedia):
  mycursor = mydb.cursor(dictionary=True)
  mycursor.execute("SELECT id, appid, rahasia FROM account_shopeeaff WHERE id={}".format(idshopee))
  account_shopee = mycursor.fetchall()

  from shopee_affiliate import ShopeeAffiliate    
  sa = ShopeeAffiliate(account_shopee[0]['appid'], account_shopee[0]['rahasia'])
  res = sa.generateShortLink(link, akun, sosialmedia)
  res = res.replace("shope", "shpe")
  return(res)