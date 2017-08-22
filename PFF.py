import json
import requests
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

user = ["ExampleUser1", "ExampleUser2"]
picarto = "https://api.picarto.tv/v1/channel/name/"
userList = ""

for i in range(0, len(user)):
    response = requests.get(picarto + user[i])
    stat = response.status_code
    if response.text.find("\"online\":true") == -1 and stat != 404:
        print(str(i) + "/" + str(len(user)))
    elif stat != 404:
        print(str(i) + "/" + str(len(user)))
        userList = userList + ", " + user[i]
    else:
        print(user[i] + " does not exist.")

if userList == "":
    userList=="No users online."

Notify.init("Online Users")
Hello=Notify.Notification.new("Online Users", userList, "dialog-information")
Hello.show()
