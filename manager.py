
from appium.webdriver import webdriver
import case
# from app_config import ios,android
import app_config
import create_report
import elements
import time
import logging

#声明日志记录器
logging.basicConfig(level=logging.INFO,
					format='%(asctime)s - %(levelname)s - %(pathname)s --> %(message)s')
logger = logging.getLogger(__name__)
logging.info("日志模块声明成功")


def android_test():
	#配置文件中获取Android设备的信息
	device_desc = app_config.android['des_dic']
	#实例化驱动器
	driver = webdriver.WebDriver(desired_capabilities=device_desc)
	#设置隐形等待元素时间
	driver.implicitly_wait(10)
	#检查是否有授权弹出框
	check_allow_use(driver,app_config.android['allow_instll_id'])

	# 初始化获取元素的类
	logging.info("初始化Android元素类")
	android_elements = elements.android(driver)
	#获取首页的元素列表
	home_elements = android_elements.home_elements


	# 获取到首页的banner按钮，然后点击
	logging.info("开始执行feed的测试用例==========")
	logging.info("1、设置物料响应，接口请求正常后，继续进行。")
	banner_button = home_elements['feed']
	banner_button.click()
	# 进入banner后，执行banner的用例
	banner = case.banner(driver,android_elements.banner_elements())
	logging.info("执行用例，获取测试结果")
	# 执行第一个用例
	result_1 = banner.banner_case_1()
	logging.info("调用创建报告的函数，创建报告")
	create_report.create_rep(result_1)
	logging.info("banner第一个用例执行完毕")



def check_allow_use(driver,allow_buttons):
		# allow_buttons 是列表，依次为允许安装、同意获取各种权限等
		for allo in allow_buttons:
			try:
				allow_use = driver.find_element_by_id(allo)
				allow_use.click()
				logging.info("获取权限成功...")
			except:
				logging.info("获取权限失败...!!!")

		logging.info("权限允许完成")
		

def ios_test():
	logging.info("创建驱动器")
	driver = "ios demo driver"

	logging.info("初始化Android元素类")
	ios_elements = elements.ios(driver)

	logging.info("执行banner测试用例，获取元素")
	banner = case.banner(driver,ios_elements.splash_elements())
	logging.info("执行用例，获取测试结果")
	result_1 = banner.banner_case_1()
	logging.info("调用创建报告的函数，创建报告")
	create_report.create_rep(result_1)

	logging.info("用例执行完毕")



android_test()

















