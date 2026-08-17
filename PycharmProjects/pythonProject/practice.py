#编写一个程序，找到2000到3200（包括在内）中所有可被7整除但不能被5整除的所有数字，得到的数字按逗号隔开，打印在一行上
l = []
for i in range(2000,3201):
    if (i%7 ==0)and(i%5!=0):
        l.append(str(i))
print(','.join(l))
#编写一个可以计算给定数阶乘的程序，结果以逗号分隔，打印在一行上；
def fact(x):
    if x == 0:
        return 1
    return x* fact(x-1)
print("请输入一个数字")
x=int(input())
print(fact(x))
#使用给定的整数n，编写程序生成一个包含（i,ixi)字典，该字典包含从1到n之间的整数（两者都包含），然后打印字典，假设向程序提供以下输入：8 则输出为：{1:1.2:4.3:9.4:16.5:25}
#dic = {x:x*x for x in range(i,n=1)}
print('请输入一个数字')
n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i
print(d)
# 基础播放量为20.7万，每月增加播放量50万请输出未来两个月的播放量
i = 20.7
j = 50
print('第一个月的播放量：',i+j,'第二个月的播放量：',i+j*2)