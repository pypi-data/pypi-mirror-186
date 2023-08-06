import os
import time
from typing import List, Optional, Union
from io import BytesIO
from PIL import Image
# RPA library imports
from RPA.core import webdriver
from RPA.Browser.Selenium import Selenium
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.remote.webelement import WebElement
# Local imports
from justrpa.browser.chrome import start_chrome_windows
from justrpa.browser.firefox import get_firefox_profile_path, FILE_CONTENT_TYPE
from justrpa.utils.file import create_dir_for_file
from justrpa.errors import BrowserNotAvailable

# RPA Browser Selenium Extension; adds common browser methods.
class SeleniumExt(Selenium):  
    def sleep_short(self):
        self.sleep(2)
    
    def sleep_medium(self):
        self.sleep(4)
    
    def sleep_long(self):
        self.sleep(8)
    
    def sleep_very_long(self):
        self.sleep(20)

    def sleep(self, seconds:int):
        time.sleep(seconds)

    def get_driver_path(self, browser:str)->str:
        def is_tool(name):
            """Check whether `name` is on PATH and marked as executable."""
            from shutil import which
            return which(name) is not None
        path_cache = webdriver.cache(browser)
        if path_cache:
            return path_cache
        # Try to download webdriver
        try:
            path_download = webdriver.download(browser)
            return path_download
        except Exception as e:
            self.logger.error(f"Failed to download webdriver: {e}")
            pass
        return None

    def get_firefox_profile(self, download_dir:str=None):
        ff_profile_path = get_firefox_profile_path()
        self.logger.info(f"Firefox profile: {ff_profile_path} ")
        profile = FirefoxProfile(ff_profile_path)
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.link.open_newwindow", 1)
        profile.set_preference("browser.download.manager.showWhenStarting",False)
        if download_dir:
            dl_dir = os.path.abspath(download_dir)
            self.logger.info(f"download_dir:{dl_dir}")
            profile.set_preference("browser.download.dir", dl_dir)
        profile.set_preference("browser.helperApps.alwaysAsk.force", False)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", FILE_CONTENT_TYPE)
        profile.set_preference("browser.download.manager.closeWhenDone", True)
        profile.set_preference("pdfjs.disabled", True)
        return profile

    def open_firefox_browser(self, url:str, download_dir:str=None)->None:
        driver_path = self.get_driver_path("firefox")
        self.logger.info(f"driver path: {driver_path}")
        ff_profile_path = self.get_firefox_profile(download_dir)
        self.logger.info(f"Firefox profile: {ff_profile_path.profile_dir} ")
        self.logger.info(f"Firefox profile: {ff_profile_path.path} ")
        # self.open_browser(url,browser="firefox", ff_profile_dir="/Users/yanjing/Library/Application Support/Firefox/Profiles/kpzh8uvf.default-release")
        self.open_browser(url,browser="firefox", ff_profile_dir=ff_profile_path, executable_path=f"{driver_path}", service_log_path='output/gecko.log')

    def open_new_tab(self, url):
        self.logger.info(f"open new tab: {url}")
        num_tabs = len(self.driver.window_handles)
        self.driver.execute_script("window.open('about:blank', '_blank');")
        num_tabs_after = len(self.driver.window_handles)
        self.logger.info(f"num_tabs: {num_tabs}, num_tabs_after: {num_tabs_after}")
        self.new_tab= num_tabs_after>num_tabs 
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.get(url)
    
    def close_tab(self):
        opened = self.new_tab if hasattr(self, 'new_tab') else False
        self.logger.info(f"opened tab: {opened}. ")
        if opened:
            self.logger.info(f"close tab: {self.driver.current_url}")
            self.driver.close()

    def prepare_browser(self, url:str)->None:
        self.logger.info(f"browser:{self.browser}, New browser: {self.new_browser}, {self.browser_info}")
        handler = {
            0:self.attach_default_browser,
            1:self.open_new_browser,
            2:self.open_after_attach_fail
        }
        # info(f"{handler[self.new_browser]}")
        handler[self.new_browser](url)
        #self.attach_default_browser(url)

    def open_new_browser(self, url:str)->None:
        browser_info = self.browser_info
        browser_name = browser_info['name']
        if browser_name == 'chrome':
            # profile_path = "/Users/yanjing/Library/Application Support/Google/Chrome/"
            #options.AddArgument("--ignore-certificate-errors");
            #options.AddArgument("--disable-popup-blocking");
            # info(f"download_dir:{download_dir}")
            # prefs = {
            #     "download.default_directory": download_dir,
            #     "download.prompt_for_download": False,
            #     "download.directory_upgrade": True,
            # }
            self.logger.info(f"open chrome with default profile")
            if hasattr(self, "download_dir"):
                self.download_dir = os.path.abspath(self.download_dir)
                self.set_download_directory(self.download_dir)
            self.open_chrome_browser(url, use_profile=False, maximized=True, headless=self.headless)
            self.logger.info(f"Opended browser")
            self.go_to(url)
            self.logger.info(f"Go to {url}")
            # self.open_chrome_browser(url, use_profile=browser_info["use_profile"],profile_path=browser_info["profile_path"])
        elif browser_name == 'default':
            self.open_available_browser(url)
        elif browser_name == 'firefox':
            self.open_firefox_browser(url, self.download_dir)
            self.set_selenium_speed(0.2)
        else:
            self.open_available_browser(url, browser_selection=browser_name)   
        self.logger.info(f"Opened new browser: {browser_name}. ")

    def open_after_attach_fail(self, url:str)->None:
        try:
            self.check_browser_and_attach(url, clean=False)
        except BrowserNotAvailable as ex:
            self.logger.error(ex, stack_info=True)  
            self.check_browser_and_attach(url, clean=True)
    
    def check_browser_and_attach(self, url:str, clean=False):
        result = start_chrome_windows(clean)
        if result:
            self.sleep_short()
            self.attach_default_browser(url)
        else:
            self.logger.error("Can't connect to Chrome. And start failed.")

    def attach_default_browser(self,url:str):
        try:
            self.attach_chrome_browser(self.attach_port)
            self.set_selenium_timeout(20)
        except Exception as ex:
            self.logger.error(ex, stack_info=True)  
            raise BrowserNotAvailable("Attach browser failed. Browser is not opened or not available for connect.") 
        self.logger.info(f"Attached to browser.")
        self.open_new_tab(url)

    def cleanup(self):
        self.sleep_short()
        self.close_tab()
        if self.new_browser == 1:
            self.logger.info(f"Opened new browser, will close it.")
            self.close_browser()

    ################################################################
    ## Screenshot functions
    def screenshot_fullpage(self, file, scroll_delay=0.3):
        driver = self.driver
        device_pixel_ratio = driver.execute_script('return window.devicePixelRatio')
        total_height = driver.execute_script('return document.body.parentNode.scrollHeight')
        viewport_height = driver.execute_script('return window.innerHeight')
        total_width = driver.execute_script('return document.body.offsetWidth')
        viewport_width = driver.execute_script("return document.body.clientWidth")
        assert(viewport_width == total_width)
        # scroll the page, take screenshots and save screenshots to slices
        offset = 0
        slices = {}
        while offset < total_height:
            if offset + viewport_height > total_height:
                offset = total_height - viewport_height
            driver.execute_script('window.scrollTo({0}, {1})'.format(0, offset))
            time.sleep(scroll_delay)
            img = Image.open(BytesIO(driver.get_screenshot_as_png()))
            slices[offset] = img
            offset = offset + viewport_height
        # combine image slices
        # info(f"{device_pixel_ratio} {total_height} {viewport_height} {total_width} {viewport_width}")
        stitched_image = Image.new('RGB', (int(total_width * device_pixel_ratio), int(total_height * device_pixel_ratio)))
        for offset, image in slices.items():
            stitched_image.paste(image, (0, int(offset * device_pixel_ratio)))
        stitched_image.save(file)

    def screenshot_to_dest(self, filepath:str, full_page:bool=False):
        create_dir_for_file(filepath)
        if full_page:
            self.screenshot_fullpage(file=filepath)
        else:
            self.screenshot(filename=filepath)

    ################################################################
    # JS functions
    def scroll_to_element(self, locator: Union[WebElement, str]):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    def zoom_in(self, ratio=1):
        js = f"document.body.style.zoom = '{ratio}'"
        self.driver.execute_script(js)
    
    def input_element_text_by_js(self, locator: Union[WebElement, str], text:str):
        element = self.find_element(locator)
        script = f'arguments[0].value="{text}";arguments[0].dispatchEvent(new Event("change"));'
        self.driver.execute_script(script, element)

    def click_element_by_js(self, locator: Union[WebElement, str]):
        self.wait_until_element_is_visible(locator,20)
        self.click_element_by_js_directly(locator)

    def click_element_by_js_directly(self, locator: Union[WebElement, str]):
        element = self.find_element(locator)
        script = f'arguments[0].click();'
        self.driver.execute_script(script, element)

    def hide_element_by_js(self, locator: Union[WebElement, str]):
        if self.does_page_contain_element(locator)==False:
            return
        element = self.find_element(locator)
        script = f"arguments[0].innerHTML = '';"
        self.driver.execute_script(script, element)

    ################################################################
    # Simple combine functions    
    def focus_and_input_text(self,locator: Union[WebElement, str], text:str):
        self.mouse_over(locator)
        self.clear_element_text(locator)
        #self.input_text(locator, text)
        self.input_element_text_by_js(locator, text)
    
    def focus_and_click_element(self, locator: Union[WebElement, str]):
        self.mouse_over(locator)
        self.click_element(locator)
    
    def focus_and_select_checkbox(self, locator: Union[WebElement, str]):
        self.mouse_over(locator)
        self.select_checkbox(locator)

    ##################################################################
    # actions
    def action_screenshot(self, filepath:str, full_page:bool=False, hide_locators:List[str]=[]):
        for locator in hide_locators:
            self.hide_element_by_js(locator)
        self.screenshot_to_dest(filepath, full_page)