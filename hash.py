# array=[2,5,1,2,3,5,1,2,4]
# array=[2,1,1,2,3,5,1,2,4]
array=[1,2,3,4]
temp=[]
f=0

for i in array:
    if i in temp:
        print(i)
        f=1
        break
    else:
        temp.append(i)

if f==0:
    print('undefined')