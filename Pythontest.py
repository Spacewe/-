#-*-coding:utf-8-*-
import re
import pickle
import os 
def illustration():
    illustration="""
    创建表语法格式：
        CREATE TABLE <表名>（<列名> <数据类型>[ <列级完整性约束条件> ]
        [,<列名> <数据类型>[ <列级完整性约束条件>] ] … 
        [,<表级完整性约束条件> ] ）
         ;
    修改表语法格式：
        ALTER TABLE <表名>
        [ ADD <新列名> <数据类型> [ 完整性约束 ] ]
        [ DROP <完整性约束名> ]
        [ ALTER COLUMN<列名> <数据类型> ]
        [ADD [COLUMN<约束名> ] <约束定义> ]
        ;
       ******
        Author：宋培城
       ******
    ***WARNING : 最后需要【单独另起一行并以分号；结尾】，【并按回车】 表示结束***
    ***WARNING : 以程序方式执行请确保每条SQL语句为一行***
    ***WARNING : 以程序方式执行现在只能读取.txt文件，请直接输入文件名，并按回车执行***
    ***WARNING : 以程序方式执行请确保可执行文件在当前目录下***
    """
    print('*'*100)
    print(illustration)
    print('*'*100)
    print("请选择使用Sql命令(A)或导入可执行文件(B)：")

##########################判断执行方式 1 ：命令    2： 可执行文件

#。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。

##########################以命令方式执行

#定义一个类 用来创建表
class Table(object):
    #name=''
    #dictelist={}   #包含属性名和列表（列表中为属性值）
    #dictacon = {}  #包含属性名和列级约束条件
    #key={}         #实体完整性 主码 和 unique
    #oukey={}       #参照完整性 外码
    def __init__(self,name):
        self.name = name
        #self.dictelist = dicte 
        self.key = {}
        self.key["key"]=[]
        self.key["unique"]=[]               #初始化为字典，方便后面操作
        self.dictacon = {}                  #包含属性名和列级约束条件
        self.dictelist = {}                 #包含属性名和列表（列表中为属性值）
        self.oukey = {}                     #参照完整性 外码
    def attribute(self,everyattr,acon):   #创建两个字典 一个字典中包含属性名和约束条件；一个字典中包含属性名和一个列表，列表中为属性值
        self.dictelist[everyattr] = []
        self.dictacon[everyattr] = acon      #包含属性名和列级约束条件
        #print("--------------------attribute finished--------------------")
    def setkey(self,keyy):        #设置主码
        #判断输入的主码是否是该关系的属性
        if isinstance(keyy,list):
            for e in keyy:
                if e in self.dictacon:
                    pass
                else:
                    Error(1)
           
            self.key["key"] = keyy                 #----------------keyy是个列表-----------------# 
        elif isinstance(keyy,str):
            key_list = key["key"]
            #list_len =len(key_list)
            for e in key_list:
                if keyy == e:
                    print(keyy,"is already exists as PRIMARY KEY")
                    return
                else:
                    pass 
            key_list.append(keyy)
            self.key["key"] = key_list
        #print("----------------setkey finished--------------------------")
    def setunique(self,uniquelist):
        un_list = key["unique"]
        if len(un_list) == 0:
            list_qu=[]
            list_qu.append(uniquelist)
            self.key["unique"] = list_qu
        else:
            for r in un_list:
                if uniquelist == r:
                    print(uniquelist," already is Unique")
                    return
                else:
                    pass
            un_list.append(uniquelist)
            self.key["unique"] = un_list      #uniquelist 是个列表  因为唯一的可能不止一个属性  但是输入不是一个列表 是字符串
    def setoukey(self,oukk,tablekey):   #设置外码
        #判断输入的外码是否是该关系的属性
        if oukk in self.dictacon:          #使用in判断输入的外码是否是该关系的属性
            self.oukey[oukk] = tablekey    #tablekey 是参照表 是个字符串
        else:
            Error(1)
        #print("外码：",self.oukey)
    def showtable(self):
        print("建表成功！表的信息如下：")
        print("   表名       :",self.name)
        print("\n")
        print("   |%-9s |%-9s |"%("属性","类型"))
        print("   |%-9s   |%-9s   |"%("---------","---------"))
        for key,value in self.dictacon.items():        #遍历字典
            print("   |%-9s   |%-9s   |" % (key,value))
        #print("------------------------")
        print("\n")
        #print("实体完整性  :",self.key)
        for kkey,uni in self.key.items():
            if kkey =="key":
                print("   %-9s :" % "主码",end='')
                for ee in uni:
                    print("   %-6s"% ee,end='')
                print("")
            else:
                print("   %-9s   :" % "UNIQUE",end='')
                for ee in uni:
                    print("   %-6s"% ee,end='')
                print("")

        print("\n")
        #print("参照完整性  :",self.oukey)
        print("   |%-10s |%-10s  |"%("外码","参照表"))
        print("   |%-10s   |%-10s     |"%("----------","----------"))
        for key,value in self.oukey.items():        #遍历字典
            print("   |%-10s   |%-10s    |" % (key,value))
        #print("\n")


        




