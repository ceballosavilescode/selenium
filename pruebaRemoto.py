import os
import time
import sqlite3
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
	NoSuchElementException,
	TimeoutException,
	WebDriverException
)
import sys
from selenium.webdriver.firefox.service import Service
service = Service(executable_path=variables['geckodriver_path'])

def descargar_disponibilidad_devengos(variables):
    print("🌐 Automatización con Selenium iniciada...")

from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import time

def descargar_disponibilidad_devengos(variables):
    options = Options()
    options.headless = True

    geckodriver_path = variables.get("geckodriver_path")
    if not geckodriver_path:
        raise ValueError("❌ No se proporcionó la ruta del geckodriver.")

    service = Service(executable_path=geckodriver_path)
    driver = webdriver.Firefox(service=service, options=options)

    try:
        driver.get(variables.get("url", "https://www.google.com/"))
        time.sleep(2)
        driver.save_screenshot("pantalla.png")
        print("✅ Screenshot guardado como pantalla.png")
    finally:
        driver.quit()


if __name__ == "__main__":
	descargar_disponibilidad_devengos()
