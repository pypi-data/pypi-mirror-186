import time

from ..decorators import print_fn
from ..page_utils.selectors import select_no_such_elem_at_xpath

#no such element using xpath
@print_fn
def confirm_no_such_elem_at_xpath(driver, xpath):
    select_no_such_elem_at_xpath(driver, xpath)
    return True