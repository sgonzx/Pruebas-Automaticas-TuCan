import pytest
import time
import json
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCP002PLogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cP002PLogin(self, EMAIL, PASSWORD):
    self.driver.get("https://tucan.toolsincloud.net/")
    self.driver.set_window_size(1382, 736)
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys(EMAIL)
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    self.driver.find_element(By.NAME, "login").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "h2").text == "Home"
    
  def ejectuarCP002PChrome(self):
    try:
        self.TestCP002Po = TestCP002PLogin()
        
        csvArch = open('"C:\pruebas\Libro1.csv"')
        self.reader = csv.DictReader(csvArch)
          
        for row in self.reader:
            self.TestCP002Po.setup_method()
            self.TestCP002Po.test_cP002PLogin(EMAIL = row["EMAIL"], PASSWORD = row["PASSWORD"])
            self.TestCP002Po.teardown_method()
            print("EL INGRESO AL SISTEMA POR EL USUARIO CON REGISTRO",row["ID_Reg"],"SE HA EJECUTADO CORRECTAMENTE EN CHROME.")
      
    except:
        print("SE HA DETECTADO UN ERROR EN EL CP002P, SE RECOMIENDA REVISION.")

ejecucion = TestCP002PLogin()
ejecucion.ejectuarCP002PChrome()