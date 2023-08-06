from .selenium import *
from greatawesomeutils.config import IS_DOCKER
from greatawesomeutils.config import PROFILES_PATH
from greatawesomeutils.lang import silentremove
from greatawesomeutils.user_agents import *
from greatawesomeutils.window_sizes import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as GoogleChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from undetected_chromedriver.v2 import Chrome, ChromeOptions
from .local_storage import LocalStorage
from .relative_path import relative_path
import shutil
from selenium.webdriver.common.action_chains import ActionChains
import pydash


class DriverUtils():
    def get_with_wait(self, link):
        self.get(link)
        # Wait for dom to be interactable
        sleep(2)

    def get_by_current_page_referrer(self, link, wait=2):
        self.execute_script(f"""
                window.location.href = "{link}";
            """)
        if wait is not None and wait != 0:
            sleep(wait)

    def js_click(self, element):
        return js_click(self, element)


    def get_element_or_none_by_selector(self, selector, wait=None):
        return get_element_or_none_by_selector(self, selector, wait)

#     await new Promise((resolve) => {
#       var totalHeight = 0;
#       var distance = 100;
#       let count = 0;

#       var timer = setInterval(() => {
#         count++  
#         var scrollHeight = document.body.scrollHeight;
#           window.scrollBy(0, distance);
#           totalHeight += distance;
#           if (count >=5 ){
#             clearInterval(timer);
#             return resolve();

#           }else{

#           if(totalHeight >= scrollHeight - window.innerHeight){
#               clearInterval(timer);
#               resolve();
#           }}
#       }, 100);
#   });
# 
    def scroll_some(self):
        self.execute_script(""" 
window.scrollBy(0, 10000);
""")

    def scroll_element(self, element):

        is_till_end = self.execute_script("return arguments[0].scrollTop === (arguments[0].scrollHeight - arguments[0].offsetHeight)", element)

        if is_till_end:
            return False
        else:
            
            # self.execute_script("console.log(arguments[0])", element)
            # act = ActionChains(self)
            # act.scroll_from_origin(element, 0, -h).perform()

            # wait_for_enter()

            self.execute_script("arguments[0].scrollBy(0, 10000)", element)
            return True

#         self.execute_script("""
# const el = arguments[0]
        
# const isTillEnd = 

