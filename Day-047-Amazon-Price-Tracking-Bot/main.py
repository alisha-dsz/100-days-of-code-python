from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
WEBSITE_URL = "https://www.amazon.in/One94Store-Touch-Control-LED-Lamp/dp/B0DZCGKKNP/ref=sr_1_2_sspa?crid=6XE09VQWKJPP&dib=eyJ2IjoiMSJ9.lSX7FE2gRr3CbvisBxcRl86Zfh2R0YEIgWdxM3XXNTmz5ROK6riBqnL1z74fkt8ztUUsEYmuqLFewW2fPOJRlDDZYYKYZYujKiW61Fc6bIygX-Vs9xL1Qx2rv05w98uVmf73z2I21Hj5Xf4DuLaQrX0_ARnAOU3MfP5pUuJG7J8Rj8GlHV2y809Px-ctRyr15EfBTl_5Fn6Vm58JwOhCPnGmyr9i29voBzhxXYS2yUPSD5uc-zz1HYBQ91QEPEC1KsL6noSklwFkp4L-4VvQerxK9yUdUIXAxmZAA6LUI5c.XmY9iXwmZk_FeZncRsPp2sHwXWgjoyNFLV5Sk6HAW2I&dib_tag=se&keywords=lamp&qid=1792576893&sprefix=lamp%2Caps%2C282&sr=8-2-spons&aref=a1w8dRwgwz&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
header = {
    "Accept-Language": "en-IN,en;q=0.9", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
  }


response = requests.get(url=WEBSITE_URL, headers=header)
soup = BeautifulSoup(response.content, "html.parser")

# Collecting price from website without dollar symbol
price = float(soup.find("span", class_="a-price-whole").getText())
# price_without_dollar = float(price.split("$")[1])

product_title = soup.find("span", id="productTitle").getText().strip()
# Sends email when the price of the product is below the target
if price < 300:
    email_sent = True
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(SENDER_EMAIL, SENDER_PASSWORD)
        connection.sendmail(from_addr=SENDER_EMAIL, 
                            to_addrs=RECEIVER_EMAIL,
                            msg=f"Subject: Amazon Price Alert!\n\n{product_title} is on sale for ₹{price}\n{WEBSITE_URL}".encode("utf-8"))
else:
    email_sent = False
if email_sent:
    print("Email sent successfully!")
else:
    print("Email failed.")