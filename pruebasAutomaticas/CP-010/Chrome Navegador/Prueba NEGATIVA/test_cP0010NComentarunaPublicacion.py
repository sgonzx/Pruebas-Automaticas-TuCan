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

class TestCP0010NComentarunaPublicacion():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cP0010NComentarunaPublicacion(self, EMAIL, PASSWORD, COMENTARIO_FALLA):
    self.driver.get("https://tucan.toolsincloud.net/")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys(EMAIL)
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    self.driver.find_element(By.NAME, "login").click()
    self.driver.find_element(By.CSS_SELECTOR, ".box-tweet:nth-child(3) .grid-box-reaction:nth-child(1) .far").click()
    self.driver.find_element(By.CSS_SELECTOR, ".popupComment:nth-child(38) .retweet-msg").click()
    self.driver.find_element(By.CSS_SELECTOR, ".popupComment:nth-child(38) .retweet-msg").send_keys(COMENTARIO_FALLA)
    self.driver.find_element(By.CSS_SELECTOR, ".popupComment:nth-child(38) .comment-it").click()  

  def ejectuarCP0010NChrome(self):
    try:
        self.TestCP0010Neg = TestCP0010NComentarunaPublicacion()
        
        csvArch = open('"C:\pruebas\Libro1.csv"')
        self.reader = csv.DictReader(csvArch)
          
        for row in self.reader:
          self.TestCP0010Neg.setup_method()
          self.TestCP0010Neg.test_cP0010NComentarunaPublicacion(EMAIL = row["EMAIL"], PASSWORD = row["PASSWORD"], COMENTARIO_FALLA = row["COMENTARIO_FALLA"])
          self.TestCP0010Neg.teardown_method()
          print("COMENTAR DE FORMA FALLIDA UNA PUBLICACION CON REGISTRO",row["ID_Reg"],"SE HA EJECUTADO CORRECTAMENTE EN CHROME.")
      
    except:
        print("SE HA DETECTADO UN ERROR EN EL CP0010N, SE RECOMIENDA REVISION.")

ejecucion = TestCP0010NComentarunaPublicacion()
ejecucion.ejectuarCP0010NChrome()