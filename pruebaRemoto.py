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
        driver.save_screenshot("pantalla.png")
        print("✅ Screenshot guardado como 'pantalla.png'")
    finally:
        driver.quit()
        print("🧹 Sesión de navegador cerrada.")
