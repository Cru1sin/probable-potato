import numpy
f=open("word.txt", "rt")
shuju=f.readlines()
shuju = list(map(str,shuju[0].split()))
set_all = []
dic_all = {}
for i in shuju:
    dic = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0,'-':0}
    set_1 = set(i)
    for k in set_1:
        dic[k]+=1
    renda = list(dic.values())
    set_all.appned.renda
    dic_all[renda] = i
for i in set_all:
    m = set_all.index(i)
    for k in set_all[m:]:
        x=np.array(i)
        y=np.array(k)
        # 分别计算两个向量的模：
        l_x=np.sqrt(x.dot(x))
        l_y=np.sqrt(y.dot(y))
        # 计算两个向量的点积
        dian=x.dot(y)
        # 计算夹角的cos值：
        cos_=dian/(l_x*l_y)
        # 求得夹角（弧度制）：
        angle_hu=np.arccos(cos_)
        # 转换为角度值：
        angle_d=angle_hu*180/np.pi
        if angle_d <= 10:
            set_all.remove(k)
print_simple = []
mylog = open('simple.txt', mode = 'a',encoding='utf-8')
for i in set_all:
    print_simple.append(dic[i])
print(*print_simple,end='',file=mylog) #输入到文件
mylog.close()