#获取输入
def getInput():
    sentinel = ';' # 遇到这个就结束   但是列表中没有该符号
    lines = []
    for line in iter(input, sentinel):
        lines.append(line)
    #print("获取输入为：",lines)     #输入为列表格式  可以任意行数输入，只要将列表合成一个字符串就行了
    return lines

#将列表合成一个字符串,上面获取的列表中sql语句可能为一句或者是多行，需要把列表中的每个字符串拼接起来
# print(','.join(lines)) #使用该方法会有两个逗号
def hecheng(list):
    n=0
    str1=''
    while n < len(list):
        str1 += list[n]
        n += 1
    #print("合成字符串为：",str1)
    return str1
#print(str1.split(' '))
#检查输入  只有创建和修改两种操作 
#CREATE TABLE SC(Sno CHAR(9), Cno CHAR(4), Grade SMALLINT,PRIMARY KEY (Sno,Cno), )
#先判断CREATE TABLE SC是否正确，如果正确，判断其后的括号中的是否正确，有两种情况：1.属性加列级约束 2.表级约束
#判断是创建表还是修改表

def Error(num):            #错误提示函数
    if num >0:
        print("Word Input Error! Please Check Input")
        return 
    elif num ==0:
        print("格式错误！")
        return 
    else:
        print("Unknown error!")
        return 
    

def judgeFirst(string):
    #print(string)
    #for e in string:   #扫描字符串 一个字符一个字符的扫
    #    print(e)
    slist=string.split(" ")
    if slist[0]=="CREATE":
        if slist[1]=="TABLE": # 判断是不是创建表 如果是的话，取得要创建表的名称（用正则）
            #print("输入为创建表，开始创建：")
            numk=0               ######检查括号是否匹配######
            for e in string:
                if e=="(":
                    numk+=1
                elif e==")":
                    numk=numk-1
                else:
                    pass 
            if numk == 0:
                getAttribute(string) #------------------------------------------------获得相关属性创建表----------------------#
            else:
                Error(0)

            
        else:
            Error(1)
    elif slist[0]=="ALTER":
        if slist[1]=="TABLE":
            #print("OK")

            numk=0               ######检查括号是否匹配######
            for e in string:
                if e=="(":
                    numk+=1
                elif e==")":
                    numk=numk-1
                else:
                    pass 
            if numk == 0:
                getAlter(string)                ################此处是修改表######################
            else:
                Error(0)

        else:
            Error(1)
    else:
        Error(0)
#检查语法

