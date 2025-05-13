from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time

def descargar_disponibilidad_devengos(variables):
    print("🌐 Automatización con Selenium iniciada...")

    # Parámetros desde el diccionario
    url = variables.get("url", "https://example.com")
    geckodriver_path = variables.get("geckodriver_path")

    if not geckodriver_path:
        raise ValueError("❌ No se proporcionó la ruta al geckodriver.")

    # Configuración de Selenium
    options = Options()
    options.headless = True

    service = Service(executable_path=geckodriver_path)
    driver = webdriver.Firefox(service=service, options=options)

    try:
        print(f"🌍 Navegando a: {url}")
        driver.get(url)
        time.sleep(20)
        # Intentar hacer clic en la opción "Como Excel" con espera incremental
        wait_time = 10
        while True:
            try:
                wait = WebDriverWait(driver, wait_time)
                opcion_excel = wait.until(EC.element_to_be_clickable((By.XPATH, '//p[normalize-space(text()) = "Como Excel"]')))
                opcion_excel.click()
                break  # Salir del bucle si el clic es exitoso
            except (TimeoutException, NoSuchElementException) as e:
                print(f"⚠️ Fallo al encontrar opción Excel para {cod_institucion} con espera de {wait_time}s. Error: {e}")
        time.sleep(20)

        
        print("FINALIZADO")
    finally:
        driver.quit()
        print("🧹 Sesión de navegador cerrada.")
