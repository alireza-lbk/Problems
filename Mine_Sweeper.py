row,column=input().split()
mine_number = int(input())
mine_coordinate=[]
for mine in range(mine_number):
   mine_coordinate.append(list(map(int,input().split())))
mine_coordinate.sort()
row=int(row)
column=int(column)
map = []
for x in range(row):
    map.append([])
    for y in range(column):
        map[x].append(0)
for mine in mine_coordinate:
    map[mine[0]-1][mine[1]-1]='*'
###################################
for i in range(row):
    for j in range(column):
        if map[i][j]=='*':
            if i-1>=0 and j-1>=0 and map[i-1][j-1]!='*':
                map[i-1][j-1]+=1
            if i-1>=0 and map[i-1][j]!='*':
                map[i-1][j]+=1
            if i-1>=0 and j+1<=column-1 and map[i-1][j+1]!='*':
                map[i-1][j+1]+=1
            if j-1>=0 and map[i][j-1]!='*':
                map[i][j-1]+=1
            if j+1<=column-1 and map[i][j+1]!='*':
                map[i][j+1]+=1
            if i+1<=row-1 and j-1>=0 and map[i+1][j-1]!='*':
                map[i+1][j-1]+=1
            if i+1<=row-1 and map[i+1][j]!='*':
                map[i+1][j]+=1
            if i+1<=row-1 and j+1<=column-1 and map[i+1][j+1]!='*':
                map[i+1][j+1]+=1
for k in range(row):
    for t in range(column):
        print(map[k][t],end=' ')
    print("")
