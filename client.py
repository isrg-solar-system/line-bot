from xmlrpclib import ServerProxy
import requests
import time
time.sleep(3)
token = "gC4LQPE6Rcm1AgJTfLSFtokdP6bXvVpp9J8EbG8TkLR"
msg = "Have a nice day"
#send picture
stickerPackageId = 1
stickerId = 2
#send img
picURI = "C:/Users/WuJunHao/Desktop/x64/win.jpg"
if __name__ == '__main__':
    s = ServerProxy("http://127.0.0.1:8888")
    s.lineNotify(token, msg,picURI)