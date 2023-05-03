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

class TestCP001NRegistrodeUsuario():
    
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cP001NRegistrodeUsuario(self, NAME, USER, EMAIL, PASSWORD):
    self.driver.get("https://tucan.toolsincloud.net/")
    self.driver.set_window_size(1382, 736)
    self.driver.find_element(By.ID, "auto").click()
    self.driver.find_element(By.ID, "exampleInputEmail1").click()
    self.driver.find_element(By.ID, "exampleInputEmail1").send_keys(NAME)
    self.driver.find_element(By.NAME, "username").click()
    self.driver.find_element(By.NAME, "username").send_keys(USER)
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #exampleInputEmail1").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #exampleInputEmail1").send_keys(EMAIL)
    self.driver.find_element(By.ID, "exampleInputPassword1").click()
    self.driver.find_element(By.ID, "exampleInputPassword1").send_keys(PASSWORD)
    self.driver.find_element(By.NAME, "signup").click()
    
  
  def ejectuarCP001NChrome(self):
    try:
      self.TestCP001Neg = TestCP001NRegistrodeUsuario()
      
      csvArch = open('"C:\pruebas\Libro1.csv"')
      self.reader = csv.DictReader(csvArch)
        
      for row in self.reader:
         self.TestCP001Neg.setup_method()
         self.TestCP001Neg.test_cP001NRegistrodeUsuario(NAME = row["NAME"], USER = row["USER"], EMAIL = row["EMAIL"])
         self.TestCP001Neg.teardown_method()
         print("REGISTRO DE USUARIO EN EL SISTEMA SIN TENER EN CUENTA LA CONTRASEÑA", row["ID_Reg"], "SE HA EJECUTADO CORRECTAMENTE EN CHROME.")
    
    except:
      print("SE HA DETECTADO UN ERROR EN EL CP001N, SE RECOMIENDA REVISION.")

ejecucionPruebaCP001N = TestCP001NRegistrodeUsuario()
ejecucionPruebaCP001N.ejectuarCP001NChrome()
