
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
		print("android devices elements.....")

	def splash_elements(self):

		print("android - splash - elements.")
		return 1

	def banner_elements(self):
		# e1 = self.driver.find_element_by_id("iiiii")
		print("android - banner - elements.")
		return 1


