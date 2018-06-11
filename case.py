#分类开始操作广告
# 每个类初始化，都要elements参数，传入的是可操作元素的字段
import logging

'''测试用例执行结果返回接口
{
		"title":"banner广告第一个用例",  						#测试用例标题
		"run_time":time.strftime("%Y-%m-%d %H:%M:%S"),		#执行测试用例的时间
		"case_code":False,									#是否通过
		"error":error_msg,									#错误信息，是个列表
		"event_ex":event_ex,								# 预计产生的事件数量
		"event_ac":event_ac									# 数据库查到的事件数量
		}



'''

import time

class splash():

	def __init__(self):
		logging.info("----开屏广告测试用例初始化成功----")

class feed():

	def __init__(self):
		logging.info("------feed 广告测试用例初始化成功------")

	def feed_case_1(self):
		logging.info("-----feed 第一个测试用例，执行成功-------")


class banner():

	def __init__(self,driver,elements):
		logging.info("----banner广告测试用例初始化成功，准备执行case----")
		self.driver = driver
		self.elements = elements

	def banner_case_1(self):
		logging.info("----banner广告执行的第一个用例----")
		logging.info("----传入的elements：",self.elements,"----")
		logging.info(self.elements)
		error_msg =["未展示广告","未能轮播","dislike点不了","落地页跳转失败"]
		# 预期的事件数量
		event_ex = {
		"show":4,
		"click":2,
		"dislike":2
		}
		# es 查到是事件数量
		event_ac = {
			"show": 4,
			"click": 2,
			"dislike": 2
		}
		self.driver.keyevent(4)
		return {
		"title":"banner广告第一个用例",
		"run_time":time.strftime("%Y-%m-%d %H:%M:%S"),
		"case_code":False,
		"error":error_msg,
		"event_ex":event_ex,
		"event_ac":event_ac
		}