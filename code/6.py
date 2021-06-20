import base64

id = b"admin"
pw = b"nimda"
i = 0

for i in range(20):
    id = base64.b64encode(id)
    pw = base64.b64encode(pw)

# UTF-8로 디코딩
id = id.decode()
pw = pw.decode()

change = str.maketrans('!@$^&*()', '12345678')

id = id.translate(change)
pw = pw.translate(change)

print('id : {}\npw : {}'.format(id,pw))

