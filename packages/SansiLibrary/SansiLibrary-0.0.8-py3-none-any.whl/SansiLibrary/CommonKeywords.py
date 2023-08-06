# -*- coding: utf-8 -*-
# @Author: yongfanmao
# @email: maoyongfan@163.com
# @Date:   2022-11-28 16:11:35
# @Last Modified by:   yongfanmao
# @Last Modified time: 2022-12-06 15:51:24
import os
import datetime

from robot.api import logger
from robot.api.deco import keyword

class CommonKeywords(object):

	@keyword("Get Time Format")
	def get_time_format(self,formatStyle="%Y-%m-%d %H:%M:%S"):
		'''
		得到当前格式化时间
		'''
		return datetime.datetime.now().strftime(formatStyle)

	@keyword("Is Empty")
	def isEmpty(self,ob):
		if ob:
			return False
		else:
			return True

	@keyword("Is Equals")
	def isEquals(self,inputValue,outputValue):
		if inputValue == outputValue:
			return True
		else:
			return False

if __name__ == '__main__':
	ck = CommonKeywords()
	print(ck.get_time_format())




		