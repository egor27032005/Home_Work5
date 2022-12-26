file=open('for_Task4.txt', 'r')
map=file.readline()
file.close
long=len(map)
map2=list(map)
rle=''
sum=1
f=0
for i in range(long-1):
    if map2[i]==map2[i+1]:
        sum+=1
    else:
        rle+=str(sum)
        rle+=map2[i]
        f+=sum
        sum=1
rle+=str(long-f)
rle+=map2[long-1]
map3=list(rle)
long=len(map3)
rle2=''
for i in range(1,long,2):
   a=int(map3[i-1])
   while(a>0):
      rle2+=map3[i]
      a-=1
file2=open('2for_Task4.txt', 'w')
file2.write(rle +"\n"+ rle2)
file2.close

