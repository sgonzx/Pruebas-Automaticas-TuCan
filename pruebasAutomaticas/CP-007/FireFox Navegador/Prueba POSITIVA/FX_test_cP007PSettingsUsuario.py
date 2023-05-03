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

class TestCP007PSettingsUsuario():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cP007PSettingsUsuario(self, EMAIL, PASSWORD, USER_CAMBIO):
    self.driver.get("https://tucan.toolsincloud.net/")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys(EMAIL)
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    self.driver.find_element(By.NAME, "login").click()
    self.driver.find_element(By.CSS_SELECTOR, ".grid-sidebar:nth-child(9) strong").click()
    self.driver.find_element(By.ID, "exampleInputPassword1").click()
    self.driver.find_element(By.ID, "exampleInputPassword1").send_keys(USER_CAMBIO)
    self.driver.find_element(By.NAME, "submit").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".grid-user .username").text == "@TesterQA01"

  def ejectuarCP007PFirefox(self):
    try:
        self.TestCP007Po = TestCP007PSettingsUsuario()
        
        csvArch = open('"C:\pruebas\Libro1.csv"')
        self.reader = csv.DictReader(csvArch)
          
        for row in self.reader:
          self.TestCP007Po.setup_method()
          self.TestCP007Po.test_cP007PSettingsUsuario(EMAIL = row["EMAIL"], PASSWORD = row["PASSWORD"], USER_CAMBIO = row["USER_CAMBIO"])
          self.TestCP007Po.teardown_method()
          print("EDITAR EL USUARIO EN TUCAN CON REGISTRO",row["ID_Reg"],"SE HA EJECUTADO CORRECTAMENTE EN FIREFOX.")
      
    except:
        print("SE HA DETECTADO UN ERROR EN EL CP007P, SE RECOMIENDA REVISION.")

ejecucion = TestCP007PSettingsUsuario()
ejecucion.ejectuarCP007PFirefox()
