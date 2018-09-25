# -*- coding:utf8-

'''
#温度转换
c=float(input(">>"))
f=(9/5)*c+32
print(f)
'''

'''
#圆柱体体积
from math import *
r,h=eval(input(">>"))
a=pow(r,2)*3.141
v=a*h
print(a,'\n',v)
'''

'''
#长度转换
feet=float(input(">>"))
meter=feet*0.305
print(meter)
'''

'''
#计算能量
m=float(input(">>"))
i=float(input(">>"))
f=float(input(">>"))
q=m*(f-i)*4184
print(q)
'''

'''
#计算利息
b,r=eval(input(">>"))
i=b*(r/1200)
print(i)
'''

'''
#计算加速度
from math import *
v0,v1,t=eval(input(">>"))
a=fabs((v0-v1))/t
print(a)
'''

'''
#计算复利
m=float(input(">>"))
f=1.00417
sum=m*f
for i in range(5):
	sum+=100
	sum*=f	
print(sum)
'''


#位数求和
s = float(input(">>"))
if (0<=s<10):
	print(s)
elif 10<=s<100:
	a=s%10
	b=s//10
	print(a+b)
else:
	a=s%10
	b=s//10%10
	c=s//100
	print(a+b+c)
