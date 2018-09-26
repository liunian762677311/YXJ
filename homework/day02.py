#_*_ coding:utf8- 

from math import *
from random import *

'''
#五边形面积
r=eval(input(">>"))
s=5*pow(2*r*sin(pi/5),2)/(4*tan(pi/5))
print(s)
'''

'''
#大圆距离
x1,y1=eval(input(">>"))
x2,y2=eval(input(">>"))
r=6371.01
x1=radians(x1)
x2=radians(x2)
y1=radians(y1)
y2=radians(y2)
d=r*acos(sin(x1)*sin(x2)+cos(x1)*cos(x2)*cos(y1-y2))
print(d)
'''

'''
#五角形面积
s=eval(input(">>"))
print(5*pow(s,2)/(4*tan(pi/5)))
'''

'''
#多边形面积
n=eval(input(">>"))
s=eval(input(">>"))
print(n*pow(s,2)/(4*tan(pi/n)))
'''

'''
#找字符
n=eval(input(">>"))
print(chr(n))
'''

'''
#工资表
name=input(">>")
time=eval(input(">>"))
hour_pay=eval(input(">>"))
federal_tax=eval(input(">>"))
state_tax=eval(input(">>"))

pay_rate=hour_pay
gross_pay=hour_pay*10

federal=gross_pay*federal_tax
state=gross_pay*state_tax
total=federal+state
sum=gross_pay-total
print(name,'\n',time,'\n',pay_rate,'\n',gross_pay,'\n',federal,'\n',state,'\n',total,'\n',sum)
'''

'''
#反向数字
s=str(input(">>"))
a=3
for i in range(4):
	print(s[i+a],end='')
	a-=2
print('\n')
'''


#加密文本，并将解密文件保存到本地(不会)

'''
#解一元二次方程
a,b,c=eval(input(">>"))
dert=pow(b,2)-4*a*c
if dert>0:	
	x1=(-1*b+sqrt(dert))/2*a
	x2=(-1*b-sqrt(dert))/2*a
	print(x1,x2)
elif dert==0:
	x1=(-1*b+sqrt(dert))/2*a
	print(x1)
else:
	print("NO")
'''

'''
#学习加法
s1=randint(0,100)
s2=randint(0,100)
print(s1,s2)
n=eval(input(">>"))
if(n==s1+s2):
	print("True")
else:
	print("False")
'''

'''
#找未来数据
day=eval(input(">>"))
step=eval(input(">>"))
flag=(day+step)%7
if(flag==0):
	print("Sunday")
elif(flag==1):
	print("Monday")
elif(flag==2):
	print("Tuesday")
elif(flag==3):
	print("Wednesday")
elif(flag==4):
	print("Thursday")
elif(flag==5):
	print("Friday")
else:
	print("Saturday")
'''

'''
#排序
li = list(map(int,input(">>").split()))
li.sort()
print(li)
'''

'''
#比较价钱
p1,w1=eval(input(">>"))
p2,w2=eval(input(">>"))
if(p1>p2):
	print("p2")
else:
	print("p1")
'''

'''
#判断天数
m,y=eval(input(">>"))
if(m==2):
	if((y%4==0&y%100!=0)|y%400==0):
		print(29)
	else:
		print(28)
else:
	if(m==4|m==6|m==9|m==11):
		print(30)
	else:
		print(31)
'''

'''
#猜硬币
s=eval(input("on/down(1/0)>>"))
f=randint(0,1)
if(s==f):
	print("True")
else:
	print("Fales")
'''

'''
#猜拳
p=eval(input("石头,剪刀,布(0,1,2)>>"))
ai=randint(0,2)
print(ai,p," ",end='')
if((p==0&ai==1)|(p==1&ai==2)|(p==2&ai==1)):
	print("win")
elif(p==ai):
	print("draw")
else:
	print("lose")
'''

'''
#抽牌
porks=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
color=["Heart","Spade","Diamond","Club"]
print(choice(color),choice(porks))
'''

'''
#回文数
n=eval(input(">>"))
if((n//100)==(n%10)):
	print("YSE")
else:
	print("NO")
'''

#计算三角形周长
q,w,e=eval(input(">>"))
if((q+w<=e)|(q+e<=w)|(w+e<=q)):
	print("Error")
else:
	print(q+w+e)



