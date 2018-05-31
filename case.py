#分类开始操作广告
# 每个类初始化，都要elements参数，传入的是可操作元素的字段
import time

class splash():

	def __init__(self):
		print("----开屏广告测试用例初始化成功----")


class banner():

	def __init__(self,driver,elements):
		print("----banner广告测试用例初始化成功，准备执行case----")
		self.driver = driver
		self.elements = elements

	def banner_case_1(self):
		print("----banner广告执行的第一个用例----")
		print("----传入的elements：",self.elements,"----")
		print(self.elements)
		error_msg =["未展示广告","未能轮播","dislike点不了","落地页跳转失败"]
		event = {
		"show":4,
		"click":2,
		"dislike":2
		}
		return {
		"title":"banner广告第一个用例",
		"run_time":time.strftime("%Y-%m-%d %H:%M:%S"),
		"case_code":False,
		"error":error_msg,
		"event":event
		}