from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
from decouple import config


driver = webdriver.Chrome(
    executable_path='/home/shekhar/chromedriver')
driver.get('http://github.com/login')


def create():
    username = config('username')
    password = config('password')
    driver.find_element_by_id("login_field").send_keys('{}'.format(username))
    driver.find_element_by_id("password").send_keys('{}'.format(password))
    driver.find_element_by_name("commit").click()
    driver.get('http://github.com/new')
    project_name = sys.argv[1]
    driver.find_element_by_id("repository_name").send_keys('{}'.format(
        project_name))
    submit_button = driver.find_element_by_css_selector('button.first-in-line')
    submit_button.submit()
    driver.close()


if __name__ == "__main__":
    create()
