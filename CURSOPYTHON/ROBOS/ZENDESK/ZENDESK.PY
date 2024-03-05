from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Substitua o caminho abaixo pelo caminho do seu ChromeDriver baixado
driver_path = "C:/caminho_para_o_seu_chromedriver/chromedriver.exe"
chrome_service = ChromeService(driver_path)
driver = webdriver.Chrome(service=chrome_service)

# Substitua pelos seus dados de login
login = "ricardo.aguiar@headsetbrasil.com"
senha = "250174"

try:
    # Abre a página de login do Zendesk
    driver.get("https://affixatendimento.zendesk.com/explore/portal#!/dashboards-library")

    # Encontrar e preencher o campo de e-mail
    email_field = driver.find_element(By.ID, "user_email")
    email_field.send_keys(login)

    # Encontrar e preencher o campo de senha
    password_field = driver.find_element(By.ID, "user_password")
    password_field.send_keys(senha)

    # Clicar no botão de login
    login_button = driver.find_element(By.NAME, "commit")
    login_button.click()

    # Aguarde até que a página esteja totalmente carregada
    WebDriverWait(driver, 10).until(EC.title_contains("Dashboard"))

    # Agora você pode realizar ações adicionais após o login, se necessário.

finally:
    # Encerra o navegador
    driver.quit()
