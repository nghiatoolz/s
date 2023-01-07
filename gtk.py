import json
import requests
import os
def clear():
    os.system("cls" if os.name =="nt" else "clear")
print("[KAZUTO][INPUT ACCESS_TOKEN FACEBOOK]")
tokenfb = input("INPUT ACCESS TOKEN ACCOUNT: ")
clear()
a = requests.get(f"https://graph.facebook.com/me/accounts?access_token={tokenfb}").json()
data = a["data"]
pro=0
nor=0
write_pro5 = open("token_pro5.txt", "w")
write_nor = open("token_pagenor.txt", "w")
for i in range(len(data)):
    i=i+1
    idpage = data[i-1]["id"]
    name = data[i-1]["name"]
    get_token = data[i-1]["access_token"]
    url = f"https://www.facebook.com/{idpage}"
    res = requests.get(url).url
    if "https://www.facebook.com/people/" in res:
        pro=pro+1
        pro5 = res.split("https://www.facebook.com/people/")[1].split("/")[0]
        print(f"Name: {name}|ID: {idpage}|Type: Pro5|ACCESS_TOKEN: {get_token}")
        write_pro5.write(get_token+"\n")
    else:
        nor=nor+1
        print(f"Name: {name}|ID: {idpage}|Type: Page Normal|ACCESS_TOKEN: {get_token}")
        write_nor.write(get_token+"\n")
    if os.name == "nt":
        os.system(f"title [Kazuto][Pro5: {pro}][Page Normal: {nor}][Total: {pro+nor}]")
    else:
        pass
input("file token pro5 and token page normal store in two file text\nFind it!\nDone!\nWhen press enter key then out this to check!")