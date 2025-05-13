from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    WebDriverException
)
import time

def descargar_disponibilidad_devengos(variables):
    print("🌐 Automatización con Selenium iniciada en modo headless...")

    url = variables.get("url", "https://example.com")
    geckodriver_path = variables.get("geckodriver_path")

    if not geckodriver_path:
        raise ValueError("❌ Ruta del geckodriver no proporcionada.")

    # Configurar Firefox sin cabeza
    options = Options()
    options.headless = True  # ← modo sin interfaz gráfica

    service = Service(executable_path=geckodriver_path)
    driver = webdriver.Firefox(service=service, options=options)

    wait_time = 10
    try:
        while True:
            try:
                driver.get(url)
                wait = WebDriverWait(driver, wait_time)

                # Esperar y hacer clic en el botón de menú
                menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="export"]/span/span[2]')))
                menu_button.click()
                time.sleep(2)

                # Esperar y hacer clic en "Como Excel"
                opcion_excel = wait.until(EC.element_to_be_clickable((By.XPATH, '//p[normalize-space(text()) = "Como Excel"]')))
                opcion_excel.click()
                time.sleep(10)

                print("✅ Archivo descargado correctamente.")
                break  # Salir del bucle si todo fue exitoso

            except (TimeoutException, NoSuchElementException) as e:
                print(f"⚠️ Reintentando (espera de {wait_time}s). Error: {e}")
                wait_time += 10
    finally:
        driver.quit()
        print("🧹 Firefox cerrado.")
