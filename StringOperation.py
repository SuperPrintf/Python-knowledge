#对string的内置处理函数

str = 'This is a Py program,Hello'#初始化字符串
#使用+将字符串连接
print(str + ' world')
#*会在字符间插入空格
print(*str)
#使用[]来读取字符串中的单独位置
print(str[3])
#使用[:]来对字符串进行切片
print(str[4:11:1])
#len()函数求取字符串长度
print(len(str))
#.upper()方法将字符串以全大写形式赋给左值
print(str.upper())
#.lower()方法将字符串以全小写形式赋给左值
print(str.lower())
#.strip()方法去除两边的空格以及指定字符
print(str.strip('This '))
print('qqqqwwawawWqqq'.strip('qw'))#内容区分大小写，且单字符匹配所有可行结果
#.split()按照指定字符分割字符串为队列
strs = str.split(' ')
print(strs)
#.join()连接字符串序列
print(' '.join(strs))#将空格插入并连接目标字符串序列
#.find()方法搜索指定字符串
print(str.find('Py'))#返回找到的第一个目标串的所在位置
print('wertyuikwertyuzxcvgbwdfgbn'.find('w',2))#参数2表征返回检索到的第几个目标
#.replace(old,new[,max])方法替换目标字符串
print(str.replace(' ',' and ',3))#第三个参数表示最大替换数
#in字符串的迭代
print(' ' in str)#返回值(bool)表示该串是否存在于字符