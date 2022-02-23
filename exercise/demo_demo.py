import os,re,sys
# def wenjian(file):
#     if os.path.isfile(file):
#        os.system(file)
#
#     elif os.path.isdir(file):
#         ls=os.listdir(file)
#         for i in ls:
#             os.system(i)
# file='D:\project\exercise\demo_demo.py'
# print(wenjian(file))
# def func(path):
#     # 先判断这个path是文件还是文件夹,isdir isfile
#     # 如果是文件,.py结尾的
#     if os.path.isfile(path) and path.endswith('.py'):
#         # 执行这个文件 :
#         os.system('python %s'%path)  # 模拟了在cmd中执行代码的过程
#     # 如果是文件夹
#     elif os.path.isdir(path):
#         # 查看这个文件夹下的所有内容  listdir
#         for name in os.listdir(path):
#             abs_path = os.path.join(path,name)
#             # 如果是文件 .py结尾的
#             if abs_path.endswith('.py'):
#                 # 执行这个文件 : os.system('python %s'%abs_path)
#                 os.system('python %s' % abs_path)
# path='D:\project\work\work.py'
# func(path)
# print(sys.path)
# print(sys.argv[0])
#

# with open('outfile.log',"a+",encoding='utf-8')as f:
#     sys.stdout=f
#     aug_path = sys.argv[1]
#     pythonpath = sys.path
#     pythonpath.append(aug_path)
#     try:
#         for name in os.listdir(aug_path):
#             abs_path = os.path.join(aug_path,name)
#             if abs_path.endswith('.py'):
#                 print(os.system(f'python {abs_path}'))
#             else:
#                 print("没有py")
#     except FileNotFoundError:
#             print("没有这个目录文件")
#             sys.exit()
# import subprocess,os
#
# # a=subprocess.call('ping softwaretesting.tech', shell=True)
# # # print(a)
# print(os.system('ping softwaretesting.tech'))
# os.system(command='notepad')
# import xlwt
# from pandas import DataFrame
# data={'name':[1,1,1,2],'vale':[5,6,7,8]}
# df=DataFrame(data)
# df.to_excel('fi.xls')
# def func(s,i,j):
#     if i<j:
#         func(s,i+1,j-1)
#         s[i],s[j]=s[j],s[i]
# def main():
#     a=[10,6,23,-90,0,3]
#     func(a,0,len(a)-1)
#     for i in range(6):
#         print(a[i])
#         print('\n')
# main()
# # 3 6 23 -90 0 10
# # 3 0 23 -90 6 10
# # 3 0 -90 23 6 10
# def adder(x):
#     def wrapper(y):
#         return  x+y
#     return wrapper
# a=adder(5)
# print(a(a(6)))
# func=lambda x :x%2
# res=filter(func,[1,2,3,4,5])
# print(list(res))
#
# a=[1,2,3,4]
# print(list(filter(lambda  x:x%2==0,a)))
# a=(1,(2,3))
# b,c,d=a
# print(b,c,d)
# def outer(fn):
#     print('outer')
#     def inner():
#         print('inner')
#         return fn
#     return inner
# @outer
# def fusssn():
#     print('fun')



import pymysql

# # 打开数据库连接
# db = pymysql.connect(host='121.4.36.2',#服务器号
#                      user='root',#用户名
#                      password='123456',#密码
#                      database='wang',#数据库
#                      port=3388)#端口
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("select * from testdata;")
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
# print(data)
# # # print("Database version : %s " % data)
# # # 获取所有记录列表
# results = cursor.fetchall()
# for row in results:
#   fname = row[0]
#   lname = row[1]
# #   # age = row[2]
# #   # sex = row[3]
# #   # income = row[4]
# #    # 打印结果
#   print ("payload=%s,respnose=%s" % (fname, lname))
# # # 关闭数据库连接
# db.close()

def sort_num(num,type):
    x=0
    y=0
    while(num):
        if type==0:
            x=y+2
        elif(type==1):
            x=y+10
        else:
           x=y+20
        num=num-1
    return x















