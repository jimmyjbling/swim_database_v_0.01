from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


def collect_dara():
    """
    creates cvs file with relevant data of swimmers
    :return: None
    """
    driver = login(login_info())
    program_links = get_program_list(driver)
    wait = ui.WebDriverWait(driver, 10)
    for link in program_links:
        extract_data(driver, link)


def login(user_psw):
    """
    completes login in to website
    :param user_psw: username and psw list
    :return: created driver
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
    return driver


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


def get_program_list(driver):
    wait = ui.WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.ID, 'MasterHeaderCtl_liPrograms')))
    driver.find_element_by_id('MasterHeaderCtl_liPrograms').click()
    wait.until(expected_conditions.presence_of_element_located((By.ID, 'pgmTable_wrapper')))
    return driver.find_elements_by_partial_link_text('Session C')


def extract_data(driver, link):
    wait = ui.WebDriverWait(driver, 10)
    link.click()
    wait.until(expected_conditions.presence_of_element_located((By.ID, 'PageContent_cmdViewRoster')))
    driver.find_element_by_id('PageContent_cmdViewRoster').click()
    wait.until(expected_conditions.presence_of_element_located((By.ID, 'tblList')))
    table = driver.find_element_by_id('tb1List')
    


def write_to_database(info):


def read_from_database(info):


def update_database(info):


login(login_info())
