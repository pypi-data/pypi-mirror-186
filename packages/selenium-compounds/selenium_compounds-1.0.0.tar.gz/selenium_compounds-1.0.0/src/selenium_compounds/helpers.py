import datetime

from .config.getter import get_value

def get_start_date():
        today = datetime.datetime.now()
        return today

def get_end_date(startDate,value):
    if get_value("Duration") == "minutes":
        endDate = startDate + datetime.timedelta(minutes=get_value(value))
        return endDate.strftime("%m/%d/%Y, %H:%M")
    if get_value("Duration") == "hours":
        endDate = startDate + datetime.timedelta(hours=get_value(value))
        return endDate.strftime("%m/%d/%Y, %H")
    if get_value("Duration") == "days":
        endDate = startDate + datetime.timedelta(days=get_value(value))
        return endDate.strftime("%m/%d/%Y")
    
def take_screenshot(driver, screenshot_name):
    DATETIME_FORMAT = '%Y_%m_%d_T_%H_%M_%S_%f'
    location = f"./screenshots/screenshot_{datetime.datetime.now().strftime(DATETIME_FORMAT)}_{screenshot_name}.png"
    driver.save_screenshot(location)