arr=[0, 2, 0, 3, 4, 0, 5, 0]
n=len(arr)
cnt0=0
cntr=0
random=[]

for i in range(0,n):
    sort_array=[]

for i in range(0,n):
    if arr[i]!=0:
        cntr+=1
        random.append(arr[i])
    elif arr[i]==0:
        cnt0+=1
        
    i = 0
	
	
while (cntr > 0): 
		sort_array.append(random[i])
		i+=1
		cntr-=1

while (cnt0 > 0): 
       arr[i] = 0
       sort_array.append(arr[i])
       i+=1
       cnt0-=1

print(sort_array)