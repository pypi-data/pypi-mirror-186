import time

from ..config.getter import get_value
from ..page_utils.selectors import select_elem_by_xpath

def switch_to_child_window(driver):
    # get current window handle
    time.sleep(get_value("exp_wait"))
    chwnd = driver.window_handles[1]
    # to switch focus the first child window handle
    driver.switch_to.window(chwnd)
    return driver

def switch_to_main_window(driver):
    prntwnd = driver.window_handles[0]
    driver.switch_to.window(prntwnd)
    return driver

def switch_to_child_window_and_click_elem(driver, xpath_elem):
    switch_to_child_window()
    elem = select_elem_by_xpath(driver, xpath_elem)
    elem.click()