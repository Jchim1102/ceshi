import smtplib, datetime, time
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from time import sleep


def SendQQMail_Text(text_content):  # 发送附件邮件

    smtpserver = 'smtp.qq.com'
    user = "2856140498@qq.com"  # 发送邮件的邮箱
    sender_pwd = 'smsoqgahusybdehi'  # 授权码！！！

    sender = '2856140498@qq.com'  # 发送邮箱

    to_list = ['1470229484@qq.com']
    receiver = ','.join(to_list)
    msg = MIMEMultipart()
    # now = time.strftime('%Y_%m_%d %H_%M_%S')
    sleep(2)


    msg["from"] = sender  # 发件人
    msg["to"] = receiver  # 收件人
    # msg["to"] = ";".join(receiver) # 多个收件人 list 转 str
    msg["subject"] = Header('--★邮件主题★--')  # 发送的邮件的主题

    body = text_content
    msg.attach(MIMEText(body, 'plain'))

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)  # 连服务器
    smtp.login(user, sender_pwd)
    smtp.sendmail(msg["from"], msg["to"].split(','), msg.as_string())

    # print("已发送内容:\n",text_content)

    smtp.quit()


SendQQMail_Text('--《来自 项目》速速去续期 hax 和 woiden--')
