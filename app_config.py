# 存放跑用例的测试机信息
'''
安卓 网盟SDK demoAPP 的配置参数
	'platformName':'Android',
	'platformVersion':'8.0.0',
	'deviceName':'mate8',
	'appActivity':'.SplashActivity',
	'appPackage':'com.union_test.toutiao'


{
  "platformName": "ios",
  "platformVersion": "11.2.6",
  "deviceName": "王志坤的 iPhone",
  "bundleId": "com.lemontree.union.wangzk",
  "udid": "63f8cfd828f7ee7871182f643d65e5bfa3bd623e"
}


{
  "platformName": "Android",
  "platformVersion": "8.0.0",
  "deviceName": "mate10",
  "appActivity": ".SplashActivity",
  "appPackage": "com.union_test.toutiao"
}



'''

# 如果每次跑，会要求安装的话，存放允许安装的id
huawei_mate10 = "com.android.packageinstaller:id/permission_allow_button"
vivo_y66 = "android:id/button1"
sanxing_s6 = ""

ios = {
	"des_dic":"test_bundel_id"
}

android = {
	"des_dic":{
	'platformName':'Android',
	#'platformVersion':'8.0.0',
	'deviceName':'s6',
	'appActivity':'.SplashActivity',
	'appPackage':'com.union_test.toutiao'
	},
	"allow_instll_id":sanxing_s6,
}





