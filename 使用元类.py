#!/usr/bin/python
#coding:utf-8
'''class Hello():
    def hello(self,name='world'):
        print('helo,%s'% name)

h=Hello()
print(h.hello())
print(type(Hello))
print(type(h))'''
'''type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。

我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。'''
'''type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：'''
def fn(self,name='world'):
    print('hello,%s'%name)

Hello2=type('Hello',(object,),dict(hello2=fn))
'''要创建一个class对象，type()函数依次传入3个参数：
1.class的名称； 'Hello'  
2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法； (object,)  
3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。  dict(hello2=fn) '''
h=Hello2()
print(h.hello2())
'''通过type()函数创建的类和直接写class是完全一样的因为Python解释器遇到class定义时，
仅仅是扫描一下class定    义的      语法，然后调用type()函数创建出class。'''

snijsdisdhiab