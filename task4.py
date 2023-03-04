import time
from selenium import webdriver
from selenium.webdriver.common.by import By

my_driver = webdriver.Chrome(
    executable_path="C:/Users/jawad/Desktop/Devops Coruse/chromedriver"
)


# exercise 1


# opening chrome:
def opening_chrome():
    my_driver.get("https://walla.co.il")
    my_driver.close()


# opening_chrome()

# opening firefox:


# exercise 2
def opening_walla():
    my_driver.get("https://walla.co.il")
    title = my_driver.title
    print(title)
    """ refresh driver"""
    my_driver.refresh()
    if title == my_driver.title:
        print("match")
    else:
        print(" not match")
    my_driver.close()


# opening_walla()

# exercise 3
""" regardless to browser type (firefox/Chrome etc ...) when using the inspector , elements are the same"""


# exercise 4


def test():
    my_driver.get("https://translate.google.com/")
    my_driver.find_element(
        By.XPATH,
        "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div",
    ).send_keys("שלום!")


# test()

# exercise 5


def open_youtube():
    my_driver.get("https://www.youtube.com/")
    my_driver.find_element(By.ID, "search").click()
    my_driver.find_element(By.ID, "search").send_keys("livin on a prayer")


# open_youtube()


# exercise 6


def open_google():
    my_driver.get("https://translate.google.com/")
    x = my_driver.find_element(By.ID, "gt-submit")
    y = my_driver.find_element(By.NAME, "jfk-button")
    z = my_driver.find_element(By.XPATH, "//input[@type=‘submit']")
    print(z)
    my_driver.close()


# open_google()


# exercise 7


def open_facebook():
    my_driver.get("https://www.facebook.com/")
    my_driver.find_element(By.ID, "email").send_keys("@gmail")
    my_driver.find_element(By.ID, "pass").send_keys("1234")


# open_facebook()
