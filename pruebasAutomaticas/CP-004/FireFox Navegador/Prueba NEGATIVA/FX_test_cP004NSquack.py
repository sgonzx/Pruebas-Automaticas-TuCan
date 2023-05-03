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

class TestCP004NSquack():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cP004NSquack(self, EMAIL, PASSWORD, COMENTARIO_FALLA):
    self.driver.get("https://tucan.toolsincloud.net/")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys(EMAIL)
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    self.driver.find_element(By.NAME, "login").click()
    self.driver.find_element(By.NAME, "status").click()
    self.driver.find_element(By.NAME, "status").send_keys(COMENTARIO_FALLA)
    self.driver.find_element(By.ID, "tweet-input").click()
    
  def ejectuarCP004NFirefox(self):
    try:
        self.TestCP004Neg = TestCP004NSquack()
        
        csvArch = open('"C:\pruebas\Libro1.csv"')
        self.reader = csv.DictReader(csvArch)
          
        for row in self.reader:
          self.TestCP004Neg.setup_method()
          self.TestCP004Neg.test_cP004NSquack(EMAIL = row["EMAIL"], PASSWORD = row["PASSWORD"], COMENTARIO_FALLA = row["COMENTARIO_FALLA"])
          self.TestCP004Neg.teardown_method()
          print("COMENTAR O HACER SQUAWK DE FORMA FALLIDA CON REGISTRO",row["ID_Reg"],"SE HA EJECUTADO CORRECTAMENTE EN FIREFOX.")
      
    except:
        print("SE HA DETECTADO UN ERROR EN EL CP004N, SE RECOMIENDA REVISION.")

ejecucion = TestCP004NSquack()
ejecucion.ejectuarCP004NFirefox()
  
