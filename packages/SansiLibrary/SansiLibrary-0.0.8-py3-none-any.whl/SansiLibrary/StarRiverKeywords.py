# -*- coding: utf-8 -*-
# @Author: yongfanmao
# @email: maoyongfan@163.com
# @Date:   2022-12-05 13:48:02
# @Last Modified by:   yongfanmao
# @Last Modified time: 2023-01-18 17:34:03
import os
import datetime
import time

from robot.api import logger
from robot.api.deco import keyword
from SansiLibrary.CommonKeywords import CommonKeywords
from SansiLibrary.RequestsSessionKeywords import RequestsSessionKeywords
from SansiLibrary.commonDecorator import savePic,send_notice

class StarRiverKeywords(object):

	@keyword("Take Screenshots During Playback")
	def take_screenshots_during_playback(self,playerName,playerID,programDuration,\
		picType="snapshot",hostUrl = "",cookies={},headers={},path="D:\\runRecord"):
		"""
		必传:
			playerName: 播放器名称
			playerID:  播放器ID
			programDuration:	节目播放时长毫秒
		非必传
			picType:  截图类型
			hostUrl:  截图地址的host
			cookies:  所需cookies
			path:     保存图片的基础路径

		"""
		programDuration  = int(int(programDuration)/1000) + 5

		ck = CommonKeywords()
		dateDir = ck.get_time_format(formatStyle="%Y_%m_%d_%H_%M_%S")
		now =datetime.datetime.now()
		tmp =0
		# for second in range(1,programDuration+1):
		# 	logger.info(second)
		# 	self._snapshot(playerName,playerID,second,picType=picType,\
		# 		hostUrl = hostUrl,cookies=cookies,headers=headers,path=path,dateDir=dateDir)
		# 	time.sleep(1)
		while tmp < programDuration:
			logger.info(tmp)
			self._snapshot(playerName,playerID,tmp,picType=picType,\
				hostUrl = hostUrl,cookies=cookies,headers=headers,path=path,dateDir=dateDir)
			time.sleep(1)
			tmp = self.timeDifference_seconds(now,datetime.datetime.now())
		return True

	@keyword("Send WeChat Msg")
	def send_wechat_msg(self,start_time,end_time,player_id_list_num,\
		programs_num):
		"""
		必传:
			start_time: 测试开始时间
			end_time:  测试结束时间
			player_id_list_num:	在线播放器播放器数量
			programs_num: 播放节目数量
		非必传

		"""
		seconds = self.timeDifference_seconds(start_time,end_time)
		duration = float(seconds/60)
		self._get_msg(duration,player_id_list_num,programs_num)

	@send_notice
	def _get_msg(self,duration,player_id_list_num,programs_num):

		content = "#  自动测试完成通知\n\n<font color=\"info\">一共{player_id_list_num}个在线工程机完成{programs_num}节目播放\n一共耗时{minutes}分钟</font>\n".format(
			player_id_list_num=player_id_list_num,programs_num=programs_num,minutes=duration)

		body_data = {
			"msgtype": "markdown",
			"markdown": {
				"content": content
			}
		}

		
		return "https://qyapi.weixin.qq.com",{"Content-Type":"application/json"},"/cgi-bin/webhook/send?key=08fd1ad4-a341-48be-b57a-e086036b62af&debug=1",body_data

	@savePic
	def _snapshot(self,playerName,playerID,num,picType="",hostUrl = "",cookies={},headers={},path='',dateDir=''):
		rs  = RequestsSessionKeywords(url = hostUrl, cookies = cookies, headers=headers)
		if picType == "snapshot":
			uri = "/api/media/players/{playerID}/snapshot".format(playerID=playerID)
		elif picType == "thumbnail":
			uri = "/api/storage/players/{playerID}/thumbnail/download".format(playerID=playerID)
		else:
			uri = "/api/media/players/{playerID}/snapshot".format(playerID=playerID)	
		response = rs.session_get(uri)
		status_code = response.status_code 
		if status_code == 200:
			return (playerName,playerID,response.content,path,num,dateDir)
		elif status_code == 406:
			logger.error(response.text)
			logger.error("截图超时")
			return False
		else:
			logger.error(response.text)
			logger.warn("当前错误返回码为:",status_code)
			return False

	def timeDifference_seconds(self,startTime,endTime):
		"""
			按秒为单位计算两个时间差
			startTime 开始时间 str
			endTime 结束时间 str
			total_seconds 为 int
		"""
		if isinstance(startTime,str):
			startTime = datetime.datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S")
		if isinstance(endTime,str):
			endTime = datetime.datetime.strptime(endTime, "%Y-%m-%d %H:%M:%S")
		seconds = (endTime - startTime).seconds
		# 来获取时间差中的秒数。注意，seconds获得的秒只是时间差中的小时、分钟和秒部分的和，并没有包含时间差的天数（既是两个时间点不是同一天，失效）
		total_seconds = (endTime - startTime).total_seconds()
		# mins = total_seconds / 60
		return int(total_seconds)


if __name__ == '__main__':
	a = StarRiverKeywords()
	print(a.timeDifference_seconds("2023-01-18 17:19:28","2023-01-18 17:19:31"))