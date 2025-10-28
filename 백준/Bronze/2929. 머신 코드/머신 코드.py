import re
t = input()
p = re.split('(?=[A-Z])',t)

cnt = 0    
for i in range(1,len(p)-1):
    a= len(p[i]) % 4
    if a!= 0: cnt+=(4-a)    
print(cnt)