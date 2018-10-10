# _*_ coding:utf8-
from math import *

'''
#统计求均值
m=0
f=0
zs=0
fs=0
while(1):
	s=eval(input(">>"))
	if(s==0):
		break
	else:
		f+=1
	if(s>0):
		zs+=1
	else:
		fs+=1
	m+=s
p=m/f
print(zs,fs,p)
'''

#计算学费
p=10000
s=10000
for i in range(10):
	p*=1+0.05
	s+=p
print(p,s)

'''
#统计求均值
m=0
f=0
zs=0
fs=0
while(1):
	s=eval(input(">>"))
	if(s==0):
		break
	else:
		f+=1
	if(s>0):
		zs+=1
	else:
		fs+=1
	m+=s
p=m/f
print(zs,fs,p)
'''

'''
#100-1000之间5和6的公倍数
f=0
for i in range(100,1001):
	if((i%5==0)&(i%6==0)):
		print(i,' ',end='')
		f+=1
	if(f==10):
		print()
		f=0
'''

'''
#最小
n=100
while(n*n<12000):
	n+=1
print(n)
'''

'''
#最大
n=25
while(n*n*n>12000):
	n-=1
print(n)
'''

'''
#贷款
i=0.05
p=eval(input(">>"))
t=eval(input(">>"))
f1=p*pow(1+i,t)
f2=f1/(12*t)
print("%.5f	%.2f	%.2f"%(i,f2,f1))
while(i<=0.08):
	i+=0.00125
	f1=p*pow(1+i,t)
	f2=f1/(12*t)
	print("%.5f	%.2f	%.2f"%(i,f2,f1))
'''

'''
#消除错误
s=50001
m=0
for i in range(50001):
	num=1/(s-i)
	m+=num
print(m)
'''

'''
#数列求和
a=1
b=3
s=1/3
while(a<97):
	a+=2
	b+=2
	s+=a/b
print(s)
'''

'''
#计算pi
x=eval(input(">>"))
a=1
b=2
s=0
for i in range(1,x+1):
	s+=pow((-1),i+1)/(2*i-1)
p=4*s
print(p)
'''

'''
#完全数
for i in range(1,10001):
	s=0;
	for j in range(1,int(i/2+1)):
		if(i%j==0):
			s+=j
	if(s==i):
		print(s)
'''

'''
#组合
f=0
for i in range(1,8):
	for j in range(i+1,8):
		print(i,' ',j)
		f+=1
print(f)
'''		






	