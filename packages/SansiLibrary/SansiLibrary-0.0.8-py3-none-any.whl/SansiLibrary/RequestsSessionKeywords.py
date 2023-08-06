# -*- coding: utf-8 -*-
# @Author: yongfanmao
# @email: maoyongfan@163.com
# @Date:   2022-12-05 10:45:20
# @Last Modified by:   yongfanmao
# @Last Modified time: 2023-01-18 16:43:33

import os
import datetime
import requests

from robot.api import logger
from robot.api.deco import keyword

class RequestsSessionKeywords(object):

	def __init__(self,**kwargs):

		defaultUrl = ""
		defaultCookies = {}

		kwargsKeys = kwargs.keys()

		self.session = requests.Session()

		if "url" not in kwargsKeys:
			self.session.url = defaultUrl

		if "cookies" not in kwargsKeys:
			self.session.cookies.update(defaultCookies)	
		
		if 'url' in kwargsKeys:
			url = kwargs["url"] if kwargs["url"] else defaultUrl
			self.session.url = url

		if "cookies" in kwargsKeys:
			cookies = kwargs["cookies"] if kwargs["cookies"] else defaultCookies
			self.session.cookies.update(cookies)

		if "headers" in kwargsKeys:
			headers = kwargs["headers"] if kwargs["headers"] else defaultCookies
			self.session.headers.update(headers)

		if "params" in kwargsKeys:
			params = kwargs["params"] if kwargs["params"] else defaultDict
			self.session.params.update(params)

	def session_get(self,uri,**kwargs):
		url = self.session.url + uri
		return self.session.get(url,**kwargs)

	def session_post(self,uri,data=None,json=None,**kwargs):
		url = self.session.url  + uri
		if data is not None or (data is None and json is None):
			return self.session.post(url,data=data,**kwargs)
		elif json is not None:
			return self.session.post(url,json=json,**kwargs)
		else:
			return self.session.post(url,data=data,**kwargs)



	def __del__(self):
		self.session.close()


if __name__ == '__main__':
	rs  = RequestsSessionKeywords()
	res = rs.session_get("/api/media/players/637b04fb6ea4b90018943fe3/snapshot")
	print(res)
	print(dir(res))
	print(res.status_code)

