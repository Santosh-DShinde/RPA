import json, sys, os
from RPA.Browser.Selenium import Selenium
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rpa_builder.base import RPABuilder
from config.loggings import get_logger

class SandiegoRPA(RPABuilder):
    def __init__(self, conf_path: str, timeout: int=15):
        self.browser = Selenium()
        self.browser.set_selenium_implicit_wait(timeout)
        super().__init__(self.browser)
        self.timeout: int = timeout
        self.conf_path: str = conf_path
        self.form_data: dict = {}
        self.logger = get_logger()
        self.load_config()

    def load_config(self):
        try:
            with open(self.conf_path) as conf_file:
                self.form_data = json.load(conf_file)
        except Exception as e:
            raise Exception(f"Enable to access the config file.\n{str(e, e.__traceback__)}")

    def login(self):
        self.logger.info("Started Login process")
        self.browser.open_available_browser(self.form_data.get("base_url"))
        self.browser.driver.switch_to.frame("LoginFrame")
        self.browser.wait_until_element_is_visible("id:username", self.timeout)
        self.browser.input_text("id:username", self.form_data.get("credentials").get("username"))
        self.browser.wait_until_element_is_visible("id:passwordRequired", self.timeout)
        self.browser.input_text("id:passwordRequired", self.form_data.get("credentials").get("passward"))
        self.browser.click_element_when_visible("xpath://button[contains(@class,'p-element ACA_Button')]//span[1]")
        self.browser.driver.switch_to.default_content()
        self.logger.info("Completed Login process")

    def initiate_application(self):
        try:
            self.logger.info("Started initiating appl^n")
            self.find_element("id:ctl00_PlaceHolderMain_MyCollectionList_ListMyCollections_ctrl0_noDataLabel")
            self.click_element("xpath://a[@module='DSD']", 10)
            self.click_element("xpath://span[@class='search-sub-menu']//a[1]", 10)
            self.click_element("id:ctl00_PlaceHolderMain_termAccept", 10)
            self.click_element("xpath://a[@title='Continue Application »']//span[1]", 10)
            self.logger.info("Initiated appl^n")

        except Exception as e:
            raise Exception(f"Main Exeption:{str(e)}\nTraceback: {str(e.__traceback__)}")

def main():
    try:
        manager = SandiegoRPA("data/sandiego.json")
        manager.login()
        manager.initiate_application()

    except Exception as e:
        raise Exception(f"Main Exeption:{str(e)}\nTraceback: {str(e.__traceback__)}")
    except KeyboardInterrupt:
        print("Bye")
    finally:
        input("Enter for close the browser...")
        manager.close_browser()

if __name__=="__main__":
    main()
