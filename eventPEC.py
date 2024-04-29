import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def send_event_pec(driver, index):
    time.sleep(5)

    driver.get("https://beta.apimecnacional.com.br/profissional/peccnpi/create")

    # click in position to select the option
    time.sleep(4)
    container_select = driver.find_element(By.ID, "select2-TipoEvento-container")
    container_select.click()

    time.sleep(2)
    select_option = driver.find_element(By.CLASS_NAME, "select2-search__field")
    select_option.send_keys("Jogo do Conhecimento")
    select_option.send_keys(Keys.ENTER)
    
    # add the data to event forms
    new_event_input = driver.find_element(By.ID, "novoEvento")
    new_event_input.send_keys(f"Evento teste - {index}")

    date = driver.find_element(By.ID, "data")
    date.send_keys("09/01/2025")

    event_time_duration = driver.find_element(By.ID, "numero")
    event_time_duration.send_keys("5")

    enterprise_responsible = driver.find_element(By.ID, "empresa")
    enterprise_responsible.send_keys("Joao Corps")

    details = driver.find_element(By.ID, "detalhe")
    details.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed interdum diam vitae libero sollicitudin, in faucibus mi feugiat. Ut tempus, nisl posuere euismod commodo, purus felis ullamcorper tortor, vitae rutrum diam tortor sed libero. Ut scelerisque, erat elementum efficitur volutpat, arcu velit molestie nibh, ac tempus leo tortor eget arcu. Ut eu augue imperdiet turpis hendrerit ullamcorper eu tincidunt sapien. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus tortor nisi, tincidunt sit amet auctor eu, mollis et libero. Cras sodales in eros vitae dapibus. Fusce ut imperdiet leo. Proin eleifend dignissim dui ut mollis. Proin eleifend turpis ut blandit commodo. Cras vel fringilla ligula, quis tristique velit. Suspendisse potenti. Nunc iaculis ligula a egestas hendrerit.")

    # file upload
    upload_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "upload_PEC.pdf"))

    file_input = driver.find_element(By.ID, "Arquivo")
    file_input.send_keys(upload_file)

    time.sleep(2)
    driver.find_element(By.ID, "save").click()
    
    time.sleep(2)