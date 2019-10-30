#!/usr/bin/python
# -*- coding: UTF-8 -*-
from framework.base_page import BasePage







'''
def do_basedata_corp(driver, f, s):

    #企业信息
    driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/a").click()
    time.sleep(f)
    driver.switch_to_frame("http://bus.123cx.com")  # 切换定位器
    driver.find_element_by_xpath("//*[@id='app']/section/section/div[2]/div/form/div[9]/div[2]/div/div/button/span").click()
    time.sleep(f)
    print("企业信息-保存数据成功")

def do_basedata_role(driver, f, s):
    #角色管理
    driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/a/span").click()
    time.sleep(f)
    driver.switch_to_frame("http://bus.123cx.com") #切换定位器
    driver.find_element_by_xpath("//*[@id='role']/div[1]/div/div[3]/div/div/div[1]/div[1]/input").click()
    time.sleep(f)
    driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/ul/li[2]/span").click()#点击选择应用下拉框
    time.sleep(s)
    print("进入角色管理模块")

    #新增角色
    driver.find_element_by_xpath("//*[@id=\"role\"]/div[1]/div/div[3]/div/button").click()
    time.sleep(s)
    driver.find_element_by_xpath("//*[@id='role-dialog']/div/div[2]/form/div[1]/div/div/div/div[1]/input").click()#点击新增下拉框
    time.sleep(f)
    driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/ul/li[1]/span").click()#点击所属应用下拉框
    time.sleep(s)
    driver.find_element_by_xpath("//*[@id=\"role-dialog\"]/div/div[2]/form/div[2]/div/div/div[1]/input").send_keys(u"自动测试角色")
    time.sleep(f)
    driver.find_element_by_xpath("//*[@id=\"role-dialog\"]/div/div[3]/div/button[2]/span").click()
    time.sleep(f)
    print("角色管理-新增自动测试角色成功")

    #查询新增角色
    driver.find_element_by_xpath("//*[@id=\"role\"]/div[1]/div/div[3]/div/div/div[2]/input").send_keys(u"自动测试角色")
    time.sleep(f)
    driver.find_element_by_xpath("//*[@id='role']/div[1]/div/div[3]/div/div/div[2]/i").click()
    time.sleep(f)
    print("角色管理-查询自动测试角色成功")

    #编辑
    driver.find_element_by_xpath("//*[@id=\"role\"]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[4]/div/button[1]/span").click()
    time.sleep(s)
    driver.find_element_by_xpath("//*[@id=\"role-dialog\"]/div/div[2]/form/div[2]/div/div/div/input").send_keys(u"2")
    time.sleep(s)
    driver.find_element_by_xpath("//*[@id=\"role-dialog\"]/div/div[3]/div/button[2]/span").click()
    time.sleep(f)
    print("角色管理-编辑自动测试角色成功")

    #功能权限
    driver.find_element_by_xpath("//*[@id=\"role\"]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[4]/div/button[3]").click()
    time.sleep(s)
    driver.find_element_by_xpath("//*[@id=\"role_auth_dialog\"]/div/div[2]/div/div/div[1]/label/span/span").click()
    time.sleep(f)
    driver.find_element_by_xpath("//*[@id=\"role_auth_dialog\"]/div/div[3]/div/button[2]/span").click()
    time.sleep(f)
    print("角色管理-勾选全部权限成功")

    #删除
    driver.switch_to_frame("http://bus.123cx.com")  # 切换定位器
    driver.find_element_by_xpath("//*[@id=\"role\"]/div[1]/div/div[3]/div/div/div[2]/input").send_keys(u"自动测试角色")#先输入角色
    time.sleep(s)
    driver.find_element_by_xpath("//*[@id='role']/div[1]/div/div[3]/div/div/div[2]/i").click()#再点击查询
    time.sleep(s)
    driver.find_element_by_xpath("//*[@id=\"role\"]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[4]/div/button[2]").click()#点击删除
    time.sleep(s)
    driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/button[2]/span").click()#点击确定
    print("角色管理-删除自动测试角色成功")
    time.sleep(s)

def do_basicdata_Organize(driver, f, s):
    # 组织与员工
    driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/a/span").click()
    time.sleep(f)
    #新增
    driver.find_element_by_xpath("//*[@id=\"app\"]/section/section/div[1]/div[3]/div/div[2]/button[1]").click()
    time.sleep(s)
    driver.find_element_by_xpath("//*[@id=\"app\"]/section/section/div[3]/div[1]/div/div[2]/form/div[1]/div[1]/div/div/div/input").send_keys(u"自动新增员工")
    driver.find_element_by_xpath("//*[@id=\"app\"]/section/section/div[3]/div[1]/div/div[2]/form/div[1]/div[2]/div/div/div/input").send_keys(u"1111")
    driver.find_element_by_xpath("//*[@id=\"app\"]/section/section/div[3]/div[1]/div/div[2]/form/div[1]/div[2]/div/div/div/input").send_keys(u"1111")
    driver.find_element_by_xpath("//*[@id=\"app\"]/section/section/div[3]/div[1]/div/div[2]/form/div[2]/div[1]/div/div/span/span").click()  # 点击新增下拉框
    driver.find_element_by_xpath("/html/body/div[3]/ul[1]/li").click()
    time.sleep(s)
    driver.find_element_by_xpath("//*[@id=\"app\"]/section/section/div[3]/div[1]/div/div[2]/form/div[2]/div[2]/div/div/div/input").send_keys(u"17811111111")#手机号码
    driver.find_element_by_xpath("//*[@id=\"app\"]/section/section/div[3]/div[1]/div/div[2]/form/div[3]/div[1]/div/div/div[1]/input").send_keys(u"17811111111")#员工卡号
    driver.find_element_by_xpath("//*[@id=\"app\"]/section/section/div[3]/div[1]/div/div[2]/form/div[3]/div[2]/div/div/div/input").send_keys(u"430124199902081111")#身份证号码
    driver.find_element_by_xpath( "/html/body/div[4]/div/div[1]/ul/li[2]").click()  # 点击职位
    driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/ul/li[2]/span").click()
    driver.find_element_by_xpath("//*[@id=\"app\"]/section/section/div[3]/div[1]/div/div[3]/div/button[2]/span")#确定
    time.sleep(s)
    #查询
    driver.find_element_by_xpath("//*[@id=\"app\"]/section/section/div[3]/div[1]/div/div[2]/form/div[1]/div[1]/div/div/div/input").send_keys(u"自动新增员工")
    driver.find_element_by_xpath("//*[@id=\"app\"]/section/section/div[1]/div[3]/div/div[1]/div[2]/input").click()
    time.sleep(s)
    #编辑


    time.sleep(s)
    #分配
    driver.find_element_by_xpath("//*[@id=\"app\"]/section/section/div[1]/div[3]/div/div[2]/span/button/span").click()
    time.sleep(f)
    #分配
    driver.find_element_by_xpath("//*[@id=\"app\"]/section/section/div[1]/div[3]/div/div[2]/button[2]").click()
    time.sleep(f)
    driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/a/span").click()
    time.sleep(f)


'''
# if __name__ == "__main__":
#     # 进入基础信息模块
#
#     driver = login.do_login(f, s)
#     driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div/div/div[2]/div[1]/span[1]").click()
#     time.sleep(f)
#
#     #do_basicdata_first(driver, f, s)
#     time.sleep(s)
#     do_basicdata_corp(driver, f, s)
#     time.sleep(s)
#     #do_basicdata_role(driver, f, s)
#     time.sleep(s)
