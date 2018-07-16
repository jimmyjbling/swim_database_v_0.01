from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests


def login_info():
    """
    collects login in info

    :return: username, password
    """
    user = input('Username')
    psw = input('Password')
    return user, psw


def login(user, psw):
    """
    completes login in to website

    :param user: username
    :param psw: password
    :return: None
    """
    driver = webdriver.Firefox
    driver.get(url="https://veronanat.recdesk.com/Director/Login/adminlogin.aspx")
    wait = ui.WebDriverWait(driver, 10)
    wait.until(page_is_loaded)
    user_field = driver.find_element_by_id('UserName')
    user_field.send_keys(user)
    psw_field = driver.find_element_by_id('UserPassword')
    psw_field.send_keys(psw)
    psw_field.send_keys(Keys.RETURN)


def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") is not None
