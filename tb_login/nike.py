# -*- coding:UTF-8 -*-
import datetime
import time
from datetime import date, timedelta
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import platform
import logging

import os

NIKE_LOGIN_URL = 'https://accounts.nike.com.cn/lookup?client_id=e5517bcc26532d959b2532654ac037dd&redirect_uri=https://www.nike.com.cn/auth/login&response_type=code&scope=openid%20nike.digital%20profile%20email%20phone%20flow%20country&state=a4beedc2458346468c38b6838238b7a0&code_challenge=6MPvltp00LR-hfTcXlS6KjR4mdn0ye5roz5bBEE2_s0&code_challenge_method=S256'
FAVORITE_URL = 'https://www.nike.com.cn/favorites'
goals_url = 'https://detail.tmall.com/item.htm?spm=a220o.1000855.0.da321h.497931ff7qimjV&id=662291580865&skuId=4950425878923'


class Login:

    def __init__(self, account, password, buy_time):
        self.browser = None
        self.account = account
        self.password = password
        self.buy_time = buy_time

    def open(self, url):
        self.browser.get(url)
        self.browser.implicitly_wait(20)

    def start(self):
        # 1 初始化浏览器
        self.init_browser()
        # 2 打开淘宝登录页
        # self.browser.get(NIKE_LOGIN_URL)
        # time.sleep(1)
        # # 3 输入用户名
        # self.write_username(self.account)
        # time.sleep(1.5)
        # # 4 输入密码
        # self.write_password(self.password)
        # time.sleep(1.5)
        # 7 登录成功，直接请求页面
        print("登录成功，跳转至目标页面")
        time.sleep(3.5)
        self.buy_sth_need()

    def buy_sth_need(self):
        number = 0
        while True:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            if now >= self.buy_time:
                print(now)
                try:
                    self.get_favorite()
                except:
                    time.sleep(0.02)
                number += 1
            if number == 4:
                break

    def switch_to_password_mode(self):
        """
        切换到密码模式
        :return:
        """
        if self.browser.find_element_by_id('J_QRCodeLogin').is_displayed():
            self.browser.find_element_by_id('J_Quick2Static').click()

    def write_username(self, username):
        """
        输入账号
        :param username:
        :return:
        """
        try:
            username_input_element = self.browser.find_element_by_id('username')
        except:
            logging.info("username 传入失败")

        username_input_element.clear()
        username_input_element.send_keys(username)

        try:
            privacy_term = self.browser.find_element_by_id("privacyTerms").click()
        except:
            logging.info("点击隐私条款 失败")

        self.browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div/form/div/div[3]/button').click()


    def write_password(self, password):
        """
        输入密码
        :param password:
        :return:
        """

        try:
            password_input_element = self.browser.find_element_by_id("password")
        except:
            print("未在页面找到相应信息")

        #

        password_input_element.clear()
        password_input_element.send_keys(password)
        self.browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/form/div/div[2]/button').click()

    def get_favorite(self):
        self.browser.get(FAVORITE_URL)
        label = False
        try:
            self.browser.find_element_by_link_text("选择尺码").click()
            label = True
        except:
            logging.info("页面尚未更新")
        if label:
            time.sleep(0.01)
            self.browser.find_element_by_link_text("38").click()
            time.sleep(0.01)
            self.browser.find_element_by_link_text("加入购物车").click()




    def lock_exist(self):
        """
        判断是否存在滑动验证
        :return:
        """
        return self.is_element_exist('#nc_1_wrapper') and self.browser.find_element_by_id(
            'nc_1_wrapper').is_displayed()

    def unlock(self):
        """
        执行滑动解锁
        :return:
        """
        if self.is_element_exist("#nocaptcha > div > span > a"):
            self.browser.find_element_by_css_selector("#nocaptcha > div > span > a").click()

        bar_element = self.browser.find_element_by_id('nc_1_n1z')
        ActionChains(self.browser).drag_and_drop_by_offset(bar_element, 258, 0).perform()
        if self.is_element_exist("#nocaptcha > div > span > a"):
            self.unlock()
        time.sleep(0.5)

    def submit(self):
        """
        提交登录
        :return:
        """
        try:
            self.browser.find_element_by_css_selector("#login-form > div.fm-btn > button").click()
        except:
            self.browser.find_element_by_id('J_SubmitStatic').click()

        time.sleep(0.5)
        if self.is_element_exist("#J_Message"):
            self.write_password(self.password)
            self.submit()
            time.sleep(5)

    def navigate_to_target_page(self):
        pass

    # def init_date(self):
    #     date_offset = 0
    #     self.today_date = (date.today() + timedelta(days=-date_offset)).strftime("%Y-%m-%d")
    #     self.yesterday_date = (date.today() + timedelta(days=-date_offset-1)).strftime("%Y-%m-%d")

    def init_browser(self):
        self.downloadPath = os.getcwd()
        CHROME_DRIVER = os.path.abspath(os.path.dirname(os.getcwd())) + os.sep + 'chromedriver' + os.sep
        if platform.system() == 'Windows':
            CHROME_DRIVER = os.getcwd() + os.sep + 'chromedriver.exe'
        else:
            CHROME_DRIVER = os.getcwd() + os.sep + 'chromedriver'
        """
        初始化selenium浏览器
        :return:
        """
        options = Options()
        # options.add_argument("--headless")
        # prefs = {"profile.managed_default_content_settings.images": 2}
        prefs = {"profile.managed_default_content_settings.images": 1, 'download.default_directory': self.downloadPath}
        # 1是加载图片，2是不加载图片
        options.add_experimental_option("prefs", prefs)
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--proxy-server=http://127.0.0.1:9000')
        options.add_argument('disable-infobars')
        options.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome(executable_path=CHROME_DRIVER, options=options)
        self.browser.implicitly_wait(3)
        self.browser.maximize_window()

    def is_element_exist(self, selector):
        """
        检查是否存在指定元素
        :param selector:
        :return:
        """
        try:
            self.browser.find_element_by_css_selector(selector)
            return True
        except NoSuchElementException:
            return False

account = 'username'
# 输入你的账号名
password = 'password'
# 输入你密码
Login(account, password, '2022-10-26 21:19:00.000000').start()