x,y=map(float,input().strip().split())
x=x*(1000/y)
n=int(input())
for _ in range(n):
    x1,y1=map(float,input().strip().split())
    if x>x1*(1000/y1):
        x=x1*(1000/y1)
print("%.2f" %x)