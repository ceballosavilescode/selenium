from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time
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

def descargar_disponibilidad_devengos(variables):
	print("🌐 Automatización con Selenium iniciada...")

	# Parámetros desde el diccionario
	url = variables.get("url", "https://example.com")
	geckodriver_path = variables.get("geckodriver_path")

	if not geckodriver_path:
		raise ValueError("❌ No se proporcionó la ruta al geckodriver.")

	# Configuración de Selenium
	options = Options()
	options.headless = True  # ← EJECUCIÓN SIN CABEZA

	# Crear servicio y driver
	service = Service(executable_path=geckodriver_path)
	driver = webdriver.Firefox(service=service, options=options)
	print(f"✅ descargado correctamente!.")

	print(f"🌍 Navegando a: {url}")
	driver.get(url)
	
	wait_time = 10
	while True:
		try:
			wait = WebDriverWait(driver, wait_time)
			menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="export"]/span/span[2]')))
			menu_button.click()
			time.sleep(2)
			opcion_excel = wait.until(EC.element_to_be_clickable((
				By.XPATH, '//p[normalize-space(text()) = "Como Excel"]'
			)))
			opcion_excel.click()
			time.sleep(10)

			
			break  # Salir del bucle si el clic es exitoso
		except (TimeoutException, NoSuchElementException) as e:
			print(f"⚠️ Fallo al encontrar botón de exportar para -- con espera de {wait_time}s. Error: {e}")
			wait_time += 10  # Aumentar espera en 10 segundos
	print(f"✅ descargado correctamente.")
