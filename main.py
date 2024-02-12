import telebot
import os
import smtplib
import mimetypes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


token = '6739217361:AAEDnx_5N7VR3qhSkW0_up7i1TN2MtUo3Nk'
bot = telebot.TeleBot(token)
email = None



@bot.message_handler(commands=['start'])
def start(message):
    sent_message = bot.send_message(message.chat.id, f'{message.from_user.first_name}, enter your e-mail.')
    bot.register_next_step_handler(sent_message, save_email)

def save_email(message):
    email = message.text



@bot.message_handler(commands=['sendphoto'])
def send_photo(message):
    sent_message = bot.send_message(message.chat.id, 'Sent your photo:')
    bot.register_next_step_handler(sent_message, send_email_with_photo)

def upload_photo(photo):
    print(f'Photo {photo}')
    message = type('', (), {'photo': [photo]})()
    send_email_with_photo(message)



@bot.message_handler(commands=['sendtext'])
def send_text(message):
    sent_message = bot.send_message(message.chat.id, 'Write your text:')
    bot.register_next_step_handler(sent_message, send_email_with_text)


def send_email_with_photo(message):
    sender = "ekimaru000@gmail.com"
    password = "gzhl eadd etqa bgop"
    
    text = MIMEText('You have been recieved the photo.')
    msg = MIMEMultipart()
    msg['Subject'] = 'Photo from Telegram'
    msg['From'] = sender
    msg['To'] = "gertsovmax8@gmail.com"
    msg.attach(text)

    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    temp_file_name = 'temp.jpg'
    with open(temp_file_name, 'wb') as temp_file:
        temp_file.write(downloaded_file)

    with open(temp_file_name, 'rb') as image_file:
        image = MIMEImage(image_file.read(), name=os.path.basename(temp_file_name))
        msg.attach(image)
    os.remove(temp_file_name)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, "gertsovmax8@gmail.com", msg.as_string())
        return "The message was sent"


def send_email_with_text(message):
    sender = "ekimaru000@gmail.com"
    password = "gzhl eadd etqa bgop"
    
    text = MIMEText(message.text)
    msg = MIMEMultipart()
    msg['Subject'] = 'Photo from Telegram'
    msg['From'] = sender
    msg['To'] = "gertsovmax8@gmail.com"
    msg.attach(text)
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, "gertsovmax8@gmail.com", msg.as_string())
        return "The message was sent"


def open_url(url):
    import urllib.request
    return urllib.request.urlopen(url)


bot.polling(none_stop=True)