from urllib.request import urlopen
from selenium import webdriver
from flask_testing import LiveServerTestCase
from hello_world import app


class MyTest(LiveServerTestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8943
        app.config['LIVESERVER_TIMEOUT'] = 5
        return app

    def test_server_is_up_and_running(self):
        response = urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

    def test_selenium_simple_html_site(self):
        site_url = self.get_server_url() + "/testhtml"
        driver = webdriver.Chrome()
        driver.get(site_url)
        expected_link = "https://www.wp.pl/"
        driver.find_element_by_xpath("/html/body/a").click()
        actual_link = driver.current_url
        self.assertEqual(actual_link, expected_link)
        driver.quit()