#获取表名，属性名，约束条件
#CREATE TABLE SC(Sno CHAR(9), Cno CHAR(4), Grade SMALLINT,PRIMARY KEY (Sno,Cno) )      # 在输入的时候用列级约束条件判断是否符合条件
def getAttribute(string1):
    #judgeFirst(string)
    str1 =string1

    #print("【创建】开始分析字符串：",str1)
    #----------------表名----------------#
    tablename = re.findall(r"CREATE TABLE (.*?)\(",str1) #那个左括号前要加反斜杠
    #表名不能有空格
    for k in tablename[0]:
        if k==" ":
            print("error!")
            return        #表名有空格则产生错误
    print("表名获取完成:",tablename[0])

    table=Table(tablename[0])         #------------------创建表初始化----------------#
    #---------------属性及约束条件----------------#
    strtem = str1+";"
    #print("////////////",strtem)
    xxx = strtem.strip()
    attr = re.findall(r"CREATE TABLE.*?\((.*?)\);",xxx,re.S)       #-----------获得了所有属性和约束------------#
    #print(attr)
    #print("所有属性获取完成：",attr)
    #-----------------把每一句提取出来-------------------#
    kuocheck=0     #检查逗号是否在括号内
    strattr=attr[0]
    #print(type(strattr))   # str
    locate=0
    numlo=0     #用来标记字符串遍历到那个位置
    fiattr=''  #用来保存替换过的字符串
    flag = 1      #判断是否是第一次替换 
    for e in strattr:
        #print(e),
        if e == "(":
            kuocheck+=1
            #print("kuocheck=",kuocheck)
        elif e == ")":
            kuocheck=kuocheck-1
            #print("kuocheckvvvv=",kuocheck)
        elif e ==",":
            if kuocheck==0 and flag==1:
                #print("kuocheckkkkkkkkkkk=",kuocheck)
                fiattr = strattr[:numlo]+";"+strattr[numlo+1:]    #使用切片把逗号去掉 安全可控
                #fiattr = strattr.replace(strattr[numlo],';',1)   #把每句间的逗号换成分号用以区别属性约束内的逗号
                flag=0
            elif kuocheck==0 and flag==0:
                fiattr = fiattr[:numlo]+";"+fiattr[numlo+1:]
                #fiattr = fiattr.replace(fiattr[numlo],';',1)   # replace会按顺序把每个符合条件的都换掉不符合要求
                #print("numlo:",numlo)
                #print("kuochecooooooooooo=",kuocheck)
            else:
                pass 
        else:
            pass 
        numlo+=1
    attrlist = fiattr.split(";")  #把每个属性及约束都拿出来放到列表里面去
    #print("属性分解完成：",attrlist)
    for jj in attrlist:
        #print("jj:",jj)
        delblank = jj.strip()   # 去掉每一句左右的空格
        aatt=delblank.split(" ")
        #print(aatt)
        if aatt[0]=="PRIMARY":
            keyy = [] #用来存主码 传参数
            frikey = re.findall(r".*?\((.*?)\).*?",delblank,re.S) #获取存主码的列表
            frikey_string = frikey[0]
            frikey_list = frikey_string.split(",")
            #print("主码获取完成")
            table.setkey(frikey_list)             #--------------------设置主码-----------------------#
            #print("设置主码完成")
        elif aatt[0]=="FOREIGN":
            #print("delbalnk",delblank)
            
            otkey = re.findall(r"FOREIGN.*?\((.*?)\).*?",delblank,re.S)
            otkey_string = otkey[0]   # 外码
            delblank_FOR = delblank+";"            #为了能匹配出来最后的参照表
            otkey_table = re.findall(r"REFERENCES(.*?);",delblank_FOR,re.S)
            otkey_table_string = otkey_table[0].strip()
            table.setoukey(otkey_string,otkey_table_string)
            #print("设置外码完成")
        else:
            if "PRIMARY" in aatt:          #对应另一种格式 即如果【Sno CHAR(9) PRIMARY KEY】
                table.setkey(aatt[0])
            elif "UNIQUE" in aatt:
                table.setunique(aatt[0])
            else:
                table.attribute(aatt[0],aatt[1])
    
    #print(type(table.name))
    #---------------------------------把表存起来------------------------------------------#
    current_pathc = os.getcwd()    # 获得当前路径
    #print("创建路径-----------：",current_pathc)
    if os.path.exists(os.path.join(current_pathc,"database")):    #创建保存表的文件夹
        db_path = os.path.join(current_pathc,"database")
        os.chdir(db_path)
        #print("当前路径：",os.getcwd())
        file_path = os.path.join(db_path,table.name+".txt")

        if os.path.isfile(file_path):
            print("【 表已经存在！请更换表名或删除原有文件】\n原有文件路径为 %s" % file_path)
            os.chdir(current_pathc)
            return 
        else:
            ouk_dict = table.oukey
            for key,value in ouk_dict.items():
                fff_table = re.findall(r"(.*?)\(",value,re.S)    #被参照表
                #print("fff_table",fff_table[0])
                for_path=os.path.join(db_path,fff_table[0]+".txt")
                if os.path.isfile(for_path):
                    pass
                else:
                    print("被参照表 %s 不存在！" % fff_table[0])
                    os.chdir(current_pathc)
                    return
            
            f = open(table.name+".txt","wb")  # 把当前的表存起来
            pickle.dump(table,f,True)
            #print("表存储完成！")
            f.close()
            print("*"*66)
            table.showtable()
            print("*"*66)
            #f1= open(table.name+".txt","rb")      #还能再拿出来用 
            #tt = pickle.load(f1)
            #print("tt:",tt.oukey)
            #print("tt:",type(tt.oukey))
           
            #f1.close()
        os.chdir(current_pathc)
        #return
    else:
        os.mkdir(os.path.join(current_pathc,"database"))
        os.chdir(current_pathc)
        db_path = os.path.join(current_pathc,"database")
        os.chdir(db_path)
        #print("当前路径：",os.getcwd())
        file_path = os.path.join(db_path,table.name+".txt")

        if os.path.isfile(file_path):
            print("【 表已经存在！请更换表名或删除原有文件】\n原有文件路径为 %s" % file_path)
            os.chdir(current_pathc)
            return 
        else:
            ouk_dict = table.oukey
            for key,value in ouk_dict.items():
                fff_table = re.findall(r"(.*?)\(",value,re.S)    #被参照表
                #print("fff_table",fff_table[0])
                for_path=os.path.join(db_path,fff_table[0]+".txt")
                if os.path.isfile(for_path):
                    pass
                else:
                    print("被参照表 %s 不存在！" % fff_table[0])
                    os.chdir(current_pathc)
                    return
            
            f = open(table.name+".txt","wb")  # 把当前的表存起来
            pickle.dump(table,f,True)
            #print("表存储完成！")
            f.close()
            print("*"*66)
            table.showtable()
            print("*"*66)
            #f1= open(table.name+".txt","rb")      #还能再拿出来用 
            #tt = pickle.load(f1)
            #print("tt:",tt.oukey)
            #print("tt:",type(tt.oukey))
           
            #f1.close()
        os.chdir(current_pathc)
        #return
    #print(current_path)
    
