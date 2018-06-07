
#iOS上的元素获取
class ios():

	def __init__(self,driver):
		self.driver = driver
		print("ios devices elements.....")

	def splash_elements(self):
		print("ios - splash - elements.")
		return 3

#Android上的元素获取
class android():

	def __init__(self,driver):
		self.driver = driver
		self.home_elements =self.home_element()
		print("android devices elements.....")

	def home_element(self):
		print("初始化获取元素的方法时，直接获取到整个首页的元素列表")
		self.driver.find_element_by_id
		return {
		"banner" : 1,
		"feed" :1,
		"splash":2,
		}

	def splash_elements(self):

		print("android - splash - elements.")
		return 1

	def banner_elements(self):
		# e1 = self.driver.find_element_by_id("iiiii")
		print("android - banner - elements.")
		return 1