# if (isTillEnd) {
#     return false;    
# } else {
#     el.scrollBy(0, 10000); 
#     return true;
# }
# """, element)

    def get_element_by_id(self, selector, wait=None):
        return get_element_by_id(self, selector, wait)

    def is_in_page(self, target, wait=None, raiseException=False):
        
        def check_page(driver, target):
            if isinstance(target, str):
                return target in driver.current_url
            else: 
                return pydash.some(target, lambda x: x in driver.current_url)
        
        if wait is None:
            return check_page(self, target)
        else:
            time = 0
            while time < wait:
                if check_page(self, target):
                    return True

                sleep_time = 0.2
                time += sleep_time
                sleep(sleep_time)
                
        if raiseException:
            raise Exception(f"Page {target} not found")
        return False

    def get_element_text(self, element):
        return element.get_attribute('innerHTML')

    def get_element_or_none_by_text_contains(self, text, wait=None):
        return get_element_or_none_by_text_contains(self, text, wait)

    def get_element_or_none_by_text(self, text, wait=None):
        return get_element_or_none_by_text(self, text, wait)


    def get_element_or_none_by_name(self, selector, wait=None):
        return get_element_or_none_by_name(self, selector, wait)
   
    def get_element_or_none(self, path, wait=None):
        return get_element_or_none(self, path, wait)

    def get_html(self):
        return get_html(self)

    def wait_till_element_to_disappear_by_selector(self,  selector,  wait):
        try:
            WebDriverWait(driver, wait).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, selector)))
            return True
        except:
            return False

    def get_elements_or_none_by_selector(self, selector, wait=None):
        return get_elements_or_none_by_selector(self, selector, wait)

    def extract_links(self, elements):
        def extract_link(el):
            return el.get_attribute("href")

        return list(map(extract_link, elements))

    def extract_links_starting_with(self, start, wait=None):
        els = self.get_elements_or_none_by_selector("a", wait)

        links = self.extract_links(els)

        def is_not_none(link):
            return link is not None

        def is_starts_with(link):
            return link.startswith(start)

        return list(filter(is_starts_with, filter(is_not_none, links)))

    def print_body(self):
        return print_body(self)

    def organic_get_via(self, link, via, wait=2):
        def visit(driver):
            driver.get(via)

        def run(driver, link):
            visit(driver)
            driver.get_by_current_page_referrer(link, wait)

        run(self, link)

    def organic_get(self, link, wait=2):
        self.organic_get_via(link, "https://www.google.com/", wait)


    def get_innerhtml(self, el):
        return el.get_attribute("innerHTML")

    def get_cookies_as_dict(self):
        all_cookies = self.get_cookies()
        cookies_dict = {}
        for cookie in all_cookies:
            cookies_dict[cookie['name']] = cookie['value']
        return cookies_dict

    def delete_all_site_data(self):
        self.delete_all_cookies()
        self.execute_script("window.localStorage.clear();")
        self.execute_script("window.sessionStorage.clear();")

    def add_cookies(self, cookies):
        for key in cookies:
            self.add_cookie({"name": key, "value": cookies[key]})

    def get_local_storage(self):
        storage = LocalStorage(self)
        return storage.items()

    def add_local_storage(self, local_storage):
        storage = LocalStorage(self)
        for key in local_storage:
            storage.set(key, local_storage[key])

    def get_all_site_data(self):
        cookies = self.get_cookies_as_dict()
        local_storage = self.get_local_storage()

        return {"cookies": cookies, "local_storage": local_storage}

    def add_all_site_data(self, site_data):
        cookies = site_data["cookies"]
        local_storage = site_data["local_storage"]
        self.add_cookies(cookies)
        self.add_local_storage(local_storage)


class MyChrome(Chrome, DriverUtils):
    pass


class MyGoogleChrome(webdriver.Chrome, DriverUtils):
    pass


class MyFirefox(webdriver.Firefox, DriverUtils):
    pass


def delete_cache(driver):
    print('Deleting Cache')
    driver.command_executor._commands['SEND_COMMAND'] = (
        'POST', '/session/$sessionId/chromium/send_command'
    )
    driver.execute('SEND_COMMAND', dict(
        cmd='Network.clearBrowserCache', params={}))


def add_useragent(options, user_agent):
    options.add_argument(f'--user-agent={user_agent}')


def create_profile_path(user_id):
    PATH = f'{PROFILES_PATH}/{user_id}'
    path = relative_path(PATH, 2)
    return path


def delete_corrupted_files(user_id):
    is_success = silentremove(
        f'{create_profile_path(user_id)}/SingletonCookie')
    silentremove(f'{create_profile_path(user_id)}/SingletonSocket')
    silentremove(f'{create_profile_path(user_id)}/SingletonLock')

    if is_success:
        print('Fixed Profile by deleting Corrupted Files')
    else:
        print('No Corrupted Profiles Found')


def delete_profile_path(user_id):
    path = create_profile_path(user_id)
    shutil.rmtree(path, ignore_errors=True)


RANDOM = "RANDOM"
HASHED = "HASHED"


def add_essential_options(options, user_id, window_size, user_agent):
    options.add_argument("--start-maximized")
    
    if window_size is not None:
        if window_size == RANDOM:
            window_size = WindowSizesInstance.get_unique_random_value()
        elif window_size == HASHED:
            window_size = WindowSizesInstance.get_hashed_value(user_agent)

        print("window-size: ", window_size)
        options.add_argument(f"--window-size={window_size}")