#-----------------------------修改表----------------------#
def getAlter(string1):
    strr = string1
     #----------------表名----------------#
    flag = 0
    tablename_add = re.findall(r"ALTER TABLE (.*?)ADD",strr) #那个左括号前要加反斜杠
    tablename_alet = re.findall(r"ALTER TABLE (.*?)ALTER",strr) 
    tablename_drop = re.findall(r"ALTER TABLE (.*?)DROP",strr) 
    if tablename_add != []:
        tablename = tablename_add[0]
        flag = 1
    elif tablename_alet !=[]:
        tablename = tablename_alet[0]
        flag = 2
    elif tablename_drop != []:
        tablename = tablename_drop[0]
        flag = 3
    else:
        flag = 0 
        Error(0)   #表名不能有空格
    for k in tablename:
        if k==" ":
            print("error!")
            return                      #表名有空格则产生错误
    #print("表名:",tablename)
    if flag ==1:            #--------------------------------------------------------------判断是不是ADD操作
        str_tem = strr+";"
        tem_get = re.findall(r".*?ADD(.*?);",str_tem,re.S)
        #print("tem_get",tem_get)
        ss = tem_get[0].strip().split(" ")
        #print("ss",ss)
        if ss[0] != "PRIMARY":            #------------------------------------------------判断是不是添加主码
            current_path = os.getcwd()    # 获得当前路径
            #split_path = os.path.split(current_path)
            #if split_path[1] == "database":
            #    use_path = split_path[0] 
            #else split_path[1]
            #print("ADD当前路径：",current_path)
            if os.path.exists(os.path.join(current_path,"database")):    #创建保存表的文件夹
                db_path = os.path.join(current_path,"database")
                os.chdir(db_path)
                file_path = os.path.join(db_path,tablename+".txt")
                if os.path.isfile(file_path):
                    f1= open(tablename+".txt","rb")      #还能再拿出来用 
                    tt = pickle.load(f1)
                    f1.close()
                    #print("tt:",tt.oukey)
                    #print("tt:",type(tt.oukey))
                    if ss[0] in tt.dictacon:
                        print("属性已经存在！")
                    else:
                        tt.dictacon[ss[0]] = ss[1]    #添加属性及其约束
                        tt.dictelist[ss[0]] = []    #添加属性及其值
                    ff = open(tablename+".txt","wb")   
                    pickle.dump(tt,ff)
                    ff.close()
                    fg = open(tablename+".txt","rb")             #------------------------------修改后再读出
                    ll = pickle.load(fg)
                    #print("******************",ll.__dict__)
                    print("增加完成！表的信息如下：")
                    showtable(ll)
                    fg.close()
                    
                else:
                    print("表 %s 不存在！无法修改！"% tablename)
                os.chdir(current_path)
                
            else:
                print("不存在数据库！无法修改")
                os.chdir(current_path)
                return
            #print("ss",ss)
        else:
            pass     #-------------------------------------------------------------------------此处应有添加主码的操作
    elif flag ==2:
        str_tem2 = strr+";"
        tem_get2 = re.findall(r".*?COLUMN(.*?);",str_tem2,re.S)
        #print("tem_get2",tem_get2)
        if tem_get2 == []:
            Error(0)
            return 
        else:
            ss2 = tem_get2[0].strip().split(" ")
        
        #print("ss2",ss2)
        if ss2 == '':
            Error(0)
        if ss2[0] != "PRIMARY":            #------------------------------------------------判断是不是添加主码
            current_path2 = os.getcwd()    # 获得当前路径
            if os.path.exists(os.path.join(current_path2,"database")):    #创建保存表的文件夹
                db_path2 = os.path.join(current_path2,"database")
                os.chdir(db_path2)
                file_path2 = os.path.join(db_path2,tablename+".txt")
                if os.path.isfile(file_path2):
                    f12= open(tablename+".txt","rb")      #还能再拿出来用 
                    tt2 = pickle.load(f12)
                    f12.close()
                    #print("tt:",tt2.oukey)
                    #print("tt:",type(tt2.oukey))
                    if ss2[0] in tt2.dictacon:
                        if ss2[1] == tt2.dictacon[ss2[0]]:    #--------------------------如果已经是要设置的类型，则不需要修改
                            print("属性 %s 的类型已经是 %s 不需要修改！"%(ss2[0],ss2[1]))
                            os.chdir(current_path2)
                            return 
                        else:
                            tt2.dictacon[ss2[0]] = ss2[1]     #修改属性的约束
                    else:
                        print("不存在 %s ,无法修改！"% ss2[0])
                    ff2 = open(tablename+".txt","wb")   
                    pickle.dump(tt2,ff2)
                    ff2.close()
                    fg2 = open(tablename+".txt","rb")             #------------------------------修改后再读出
                    ll2 = pickle.load(fg2)
                    #print("*****lllllllllllll********",ll2.__dict__)
                    print("修改完成！表的信息如下：")
                    showtable(ll2)
                    fg2.close()
                    
                else:
                    print("表 %s 不存在！无法修改！"% tablename)
                os.chdir(current_path2)
            else:
                print("不存在数据库！无法修改")
                os.chdir(current_path2)
                return
            #print("ss2",ss2)
        else:
            pass 
    elif flag == 3:
        str_tem3 = strr+";"
        tem_get3 = re.findall(r".*?COLUMN(.*?);",str_tem3,re.S)
        
        #print("tem_get3",tem_get3)
        ss3 = tem_get3[0].strip().split(" ")
        #print("ss3",ss3)
        if ss3 == '':
            Error(0)
        else:
            pass
        if ss3[0] != "PRIMARY":            #------------------------------------------------判断是不是添加主码
            current_path3 = os.getcwd()    # 获得当前路径
            if os.path.exists(os.path.join(current_path3,"database")):    #创建保存表的文件夹
                db_path3 = os.path.join(current_path3,"database")
                os.chdir(db_path3)
                file_path3 = os.path.join(db_path3,tablename+".txt")
                if os.path.isfile(file_path3):
                    f13= open(tablename+".txt","rb")      #还能再拿出来用 
                    tt3 = pickle.load(f13)
                    f13.close()
                    #print("tt3:",tt3.oukey)
                    #print("tt3:",type(tt3.oukey))
                    if ss3[0] in tt3.dictacon:
                        tt3.dictacon.pop(ss3[0])
                        tt3.dictelist.pop(ss3[0])
                        if ss3[0] in tt3.oukey:
                            tt3.oukey.pop(ss3[0])             #----------------------------如果他是个外码也要删
                        else:
                            pass 
                        key_ll=tt3.key["key"]
                        for e in key_ll:
                            if e == ss3[0]:
                                tem_ll = key_ll.remove(ss3[0])
                                tt3.key["key"] = tem_ll
                                print("%s是主码，已删除！"%ss3[0])   #------------------如果他是主码也会删
                            else:
                                print("%s不是主码，不操作！"%ss3[0])
                        uni_ll = tt3.key["unique"]
                        for e in uni_ll:
                            if e == ss3[0]:
                                tt_ll = uni_ll.remove(ss3[0])
                                tt3.key["unique"] = tt_ll
                            else:
                                pass

                    else:
                        print("不存在 %s ,无法删除！"% ss3[0])
                    ff3 = open(tablename+".txt","wb")   
                    pickle.dump(tt3,ff3)
                    ff3.close()
                    fg3 = open(tablename+".txt","rb")             #------------------------------修改后再读出
                    ll3 = pickle.load(fg3)
                    #print("*****lllllllllllll********",ll3.__dict__)
                    print("删除完成！表的信息如下：")
                    showtable(ll3)
                    fg3.close()
                    
                else:
                    print("表 %s 不存在！无法修改！"% tablename)
                os.chdir(current_path3)
            else:
                print("不存在数据库！无法修改")
                os.chdir(current_path3)
                return
            #print("ss3",ss3)
        else:
            pass 
    
    #------------用不着检查拼写错误了-----------------#
        #atttemp = aatt[0]
        #if atttemp[:3] == "PRI":
        #    if atttemp =="PRIMARY":
        #        pass
        #    else:
        #        Error(1)   # 单词拼写错误
        #elif atttemp[:5]== "FOREI":
        #    if atttemp=="FOREIGN":
        #        pass
        #    else:
        #        Error(1)   # 单词拼写错误
        #else:
        #    pass

