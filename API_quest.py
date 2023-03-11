import requests

url = 'https://api.deepai.org/api/nsfw-detector'

headers = {
    'api-key': ''
}

f=open("tekst.txt", "w")

for i in range(1,101):
    a=str(i)+".jpg"
    response = requests.post(
        url,
        files={
            'image': open(a, 'rb'),
        },
        headers=headers
    )
    f.write(str(i)+";"+response.text.split('"nsfw_score": ')[1].split("\n")[0]+"\n")
    print(i, response.text)
f.close()
