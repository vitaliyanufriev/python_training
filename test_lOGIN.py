# Generated by Selenium IDE
import pytest
from time import sleep
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLOGIN():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_lOGIN(self):
    self.driver.get("https://platform.today/en/casino")
    self.driver.set_window_size(1491, 973)
    self.driver.execute_script("window.scrollTo(0,0)")
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn-signin .auth-controls__title")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-signin .auth-controls__title").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.XPATH, "(//input[@type=\'text\'])[2]").send_keys("vitand33")
    self.driver.find_element(By.XPATH, "//input[@type=\'password\']").send_keys("123qwe")
    self.driver.find_element(By.CSS_SELECTOR, ".user-credentials-form__item:nth-child(1) .ng-dirty").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sign-in__with-footer").click()
    self.driver.find_element(By.CSS_SELECTOR, ".user-credentials-form__item:nth-child(3) .ng-dirty").click()
    self.driver.find_element(By.CSS_SELECTOR, ".user-credentials-form__btn").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    element = self.driver.find_element(By.CSS_SELECTOR, ".ng-star-inserted .nav-menu__link_img")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn_deposit")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()

    self.driver.find_element(By.CSS_SELECTOR, ".client-section-menu__account-logo").click()
    sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".client-section-menu__item:nth-child(1) > .client-section-menu__control").click()
    sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".btn-close__icon > .icons-font-close").click()
    sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".client-section-menu__caret-down-icon > .icons-font-caret-down").click()
    sleep(1)
    self.driver.find_element(By.XPATH, "//span[contains(.,\'Logout\')]").click()
  
