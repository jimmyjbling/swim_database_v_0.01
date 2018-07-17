from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests


def login(user_psw):
    """
    completes login in to website
    :param user_psw: username and psw list
    :return: None
    """
    driver = webdriver.Firefox()
    driver.get("https://veronanat.recdesk.com/Director/Login/adminlogin.aspx")
    wait = ui.WebDriverWait(driver, 10)
    wait.until(page_is_loaded)
    user_field = driver.find_element_by_id('UserName')
    user_field.send_keys(user_psw[0])
    psw_field = driver.find_element_by_id('UserPassword')
    psw_field.send_keys(user_psw[1])
    psw_field.send_keys(Keys.RETURN)


def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") is not None


def login_info():
    """
    collects login in info
    :return: username, password
    """
    user = input('Username: ')
    psw = input('Password: ')
    return [user, psw]


login(login_info())
