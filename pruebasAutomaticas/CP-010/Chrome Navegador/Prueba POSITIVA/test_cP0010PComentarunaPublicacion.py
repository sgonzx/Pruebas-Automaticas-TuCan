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

class TestCP0010PComentarunaPublicacion():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cP0010PComentarunaPublicacion(self, EMAIL, PASSWORD, COMENTARIO):
    self.driver.get("https://tucan.toolsincloud.net/")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys(EMAIL)
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    self.driver.find_element(By.NAME, "login").click()
    self.driver.find_element(By.CSS_SELECTOR, ".box-tweet:nth-child(6) .grid-box-reaction:nth-child(1) .far").click()
    self.driver.find_element(By.CSS_SELECTOR, ".popupComment:nth-child(38) .retweet-msg").click()
    self.driver.find_element(By.CSS_SELECTOR, ".popupComment:nth-child(38) .retweet-msg").send_keys(COMENTARIO)
    self.driver.find_element(By.CSS_SELECTOR, ".popupComment:nth-child(38) .comment-it").click()
    self.driver.find_element(By.CSS_SELECTOR, ".box-tweet:nth-child(6) > a > span").click()
    
  def ejectuarCP0010PChrome(self):
    try:
        self.TestCP0010Po = TestCP0010PComentarunaPublicacion()
        
        csvArch = open('"C:\pruebas\Libro1.csv"')
        self.reader = csv.DictReader(csvArch)
          
        for row in self.reader:
          self.TestCP0010Po.setup_method()
          self.TestCP0010Po.test_cP0010PComentarunaPublicacion(EMAIL = row["EMAIL"], PASSWORD = row["PASSWORD"], COMENTARIO = row["COMENTARIO"])
          self.TestCP0010Po.teardown_method()
          print("COMENTAR UNA PUBLICACION CON REGISTRO",row["ID_Reg"],"SE HA EJECUTADO CORRECTAMENTE EN CHROME.")
      
    except:
        print("SE HA DETECTADO UN ERROR EN EL CP0010P, SE RECOMIENDA REVISION.")

ejecucion = TestCP0010PComentarunaPublicacion()
ejecucion.ejectuarCP0010PChrome()