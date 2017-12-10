#!/usr/bin/python
#coding:utf-8
class Rectangle:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def getzhouchang(self):
		return (self.x * self.y) * 2
	def getmianji(self):
		return self.x * self.y

juxing = Rectangle(4,5)
juxing.getmianji()
juxing.getzhouchang()
