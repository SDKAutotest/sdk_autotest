
import logging
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
        logging.info("开始获取Android demo APP首页的元素.....")
        # 首页上，各个广告入口的按钮id
        id_dic = {
        "banner":"com.union_test.toutiao:id/btn_main_banner",
        "feed" : "com.union_test.toutiao:id/btn_main_feed",
        "dialog":"com.union_test.toutiao:id/btn_mian_insert",
        "splash":"com.union_test.toutiao:id/btn_mian_splash",
        "reward_video":"com.union_test.toutiao:id/btn_mian_reward"
        }
        element_dic = {}

        for key in id_dic.keys():
            try:
                element_dic[key] = self.driver.find_element_by_id(id_dic[key])
                logging.info("获取到元素:"+key)
            except:
                logging.info("未能获取到元素:"+key)
        print(element_dic)
        logging.info("获取Android demo APP首页的元素完成，返回。")
        return element_dic


    def splash_elements(self):
        print("android - splash - elements.")
        return 1

    def banner_elements(self):
        # e1 = self.driver.find_element_by_id("iiiii")
        print("android - banner - elements.")
        return 1



