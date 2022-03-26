answer = 0
directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
def getNum(x,y):
    if 1 <= x <= 20 and 1 <= y <= 20:
        f = open("data.txt","r")
        return list(map(int, f.readlines()[x-1].split(" ")))[y-1]
        f.close()
    else:
        return 0
for x in range(1,21):
    for y in range(1,21):
        for direction in directions:
            v = getNum(x,y)*getNum(x+direction[0],y+direction[1])*getNum(x+direction[0]*2,y+direction[1]*2)*getNum(x+direction[0]*3,y+direction[1]*3)
            if v > answer:
                answer = v
print(answer)
