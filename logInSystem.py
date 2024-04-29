import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from eventPEC import send_event_pec

if len(sys.argv) > 1:
    # Open browser
    driver = webdriver.Firefox()
    driver.get("https://beta.apimecnacional.com.br/")

    time.sleep(5)

    # Type user credencials
    emailInput = driver.find_element(By.ID, "Email")
    passwordInput = driver.find_element(By.ID, "Senha")

    emailInput.clear()
    passwordInput.clear()
    
    emailInput.send_keys(f"profissional{sys.argv[1]}@inntecnet.com.br")
    passwordInput.send_keys("inntecnet")

    driver.find_element(By.XPATH, "//form[@method='POST']").submit()

    for index in range(0, 20):
        send_event_pec(driver, index)

    time.sleep(10)
    driver.close()
else:
    print("[ERROR]: Passe qual o profissional que vai logar como parametro")
