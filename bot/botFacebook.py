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

# Auto Posting Halaman Facebook
def autoPostingFacebook():
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT product_name, product_price, product_rating, product_link, product_img FROM database_post")
    database_post = mycursor.fetchall()
    random_index = random.randrange(len(database_post))
    
    shopeid =1

    page_id= 105258409090407 
    facebook_access_token= 'EAAS1MRIVS4gBAFTx5PpZBtpFdm0TBLn60bBRq4EE4YR9fZB4ji6C9RZAiksiZBzp97001TrM1qUxvWMJ7WkibysHu6CCZBxyD0pWyaGyNuKMYYmn8TpzZAVPwD0VJeHkupoxZBAeHYiieXdexbd1KAkZCtHLZB082ME26y16CSVRKaQz8P2f5BMm0'
    statusTweet = "ā¼ PROMO DISKON ā¼\n\n{}\n\nāļø DISKON : {}\n\nCheckout Sekarang š\n{}".format(database_post[random_index]['product_name'], database_post[random_index]['product_rating'], shortLinkShopee(database_post[random_index]['product_link'],shopeid, "idmyfashion", "Facebook" ))
    # post_url = 'https://graph.facebook.com/{}/feed'.format(page_id_1)
    post_url = 'https://graph.facebook.com/v5.0/{}/photos'.format(page_id)
    imgUrl = database_post[random_index]['product_img']

    payload = {
        'message': statusTweet,
        'access_token': facebook_access_token,
        'url': imgUrl
    }
    
    try:
        posting = requests.post(post_url, data=payload)
        print("ā - Posting Berhasil\n")
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