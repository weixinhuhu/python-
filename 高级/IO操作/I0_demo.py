import  os
print(os.uname())
print(os.environ)

# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
# /Users/weixin/工作/python_work/高级/IO操作

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('/Users/weixin/工作/python_work/高级/IO操作', 'testdir')

# 分拆路径
print(os.path.split('/Users/michael/testdir/file.txt'))

# 然后创建一个目录:
os.mkdir('/Users/weixin/工作/python_work/高级/IO操作/testdir')

# 删掉一个目录:
os.rmdir('/Users/weixin/工作/python_work/高级/IO操作/testdir')

# 分拆路径
os.path.split('/Users/michael/testdir/file.txt')

# 利用Python的特性来过滤文件
print([x for x in os.listdir('.') if os.path.isdir(x)])


from datetime import datetime
import os

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))