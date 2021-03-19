#一张纸的厚度大约是 0.08mm，对折多少次之后能达到珠穆朗玛峰的高度（8848.13 米）？
#请用 循环 完成这个练习，并打印出 需要对折n次，n 是纸的厚度大于等于 8848.13 米时已经对折的次数。


mount = 100
paper = 20 
count = 0
while paper < mount:
  paper *= 2
  count +=1
  

print('需要对折' + str(count) + '次')


#  *=    先乘再赋值
#  paper=paper*2
#
#  +=     先加再赋值
#