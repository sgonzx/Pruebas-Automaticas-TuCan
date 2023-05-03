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

class TestCP006NEditProfile():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cP006NEditProfile(self, EMAIL, PASSWORD, BIO_FALLA, WEBSITE, LOCATION):
    self.driver.get("https://tucan.toolsincloud.net/")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys(EMAIL)
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    self.driver.find_element(By.NAME, "login").click()
    self.driver.find_element(By.CSS_SELECTOR, ".grid-sidebar:nth-child(7) strong").click()
    self.driver.find_element(By.CSS_SELECTOR, ".home-edit-button").click()
    self.driver.find_element(By.NAME, "bio").click()
    self.driver.find_element(By.NAME, "bio").send_keys(BIO_FALLA)
    self.driver.find_element(By.NAME, "website").click()
    self.driver.find_element(By.NAME, "website").send_keys(WEBSITE)
    self.driver.find_element(By.ID, "exampleInputPassword1").click()
    self.driver.find_element(By.ID, "exampleInputPassword1").send_keys(LOCATION)
    self.driver.find_element(By.NAME, "update").click()

  def ejectuarCP006NChrome(self):
    try:
        self.TestCP006Neg = TestCP006NEditProfile()
        
        csvArch = open('"C:\pruebas\Libro1.csv"')
        self.reader = csv.DictReader(csvArch)
          
        for row in self.reader:
          self.TestCP006Neg.setup_method()
          self.TestCP006Neg.test_cP006NEditProfile(EMAIL = row["EMAIL"], PASSWORD = row["PASSWORD"], BIO_FALLA = row["BIO_FALLA"], WEBSITE = row["WEBSITE"], LOCATION = row["LOCATION"])
          self.TestCP006Neg.teardown_method()
          print("EDITAR EL PERFIL DE FORMA FALLIDA CON REGISTRO",row["ID_Reg"],"SE HA EJECUTADO CORRECTAMENTE EN CHROME.")
      
    except:
        print("SE HA DETECTADO UN ERROR EN EL CP006N, SE RECOMIENDA REVISION.")

ejecucion = TestCP006NEditProfile()
ejecucion.ejectuarCP006NChrome()