#创建二维表
#
#。。。。。。。。。。。。。。。。。


#显示结果       
def showtable(table_true):
        print("   表名       :",table_true.name)
        print("\n")
        print("   |%-9s |%-9s |"%("属性","类型"))
        print("   |%-9s   |%-9s   |"%("---------","---------"))
        for keyt,valuet in table_true.dictacon.items():        #遍历字典
            print("   |%-9s   |%-9s   |" % (keyt,valuet))
        #print("------------------------")
        print("\n")
        #print("实体完整性  :",self.key)
        for kkeyt,unit in table_true.key.items():
            if kkeyt =="key":
                print("   %-9s :" % "主码",end='')
                for eet in unit:
                    print("   %-6s"% eet,end='')
                print("")
            else:
                print("   %-9s   :" % "UNIQUE",end='')
                for eet in unit:
                    print("   %-6s"% eet,end='')
                print("")

        print("\n")
        #print("参照完整性  :",self.oukey)
        print("   |%-10s |%-10s  |"%("外码","参照表"))
        print("   |%-10s   |%-10s     |"%("----------","----------"))
        for keyt,valuet in table_true.oukey.items():        #遍历字典
            print("   |%-10s   |%-10s    |" % (keyt,valuet))
        #print("\n")

###########################以程序方式执行
#读取程序文件
def getfile(string_file):
    
    #print(string_file)   #要执行的文件名
    file_name_h = string_file
    current_pathf = os.getcwd()    # 获得当前路径
    filename_path = os.path.join(current_pathf,file_name_h)  #可执行文件
    if os.path.isfile(filename_path):
        file_f = open(file_name_h)
        while 1:
            line = file_f.readline()
            if not line:
                break
            #print(line)
            line_pass = line.strip('\n')
            judgeFirst(line_pass)
            print("语句执行完成！")
            #print(type(line))
    else:
        os.chdir(current_pathf)
        print("可执行文件不存在！无法继续操作")
