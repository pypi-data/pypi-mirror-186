from ..page_utils.selectors import *
from ..decorators import print_fn

@print_fn
def get_left_menu_by_id(driver, id_menu):
    return select_elem_by_id(driver, id_menu)

@print_fn
def get_left_menu_by_xpath(driver, xpath_menu):
    return select_elem_by_xpath(driver, xpath_menu)

@print_fn
def get_loan_info_apps(driver, id_elem, xpath_iframe):
    return select_elem_by_id_in_iframe_by_xpath(driver, id_elem, xpath_iframe)

@print_fn
def get_button_by_xpath_in_iframe(driver, xpath_button, xpath_iframe):
    return select_elem_by_xpath_in_iframe_by_xpath(driver, xpath_button, xpath_iframe)

@print_fn
def get_loan_button(driver, xpath_button, xpath_iframe):
    return select_elem_by_xpath_in_iframe_by_xpath(driver, xpath_button, xpath_iframe)

@print_fn
def get_enter_by_id(driver, id_enter):
    return select_elem_by_id(driver, id_enter)

@print_fn
def get_enter_by_id_in_iframe(driver, id_enter):
    return select_elem_by_id_in_iframe(driver, id_enter)

@print_fn
def get_username_field_by_id(driver, id_username_field):
    return select_elem_by_id(driver, id_username_field)

@print_fn
def get_username_field_by_id_in_iframe(driver, id_username_field):
    return select_elem_by_id_in_iframe(driver, id_username_field)

@print_fn
def get_password_field_by_id(driver, id_password_field):
    return select_elem_by_id(driver, id_password_field)

@print_fn
def get_password_field_by_id_in_iframe(driver, id_password_field):
    return select_elem_by_id_in_iframe(driver, id_password_field)

@print_fn
def get_button_in_custom_view(driver, xpath_button, xpath_iframe):
    return select_elem_by_xpath_in_iframe_by_xpath(driver, xpath_button, xpath_iframe)
    
@print_fn
def get_links_in_mmt_agent_script(driver, xpath_links, xpath_iframe):
    return select_elem_by_xpath_in_iframe_by_xpath(driver, xpath_links, xpath_iframe)

