#OADH
import sys
import math
def find_ds(infolist):
    dslist = []
    hashlist = []
    hash2 = []
    order = int(info[0])
    count = order

    for i in range(1, len(infolist)):
        if count != 0:
            adjacency = str(infolist[i]).split()
            dslist.append(len(adjacency))
            count -= 1
        else:
            hashlist.append(get_hash(dslist))
            hash2.append(get_hash2(dslist))
        
            dslist = []
            order = int(infolist[i])
            count = order
    return (hashlist, hash2)

def get_hash(dslist):
    dslist.sort(reverse = True)
    ds = "".join(str(i) for i in dslist)
    
    if (len(ds) < 3) or (len(ds) % 2 == 0):
        ds += "0"
    mid = math.floor(len(ds)/2)
    d = ds[mid-1:mid+2]
    d = int(d)*int(d)
    d = str(d)
    if (len(d) < 3) or (len(d) % 2 == 0):
        while (len(d) < 3) or (len(d) % 2 == 0):
            d += "0"

    mid = math.floor(len(d)/2)
    hash = d[mid-1:mid+2]
    return hash

def get_hash2(dslist):
    dslist.sort(reverse = True)
    ds = "".join(str(i) for i in dslist)
    if len(ds) < 3:
        ds = "0" + ds
    h2 = ds[:3]
    return h2

info = []   
resultlist = []
for i in range(1000):
    resultlist.append("0")

for line in sys.stdin:
    info.append(line.strip())

hashlist = find_ds(info)

for i in range(len(hashlist[0])):
    placed = False
    val = int(hashlist[0][i])
    delta = int(hashlist[1][i]) + 1
    while placed == False:
        if val >= 1000:
            val = val - 1000
        elif resultlist[val] == "0":
            resultlist[val] = "1"
            placed = True
        elif resultlist[val] == "1":
            val += delta
            if delta > 1:
                delta -= 1

        
for i in range(len(resultlist)):
   print(resultlist[i])