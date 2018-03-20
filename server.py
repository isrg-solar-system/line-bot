from SimpleXMLRPCServer import SimpleXMLRPCServer
import os
import lineTool
import requests
def lineNotify(token, msg, picURI):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token
    }
    files = {'imageFile': open(picURI, 'rb')}
    payload = {'message': msg}
    # payload = {"message": msg, "stickerPackageId": stickerPackageId, 'stickerId': stickerId}
    r = requests.post(url, headers=headers, params=payload, files = files)
    return r.status_code
#send message

if __name__ == '__main__':
    s = SimpleXMLRPCServer(('127.0.0.1', 8888))
    s.register_function(lineNotify)
    s.serve_forever()