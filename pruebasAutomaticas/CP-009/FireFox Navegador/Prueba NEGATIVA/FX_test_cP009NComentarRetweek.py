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

class TestCP009NComentarRetweek():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cP009NComentarRetweek(self, EMAIL, PASSWORD, COMENTARIO_FALLA):
    self.driver.get("https://tucan.toolsincloud.net/")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys(EMAIL)
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    self.driver.find_element(By.NAME, "login").click()
    self.driver.find_element(By.CSS_SELECTOR, ".box-tweet:nth-child(27) .grid-box-reaction:nth-child(2) .fas").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fa-pencil-alt").click()
    self.driver.find_element(By.CSS_SELECTOR, ".popupTweet:nth-child(64) .retweet-msg").click()
    self.driver.find_element(By.CSS_SELECTOR, ".popupTweet:nth-child(64) .retweet-msg").send_keys(COMENTARIO_FALLA)
    self.driver.find_element(By.CSS_SELECTOR, ".popupTweet:nth-child(64) .qoute-it").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "h2").text == "Home"
  
  def ejectuarCP009NFirefox(self):
    try:
        self.TestCP009Neg = TestCP009NComentarRetweek()
        
        csvArch = open('"C:\pruebas\Libro1.csv"')
        self.reader = csv.DictReader(csvArch)
          
        for row in self.reader:
          self.TestCP009Neg.setup_method()
          self.TestCP009Neg.test_cP009NComentarRetweek(EMAIL = row["EMAIL"], PASSWORD = row["PASSWORD"], COMENTARIO_FALLA = row["COMENTARIO_FALLA"])
          self.TestCP009Neg.teardown_method()
          print("COMENTAR UNA RETWEEK DE MANERA FALLIDA EN TUCAN CON REGISTRO",row["ID_Reg"],"SE HA EJECUTADO CORRECTAMENTE EN FIREFOX.")
      
    except:
        print("SE HA DETECTADO UN ERROR EN EL CP009N, SE RECOMIENDA REVISION.")

ejecucion = TestCP009NComentarRetweek()
ejecucion.ejectuarCP009NFirefox()
