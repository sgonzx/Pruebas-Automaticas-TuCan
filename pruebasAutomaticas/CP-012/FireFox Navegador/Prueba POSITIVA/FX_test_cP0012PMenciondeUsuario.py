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

class TestCP0012PMenciondeUsuario():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cP0012PMenciondeUsuario(self, EMAIL, PASSWORD, USER_MENC, COMENTARIO):
    self.driver.get("https://tucan.toolsincloud.net/")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys(EMAIL)
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    self.driver.find_element(By.NAME, "login").click()
    self.driver.find_element(By.NAME, "status").click()
    self.driver.find_element(By.NAME, "status").send_keys(USER_MENC)
    self.driver.find_element(By.NAME, "status").send_keys(USER_MENC + COMENTARIO)
    self.driver.find_element(By.ID, "tweet-input").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "h2").text == "Home"
    
  def ejectuarCP0012PFirefox(self):
    try:
        self.TestCP00120Po = TestCP0012PMenciondeUsuario()
        
        csvArch = open('"C:\pruebas\Libro1.csv"')
        self.reader = csv.DictReader(csvArch)
          
        for row in self.reader:
          self.TestCP0012Po.setup_method()
          self.TestCP0012Po.test_cP0012PMenciondeUsuario(EMAIL = row["EMAIL"], PASSWORD = row["PASSWORD"], USER_MENC = ["USER_MENC"], COMENTARIO = row["COMENTARIO"])
          self.TestCP0012Po.teardown_method()
          print("MENCIONAR OTRO USUARIO EN TUCAN CON REGISTRO",row["ID_Reg"],"SE HA EJECUTADO CORRECTAMENTE EN FIREFOX.")
      
    except:
        print("SE HA DETECTADO UN ERROR EN EL CP0012P, SE RECOMIENDA REVISION.")

ejecucion = TestCP0012PMenciondeUsuario()
ejecucion.ejectuarCP0012PFirefox()

  
