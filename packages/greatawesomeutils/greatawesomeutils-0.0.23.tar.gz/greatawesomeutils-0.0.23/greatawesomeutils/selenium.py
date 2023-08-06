from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import  WebElement
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from greatawesomeutils.config import LOGS_PATH, SCREENSHOTS_PATH
from .relative_path import relative_path
from greatawesomeutils.config import WAIT_DURATION
from greatawesomeutils.lang import retry, write_file, write_html


def get_search_box(driver):
    m = driver.find_element(By.NAME, "q")
    return m


def search_for(driver, keyword):

    def doit():

        m = get_search_box(driver)
        # enter search text
        m.send_keys(keyword)
        sleep(1)
        # perform Google search with Keys.ENTER
        m.send_keys(Keys.ENTER)

    def run():
        doit()
        value = get_search_box(driver).get_attribute("value")
        if value != keyword:
            raise Exception(
                f"Expected keyword: {keyword} but was: {value}"
            )

    retry(run, 2, 2)


def get_direct(driver: WebDriver, link, src='Direct'):
    print(f"{src} Click: {link}")
    driver.get(link)


def get_twitter(driver: WebDriver, link):
    driver.get(link)

    # target="_blank"
    selector = "a.css-4rbku5.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1ny4l3l.r-1udh08x.r-o7ynqc.r-6416eg.r-13qz1uu"

    el = get_element_or_none_by_selector(
        driver, selector, WAIT_DURATION)

    href = el.get_attribute("href")

    print(f"Twitter Click: {href}")

    # Prevent opening in new tab
    driver.execute_script(
        f'''document.querySelector("{selector}").removeAttribute('target')''')

    el.click()


def add_cookies(driver: WebDriver, cookies):
    for key in cookies:
        driver.add_cookie({"name": key, "value": cookies[key]})


def get_cookies(driver):
    all_cookies = driver.get_cookies()
    cookies_dict = {}
    for cookie in all_cookies:
        cookies_dict[cookie['name']] = cookie['value']
    return cookies_dict


def delete_all_site_data(driver: WebDriver):
    driver.delete_all_cookies()
    driver.execute_script("window.localStorage.clear();")
    driver.execute_script("window.sessionStorage.clear();")


SAVE_SCREENSHOT_ERROR_FOLDER = 'errors'
SAVE_SCREENSHOT_DEBUG_FOLDER = 'debug'
SAVE_SCREENSHOT_SUCCESS_FOLDER = 'success'


def get_html(driver):
    html = driver.execute_script("return document.body.innerHTML;")
    return html


def save_html_logs(driver, ID):
    html = get_html(driver)
    path = f'{LOGS_PATH}/{ID}.html'
    write_html(path, html)
    print('Written HTML ', path)


def save_screenshot(driver, ID, folder_type, tag=None):
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    try:
        # success
        tag = '-' if tag is None else f'-{tag}-'
        saving_screenshot_at = relative_path(
            f'{SCREENSHOTS_PATH}/{folder_type}/{ID}{tag}{now}.png', 2)
        driver.get_screenshot_as_file(
            saving_screenshot_at)
        print(f'Saved Screenshot at location: ..{saving_screenshot_at}')
    except:
        print('Failed to save screenshot')


def find_element_by_selector_with_wait(driver, xpath, wait):
    return WebDriverWait(driver, wait).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, xpath)))


def get_element_or_none(driver, xpath, wait=None):
    try:
        if wait is None:
            return driver.find_element(By.XPATH, xpath)
        else:
            return WebDriverWait(driver, wait).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
    except:
        return None


def get_element_or_none_by_text_contains(driver, text, wait=None):
    text = f'//*[contains(text(), "{text}")]'
    return get_element_or_none(driver, text, wait)


def get_element_or_none_by_text(driver, text, wait=None):
    text = f'//*[text()="{text}"]'
    
    return get_element_or_none(driver, text, wait)


def get_element_parent(element):
    return element.find_element(By.XPATH, "./..")


def get_element_or_none_by_selector(driver: WebDriver, selector, wait=None) -> WebElement:
    try:
        if wait is None:
            return driver.find_element(By.CSS_SELECTOR, selector)
        else:
            return WebDriverWait(driver, wait).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
    except:
        return None


def get_element_by_id(driver: WebDriver, id, wait=None):
    return get_element_or_none_by_selector(driver, f'[id="{id}"]', wait)



def get_elements_or_none_by_selector(driver: WebDriver, selector, wait=None):
    try:
        if wait is None:
            return driver.find_elements(By.CSS_SELECTOR, selector)
        else:
            WebDriverWait(driver, wait).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

            return driver.find_elements(By.CSS_SELECTOR, selector)
    except:
        return None


def get_element_or_none_by_name(driver, selector, wait=None):
    try:
        if wait is None:
            return driver.find_element(By.NAME, selector)
        else:
            return WebDriverWait(driver, wait).until(
                EC.presence_of_element_located((By.NAME, selector)))
    except:
        return None


def print_body(driver):
    html = driver.find_element(
        By.XPATH, "/html/body").get_attribute('innerHTML')
    return html


def click(driver, xpath):
    driver.find_element(
        By.XPATH, xpath).click()


def assert_in_page(driver, page):
    assert (page in driver.current_url)


def js_click(driver, element):
    driver.execute_script("arguments[0].click();",  element)
