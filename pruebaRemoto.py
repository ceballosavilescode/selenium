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
    options.headless = True

    service = Service(executable_path=geckodriver_path)
    driver = webdriver.Firefox(service=service, options=options)

    try:
        print(f"🌍 Navegando a: {url}")
        driver.get(url)
        time.sleep(20)
	    
	# Intentar hacer clic en el botón de exportar con espera incremental
	wait_time = 10
	while True:
		try:
			wait = WebDriverWait(driver, wait_time)
			menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="export"]/span/span[2]')))
			menu_button.click()
			break  # Salir del bucle si el clic es exitoso
		except (TimeoutException, NoSuchElementException) as e:
			print(f"⚠️ Fallo al encontrar botón de exportar para - con espera de {wait_time}s. Error: {e}")
			wait_time += 10  # Aumentar espera en 10 segundos
			print(f"🔄 Reintentando con espera de {wait_time}s...")
			if wait_time > 20:  # Límite máximo de espera (por ejemplo, 20 segundos)
				print(f"❌ Tiempo máximo alcanzado para -. Marcando como Error.")
				raise TimeoutException("Tiempo máximo de espera alcanzado")

	time.sleep(2)

	# Intentar hacer clic en la opción "Como Excel" con espera incremental
	wait_time = 10
	while True:
		try:
			wait = WebDriverWait(driver, wait_time)
			opcion_excel = wait.until(EC.element_to_be_clickable((By.XPATH, '//p[normalize-space(text()) = "Como Excel"]')))
			opcion_excel.click()
			break  # Salir del bucle si el clic es exitoso
		except (TimeoutException, NoSuchElementException) as e:
			print(f"⚠️ Fallo al encontrar opción Excel para -- con espera de {wait_time}s. Error: {e}")
			wait_time += 10  # Aumentar espera en 10 segundos
			print(f"🔄 Reintentando con espera de --s...")
			if wait_time > 20:  # Límite máximo de espera (por ejemplo, 20 segundos)
				print(f"❌ Tiempo máximo alcanzado para --. Marcando como Error.")
				raise TimeoutException("Tiempo máximo de espera alcanzado")