#
    if user_agent is not None:
        if user_agent == RANDOM:
            user_agent = UserAgentsInstance.get_unique_random_value()
        elif user_agent == HASHED:
            user_agent = UserAgentsInstance.get_hashed_value(user_agent)

        print("user_agent: ", user_agent)
        add_useragent(options, user_agent)

    has_user = user_id is not None
    if has_user:
        path = create_profile_path(user_id)
        print("user-data-dir: ", path)
        user_data_path = f"--user-data-dir={path}"
        options.add_argument(user_data_path)
    else:
        print("No User was Given")

    return options


def get_eager_startegy():

    caps = DesiredCapabilities().CHROME
    # caps["pageLoadStrategy"] = "normal"  #  Waits for full page load
    caps["pageLoadStrategy"] = "none"   # Do not wait for full page load
    return caps


UNDETECTED_DRIVER = 'undetected_chromedriver'
FIREFOX_DRIVER = 'firefox_driver'
GOOGLE_DRIVER = 'google_driver'


def hide_automation_flags(options):
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--disable-blink-features")

    options.add_experimental_option(
        "excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    # New Options
    options.add_argument("--ignore-certificate-errors")
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-extensions")



def create_driver_by_driver_type(driver_type, user_id, window_size, user_agent, is_eager):

    if FIREFOX_DRIVER == driver_type:
        # TODO: ADD SUPPORT FOR PARAMS
        options = FirefoxOptions()
        options.headless = False

        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

        has_user = user_id is not None
        if has_user:
            path = create_profile_path(user_id)
            options.set_preference('profile', path)
            print('SET PROFILES_PATH: ', path)

        driver = MyFirefox(
            options=options,
            # firefox_profile=add_tor(),
            # capabilities=create_proxy_capability('130.41.55.190:8080'),
            executable_path=relative_path("drivers/geckodriver.exe", 1),
            #  proxy=create_proxy('130.41.55.190:8080')
        )

    else:
        is_undetected = driver_type == UNDETECTED_DRIVER
        options = ChromeOptions() if is_undetected else GoogleChromeOptions()

        if IS_DOCKER:
            print("Running in Docker, So adding sandbox arguments")
            options.arguments.extend(
                ["--no-sandbox", "--disable-setuid-sandbox"])
        else:
            print("Not Running in Docker, So not adding sandbox arguments")

        add_essential_options(options, user_id, window_size, user_agent)

        if is_eager:
            desired_capabilities = get_eager_startegy()
            print('Driver will not wait for page to load fully')
        else:
            desired_capabilities = None
        print("Creating Driver")
        

        if is_undetected:
            driver = MyChrome(desired_capabilities=desired_capabilities,
                              options=options, version_main= 106 if IS_DOCKER else 108)
        else:
            # options.add_experimental_option("prefs",  {"profile.managed_default_content_settings.images": 2})
            hide_automation_flags(options)
            
            # CAPTCHA
            options.arguments.extend(
                ["--disable-web-security", "--disable-site-isolation-trials", "--disable-application-cache"])

            path = relative_path("drivers/chromedriver.exe", 1)
            print(f'driver path: {path}' )
            driver = MyGoogleChrome(
                desired_capabilities=desired_capabilities,
                chrome_options=options,
                executable_path=path,
            )
        print("Created Driver")

    return driver


def create_undetected_driver(user_id, window_size, user_agent, is_eager=False):
    return create_driver_by_driver_type(UNDETECTED_DRIVER, user_id, window_size, user_agent, is_eager)


def create_chrome_driver(user_id, window_size, user_agent, is_eager=False):
    return create_driver_by_driver_type(GOOGLE_DRIVER, user_id, window_size, user_agent, is_eager)


if __name__ == "__main__":
    # run using python -m .selenium_driver
    driver = create_chrome_driver()
    # visit_google(driver)
    # el = find_element_by_selector_with_wait(driver, "div.denfrfrgkbrg", 10)
    get_element_or_none_by_selector(driver, 'a.pHiOh').click()

    print(driver.current_url)
    # driver.find_element(By.NAME, "q")
    driver.close()
    driver.quit()
