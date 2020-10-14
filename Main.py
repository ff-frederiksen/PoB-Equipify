import pobapi

url = 'https://pastebin.com/Y2YMA0fr'

build = pobapi.from_url(url)

for item in build.items:
    print(item)
    break
