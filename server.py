from SimpleXMLRPCServer import SimpleXMLRPCServer
import os
import lineTool
import requests
#send message
def message(token, msg):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    r = requests.post(url, headers=headers, params=payload)
    return r.status_code
#send stickers
def Stickers(token,msg, stickerPackageId, stickerId):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token
    }
    payload = {'message': msg,"stickerPackageId": stickerPackageId, 'stickerId': stickerId}
    r = requests.post(url, headers=headers, params=payload)
    return r.status_code
#send img
def img(token,msg, picURI):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token
    }
    files = {'imageFile': open(picURI, 'rb')}
    payloads = {'message': msg}
    r = requests.post(url, headers=headers, params=payloads, files=files)
    return r.status_code
    # send message
if __name__ == '__main__':
    s = SimpleXMLRPCServer(('127.0.0.1', 8888))
    s.register_function(message)
    s.register_function(Stickers)
    s.register_function(img)
    s.serve_forever()