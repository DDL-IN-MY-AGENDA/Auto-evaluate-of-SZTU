#!/usr/bin/python3
# *coding=utf-8* #

import contextlib
from seleniums import *
from systems import *
from login import login
from random import randint
from random import sample
from random import shuffle
from time import sleep


def evaluate_techer() -> None:
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="Frame1"]'))
    try:
        # 行数
        i = 2
        # 评价的每个指标都要有选择，本着能给每个老师都争取较好的评价，将前四个选项进行随机排序，后面的其他选项都从1-2中选择
        options = [1, 2, 3, 4]
        shuffle(options)
        for option in options:
            driver.find_element(By.XPATH,f'//*[@id="table1"]/tbody/tr[{i}]/td[2]/label[{option}]/i').click()
            i += 1
        while 1:
            # 选项 1-4
            j = randint(1,2)
            driver.find_element(By.XPATH,f'//*[@id="table1"]/tbody/tr[{i}]/td[2]/label[{j}]/i').click()
            i += 1
    except Exception:
        driver.find_element(By.XPATH,'//*[@id="jynr"]').send_keys('My evaluation---python selenium')
        try:
            driver.find_element(By.XPATH,'//*[@id="bc"]').click()
            close_alert()
            # fuck_off_alert()
        except Exception:
            driver.find_element(By.XPATH,'//*[@id="qx"]').click()

def evaluate_techer_switcher() -> None:
    try:
        i = 2
        # 遍历到最后一个的下一个时找不到元素会退出循环
        while 1:
            driver.find_element(By.XPATH,f'//*[@id="dataList"]/tbody/tr[{i}]/td[8]/a').click()
            evaluate_techer()
            i += 1
    except Exception:
        try:
            driver.find_element(By.XPATH,'//*[@id="btnsubmit"]').click()
        except Exception:
            driver.find_element(By.XPATH,'//*[@id="bc"]').click()
        close_alert()
        driver.find_element(By.XPATH,'//*[@id="btnShenshen"]').click()
        close_alert()

def hit_like() -> None:
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="Frame1"]'))
    try:
        # 获取首页最大的序号
        like_table = driver.find_element(By.XPATH, '//*[@id="dataList"]/tbody')
        rows = like_table.find_elements(By.TAG_NAME, 'tr')
        maxIndex = len(rows)
        print(maxIndex)
        # 有三次点赞机会
        random_num = sample(range(2, maxIndex + 1), 3)
        for index in random_num:
            driver.find_element(By.XPATH,f'//*[@id="dataList"]/tbody/tr[{index}]/td[7]/a').click()
            # 关闭弹窗
            close_alert()
        # 退出
        driver.find_element(By.XPATH,'//*[@id="btnShenshen"]').click()
        close_alert()
    except Exception:
        print("出错了，可能前面页面以更新...")

def close_alert() -> None:
    with contextlib.suppress(Exception):
        sleep(1)
        alert = driver.switch_to.alert
        alert.accept()

def select_page() -> None:
    driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="Frame1"]'))
    # 给老师点赞
    driver.find_element(By.XPATH,'//*[@id="Form1"]/table/tbody/tr[4]/td[8]/a').click()
    hit_like()
    # 综合模式
    driver.find_element(By.XPATH,'//*[@id="Form1"]/table/tbody/tr[2]/td[8]/a').click()
    evaluate_techer_switcher()
    # 德国模式
    driver.find_element(By.XPATH,'//*[@id="Form1"]/table/tbody/tr[3]/td[8]/a').click()
    evaluate_techer_switcher()
    driver.switch_to.default_content()


def main() -> None:
    global driver, catalog_name, working_catalog_index

    print("欢迎使用深技大自动评教软件，本软件仅供学习使用")
    print("")
    print("Github仓库地址：")
    driver_type = int(input("请输入你的浏览器类型（Edge:输入0，Chrome:输入1）："))
    print(f"使用本软件之前请关闭你的{'Chrome' if driver_type else 'Edge'}浏览器")
    print("浏览器启动中...")
    if driver_type:
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)
    else:
        options = webdriver.EdgeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')
        driver = webdriver.Edge(options=options)
    login(driver)
    print("开始自动测评！")
    sleep(3)
    driver.find_element(By.XPATH,'//*[@id="accordion"]/li[11]/div/i').click()
    driver.find_element(By.XPATH,'//*[@id="accordion"]/li[11]/ul/li/div/i').click()
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="accordion"]/li[11]/ul/li/ul/li').click()
    select_page()
    print('Done!')
    print("By seleniums, zion")

if __name__ == '__main__':
    main()