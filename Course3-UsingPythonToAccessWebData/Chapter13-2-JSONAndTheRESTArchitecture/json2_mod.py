import json
import urllib.request
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
uh = urllib.request.urlopen(url, context=ctx).read()
data = uh.decode()


info = json.loads(data)
# print('User count:', len(info))
sum = 0
count = 0
for item in info['comments']:
    # print('Name', item['name'])
    # print('Id', item['id'])
    # print('Attribute', item['x'])
    sum = sum + int(item['count'])
    count = count + 1

print('Count:', count)
print('Sum:', sum)
