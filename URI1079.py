N=int(input())
nums=[]
for i in range(N):
    x,y,z=input().split()
    x,y,z=float(x),float(y),float(z)
    nums.extend([[x,y,z]])

for j in range(N):
    sums=(nums[j][0])*2+(nums[j][1])*3+(nums[j][2])*5
    average=sums/10
    
    print(round(average,1))
