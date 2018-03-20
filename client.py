from xmlrpclib import ServerProxy
import requests
import time
token = "輸入TOKEN"
msg = "Have a nice day"
#send picture
stickerPackageId = 1
stickerId = 2
#send img
picURI = "圖片位址"
if __name__ == '__main__':
    s = ServerProxy("http://127.0.0.1:8888")
    s.message(token, msg)
    s.Stickers(token, msg,stickerPackageId, stickerId)
    s.img(token,msg, picURI)