# -*- coding: utf-8 -*-
# @Author: yongfanmao
# @email: maoyongfan@163.com
# @Date:   2022-11-28 16:02:10
# @Last Modified by:   yongfanmao
# @Last Modified time: 2022-12-05 17:21:54
from SansiLibrary.CommonKeywords import CommonKeywords
from SansiLibrary.StarRiverKeywords import StarRiverKeywords
from SansiLibrary.version import VERSION

class SansiLibrary(CommonKeywords, StarRiverKeywords):
	"""
	"""
	ROBOT_LIBRARY_SCOPE = "GLOBAL"
	__version__ = VERSION
