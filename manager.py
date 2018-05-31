# 入口
from mylog import mylog
from appium.webdriver import webdriver
import case
# from app_config import ios,android
import app_config
import create_report
import elements
import time

logger = mylog(True)

def android_test():
	#配置文件中获取Android设备的信息
	device_desc = app_config.android['des_dic']
	#实例化驱动器
	driver = webdriver.WebDriver(desired_capabilities=device_desc)
	#检查是否有授权弹出框
	check_allow(app_config.android['allow_instll_id'])


	logger.myprint("初始化Android元素类")
	android_elements = elements.android(driver)

	logger.myprint("执行banner测试用例，获取元素")
	banner = case.banner(driver,android_elements.banner_elements())
	logger.myprint("执行用例，获取测试结果")
	result_1 = banner.banner_case_1()
	logger.myprint("调用创建报告的函数，创建报告")
	create_report.create_rep(result_1)

	logger.myprint("用例执行完毕")


def check_allow(allow_buttons):
		# allow_buttons 是列表，依次为允许安装、同意获取各种权限等
		logger.myprint("安装成功，获取权限成功")


def ios_test():
	logger.myprint("创建驱动器")
	driver = "ios demo driver"

	logger.myprint("初始化Android元素类")
	ios_elements = elements.ios(driver)

	logger.myprint("执行banner测试用例，获取元素")
	banner = case.banner(driver,ios_elements.splash_elements())
	logger.myprint("执行用例，获取测试结果")
	result_1 = banner.banner_case_1()
	logger.myprint("调用创建报告的函数，创建报告")
	create_report.create_rep(result_1)

	logger.myprint("用例执行完毕")



android_test()

















