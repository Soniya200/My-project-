list1=[[1,2,3],[10,20,30],[100,200,500]]
max=0
for i in list1:
    sum=0
    for j in i:
        sum+=j
        if(sum>max):
            sum=max
print(i)
