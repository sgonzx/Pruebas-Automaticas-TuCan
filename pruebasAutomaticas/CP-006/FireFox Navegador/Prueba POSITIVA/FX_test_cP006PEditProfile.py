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

class TestCP006PEditProfile():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cP006PEditProfile(self, EMAIL, PASSWORD, BIO, WEBSITE, LOCATION):
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
    self.driver.find_element(By.NAME, "bio").send_keys(BIO)
    self.driver.find_element(By.NAME, "website").click()
    self.driver.find_element(By.NAME, "website").send_keys(WEBSITE)
    self.driver.find_element(By.ID, "exampleInputPassword1").click()
    self.driver.find_element(By.ID, "exampleInputPassword1").send_keys(LOCATION)
    self.driver.find_element(By.NAME, "update").click()

  def ejectuarCP006PFirefox(self):
    try:
        self.TestCP006Po = TestCP006PEditProfile()
        
        csvArch = open('"C:\pruebas\Libro1.csv"')
        self.reader = csv.DictReader(csvArch)
          
        for row in self.reader:
          self.TestCP006Po.setup_method()
          self.TestCP006Po.test_cP006PEditProfile(EMAIL = row["EMAIL"], PASSWORD = row["PASSWORD"], BIO = row["BIO"], WEBSITE = row["WEBSITE"], LOCATION = row["LOCATION"])
          self.TestCP006Po.teardown_method()
          print("EDITAR EL PERFIL SATISFACTORIAMENTE CON REGISTRO",row["ID_Reg"],"SE HA EJECUTADO CORRECTAMENTE EN FIREFOX.")
      
    except:
        print("SE HA DETECTADO UN ERROR EN EL CP006P, SE RECOMIENDA REVISION.")

ejecucion = TestCP006PEditProfile()
ejecucion.ejectuarCP006PFirefox()