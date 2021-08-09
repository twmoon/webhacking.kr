from hashlib import sha1

f = open("RT_all.csv", 'w')

for i in range(10000000, 100000000):

    result = str(i) + "salt_for_you"

    for j in range(0, 500):
        result = sha1(result.encode('utf-8')).hexdigest()

    print(str(i) + ", " + result)
    f.write(str(i) + ", " + result + "\n")

f.close()
