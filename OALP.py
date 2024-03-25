#ass 3
import sys
import math
def find_ds(infolist):
    dslist = []
    hashlist = []
    order = int(info[0])
    count = order

    for i in range(1, len(infolist)):
        if count != 0:
            adjacency = str(infolist[i]).split()
            dslist.append(len(adjacency))
            count -= 1
        else:
            hashlist.append(get_hash(dslist))
            dslist = []
            order = int(infolist[i])
            count = order
            


    return hashlist

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




info = []   
resultlist = []
for i in range(1000):
    resultlist.append("0")

for line in sys.stdin:
    info.append(line.strip())

hashlist = find_ds(info)

for i in range(len(hashlist)):
    placed = False
    val = int(hashlist[i])
    while placed == False:
        if val == 1000:
            val = 0
        elif resultlist[val] == "0":
            resultlist[val] = "1"
            placed = True
        elif resultlist[val] == "1":
            val += 1
        
        


for i in range(len(resultlist)):
    print(resultlist[i])