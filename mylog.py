#自定义的log模块

import time

class mylog():

	def __init__(self,outfile=False):
		self.outfile = outfile

	def myprint(self,msg):
		if self.outfile == False:
			print(time.strftime('%Y-%m-%d %H:%M:%S >> ')+msg)
		else:
			p_str = time.strftime('%Y-%m-%d %H:%M:%S >> ')+msg
			with open('./log/'+time.strftime('%Y-%m-%d'),'a',encoding='utf-8') as f:
				try:
					f.write(p_str+'\n')
					print(p_str)
				except Exception as e:
					print(e)