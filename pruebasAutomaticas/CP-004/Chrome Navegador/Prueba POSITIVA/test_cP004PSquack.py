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

class TestCP004PSquack():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cP004PSquack(self, EMAIL, PASSWORD, COMENTARIO):
    self.driver.get("https://tucan.toolsincloud.net/")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys(EMAIL)
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    self.driver.find_element(By.NAME, "login").click()
    self.driver.find_element(By.NAME, "status").click()
    self.driver.find_element(By.NAME, "status").send_keys(COMENTARIO)
    self.driver.find_element(By.ID, "tweet-input").click()

  def ejectuarCP004PChrome(self):
    try:
        self.TestCP004Po = TestCP004PSquack()
        
        csvArch = open('"C:\pruebas\Libro1.csv"')
        self.reader = csv.DictReader(csvArch)
          
        for row in self.reader:
          self.TestCP004Po.setup_method()
          self.TestCP004Po.test_cP004PSquack(EMAIL = row["EMAIL"], PASSWORD = row["PASSWORD"], COMENTARIO = row["COMENTARIO"])
          self.TestCP004Po.teardown_method()
          print("COMENTAR O HACER SQUAWK CON REGISTRO",row["ID_Reg"],"SE HA EJECUTADO CORRECTAMENTE EN CHROME.")
      
    except:
        print("SE HA DETECTADO UN ERROR EN EL CP004P, SE RECOMIENDA REVISION.")

ejecucion = TestCP004PSquack()
ejecucion.ejectuarCP004PChrome()