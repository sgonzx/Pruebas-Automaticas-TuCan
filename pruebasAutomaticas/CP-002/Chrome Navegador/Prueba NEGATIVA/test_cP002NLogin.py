# Generated by Selenium IDE
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

class TestCP002NLogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cP002NLogin(self, EMAIL, PASSWORD_FALLA):
    self.driver.get("https://tucan.toolsincloud.net/")
    self.driver.set_window_size(1382, 736)
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys(EMAIL)
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys(PASSWORD_FALLA)
    self.driver.find_element(By.NAME, "login").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".span-fp-error").text == "the email or password is not correct"
  
  def ejectuarCP002NChrome(self):
    try:
        self.TestCP002Neg = TestCP002NLogin()
        
        csvArch = open('"C:\pruebas\Libro1.csv"')
        self.reader = csv.DictReader(csvArch)
          
        for row in self.reader:
          self.TestCP002Neg.setup_method()
          self.TestCP002Neg.test_cP002NLogin(EMAIL = row["EMAIL"], PASSWORD_FALLA = row["PASSWORD_FALLA"])
          self.TestCP002Neg.teardown_method()
          print("EL INGRESO AL SISTEMA POR EL USUARIO CON LA CONTRASEÑA ERRONEA CON REGISTRO",row["ID_Reg"],"SE HA EJECUTADO CORRECTAMENTE EN CHROME.")
      
    except:
        print("SE HA DETECTADO UN ERROR EN EL CP002N, SE RECOMIENDA REVISION.")

ejecucionPruebaCP002N = TestCP002NLogin()
ejecucionPruebaCP002N.ejectuarCP002NLogin()