if __name__=='__main__':
    str111="CREATE TABLE SC(Sno CHAR(9), Cno CHAR(4), Grade SMALLINT,PRIMARY KEY (Sno,Cno),FOREIGN KEY (Cno) REFERENCES Course(Cno))"
    str_alter = "ALTER TABLE StudentADD S_entrance DATE;"
    str_alter2 = "ALTER TABLE SCADD S_entrance DATE;"
    str_alter22 = "ALTER TABLE SCALTER COLUMN S_entrance SMALLINT;"
    str_alter1 = "ALTER TABLE StudentALTER S_entrance DATE;"
    str_alter11 = "ALTER TABLE StudentDROP COLUMN S_entrance ;"
    str_alter111 = "ALTER TABLE SCDROP COLUMN S_entrance ;"
    illustration()  #显示界面
    while(True):
        a = input(u"[A or B]$")
        if a =="A":
            listq = getInput()    #获取输入，一个列表
            stringq = hecheng(listq)        #合成字符串
            judgeFirst(stringq)    #语句判断->获得相关属性->创建二维表
            #getAttribute(string)
        elif a =="B":
            stringf = input("#")   #获取输入，一个列表
            #print("--------",stringf)
            getfile(stringf)
        else:
            print("请选择一种执行方式！")
    
    
    