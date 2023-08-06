from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from ..decorators import print_fn
from ..config.getter import get_value

#set driver to default
def set_default(driver):
    driver.switch_to.default_content()
    
@print_fn
def select_all_elems_by_xpath(driver, xpath):
    return driver.findElements(By.XPATH, xpath)

@print_fn
def select_elem(driver, by, selector, wait:int=None):
    return WebDriverWait(driver, (get_value("imp_wait") if wait is None else wait)).until(
        EC.element_to_be_clickable((by, selector)))

@print_fn
def select_elem_by_id(driver, id_elem, wait:int=None):
    return select_elem(driver, By.ID, id_elem, wait)

@print_fn
def select_elem_by_xpath(driver, xpath_elem, wait:int=None):
    return select_elem(driver, By.XPATH, xpath_elem, wait)

def determine_selectors_and_return(driver, selector:str):
    if selector.startswith('//'):
        return select_elem_by_xpath(driver, selector)
    else:
        return select_elem_by_id(driver, selector)

#******************************************************************************
#* IFRAMES                                                                    *
#****************************************************************************** 

@print_fn
def switch_to_iframe(driver, by=By.TAG_NAME, selector:str="iframe"):
    if selector.startswith("//"):
        driver.switch_to.frame(driver.find_element(By.XPATH, selector))
    else:
        driver.switch_to.frame(driver.find_element(by, selector))

@print_fn
def select_elem_by_id_in_iframe(driver, id_elem):
    switch_to_iframe(driver)
    return select_elem_by_id(driver, id_elem)

@print_fn
def select_elem_by_xpath_in_iframe(driver, xpath_elem):
    switch_to_iframe(driver)
    return select_elem_by_xpath(driver, xpath_elem)

@print_fn
def select_elem_by_id_in_iframe_by_xpath(driver, id_elem, xpath_iframe):
    switch_to_iframe(driver, By.XPATH, xpath_iframe)
    return select_elem_by_id(driver, id_elem)

@print_fn
def select_elem_by_xpath_in_iframe_by_xpath(driver, xpath_elem, xpath_iframe):
    switch_to_iframe(driver, By.XPATH, xpath_iframe)
    return select_elem_by_xpath(driver, xpath_elem, 50)

def select_no_such_elem_at_xpath(driver, xpath):
    try:
        element = driver.find_element(By.XPATH, xpath)
        print('Element present, marking as fail')
        element.click()
        return False
    except NoSuchElementException:
        return True