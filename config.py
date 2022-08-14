### 基础部分
# 填写你的学号

stutendID = os.environ['STUTENDID']
passward = os.environ['PASSWARD']
mailPass= os.environ['MAILPASS']
receiver = os.environ['RECEIVER']




# 是否仅当打卡失败时才通知，False则打卡成功失败皆通知
sendMsgOnlyError = True



# 发送的邮箱，这里可以设置成与接收邮箱一致（即自己发给自己），或者也可以用其他的
sender = receiver



# 填写发送邮箱的SMTP服务器地址(smtp.qq.com)
mailHost = 'smtp.qq.com'

## ServerChan通知
# Server酱的SCKEY,可以在Server酱的网站注册获取
sckey = ''
