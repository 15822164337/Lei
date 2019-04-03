"""
信息管理系统：添加学生，查找学生，修改学生，删除学生
"""
from Security import*
from Security_Test.py import security

security()


stu_info=[]
while True:
    print("""
    **************************学生管理系统*********************
                            1. 添加学生
                            2. 查找学生
                            3. 修改学生
                            4. 删除学生
                            5. 退出系统
    ***********************************************************
    """)
    a = input("请输入选项（1-5）： ")
    if a == '5':
        break


    elif a == '1':
        while True:
            print ("*******************添加学生*****************")
            name = input("学生姓名： ")
            num = input("学生学号： ")
            sex = input("学生性别： ")
            hobby = input("学生爱好： ")
            tel = input("学生电话： ")
            stu = {}                    #字典必须放在里面
            stu['姓名'] =name
            stu['学号'] =num
            stu['性别'] =sex
            stu['爱好'] =hobby
            stu['电话'] =tel
            stu_info.append(stu)
            print ("\n添加成功！显示信息：")
            for i in stu_info:
                print (i)
            ch = input("\n是否继续添加？(N/Y) >>>")
            if ch =='Y'or ch =='y':
                continue
            elif ch =='N'or ch =='n':
                break



    elif a == '2':
        while True:
            print ("""
            *******************查找学生*****************
                            1. 按姓名查找
                            2. 按学号查找
            """)
            num=input("请输入序号（1-2）： ")
            if num =='1':
                name=input("请输入姓名： ")
                for i in stu_info:
                    if name in i.values():
                        print (i)
                        continue
                    else:
                        print ("没有此人！")
            elif  num =='2':
                num = input("请输入学号： ")
                for i in stu_info:
                    if num in i.values():
                        print (i)
                        continue
                    else:
                        print ("没有此人！")
            ch =input("继续查找？（Y/N）>>> ")
            if ch =='Y' or ch =='y':
                continue
            elif  ch =='N' or ch =='n':
                break



    elif a == '3':
        while True:
            print ("""
            ****************************修改学生*************************""")
            count=0
            for i in stu_info:
                print (str(count)+'. ')
                print (i)
                count=count+1
            n=input("请输入要修改的学生编号(0-%d)： "%(count-1))
            name = input("姓名： ")
            num = input("学号： ")
            sex = input("性别： ")
            hobby = input("爱好： ")
            tel = input("电话： ")
            stu_info[int(n)]['姓名'] = name
            stu_info[int(n)]['学号'] = num
            stu_info[int(n)]['性别'] = sex
            stu_info[int(n)]['爱好'] = hobby
            stu_info[int(n)]['电话'] = tel
            print ("修改完成！")
            print (stu_info[int(n)])

            a=input("是否继续修改？(Y/N)>>>")
            if a=='Y' or a=='y':
                continue
            elif a=='N' or a=='n':
                break



    elif a == '4':
        while True:
            print ("""
            ********************************删除学生***************************
            """)
            count=0
            for i in stu_info:
                print (str(count)+'. ')
                print (i)
                count=count+1
            n=input('请输入要删除的学生序号(0-%d)：'%(count-1))
            del(stu_info[int(n)])
            print ("\n删除成功！ 显示信息：\n")
            for i in stu_info:
                print (i)

            a=input("是否继续删除？（Y/N）")
            if a == 'Y' or a == 'y':
                continue
            elif a == 'N' or a == 'n':
                break



