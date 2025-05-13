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

def descargar_disponibilidad_devengos():
	columna_estado = 'descarga_cartera_financiera_contable'
	download_directory = os.path.join(os.getcwd(), 'input_excel', 'cartera_financiera_contable')
	os.makedirs(download_directory, exist_ok=True)

	# Detectar si se está ejecutando como .exe (PyInstaller) o script normal
	if getattr(sys, 'frozen', False):
		base_path = sys._MEIPASS  # Carpeta temporal donde PyInstaller extrae recursos
	else:
		base_path = os.path.dirname(os.path.abspath(__file__))


	#geckodriver_path = 'C:/Users/Hector/Downloads/cobranzas/webdriver/geckodriver.exe'
	geckodriver_path = os.path.join(base_path, 'webdriver', 'geckodriver.exe')



	firefox_options = Options()
	#firefox_options.add_argument("-headless")
	firefox_options.set_preference("browser.download.folderList", 2)
	firefox_options.set_preference("browser.download.dir", download_directory)
	firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk",
		"application/vnd.ms-excel,application/csv,text/csv,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
	firefox_options.set_preference("pdfjs.disabled", True)
	firefox_options.set_preference("browser.download.manager.showWhenStarting", False)

	service = Service(executable_path=geckodriver_path)
	driver = webdriver.Firefox(service=service, options=firefox_options)

	driver.get("https://sb.sigfe.gob.cl/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/SIGFE2/Reportes/SB_CarteraFinancieraContable&pp=u=admin&nombre_cuenta=21522%20Cuentas%20por%20Pagar%20-%20Bienes%20y%20Servicios%20de%20Consumo;&TITLESUBTITULOREPORTE=2111017%20Dirección_Regional_Ñuble&TITLETIPOMONEDAREPORTE=Nacional%20-%20Unidad&TITLETITULOREPORTE2=Reporte%20Relacionado%20-%20Variaci%C3%83%C2%B3n%20Patrimonial%20Cartera%20Financiera&mostrar_detalle=true&ejercicio=2025&page=flow.html%3F_flowId=viewReportFlow&cuenta_contable=21522&unidad_ejecutora=2111017&vista_cuenta=CUENTA_PRINCIPAL&site=SB&contenido=T&cant_saldo=2025-01-01&ambiente=SIGFE2&url=http%3A//sb.sigfe.gob.cl%3A80/sigfeReports/comun/popup/popupJasperReportRelacionado.jsp&fecha_desde=2025-01-01&codigo_moneda=CLP&nombre_contenido=Saldos%20o%20Flujos&proceso_funcionalidad=VACF&codigo_contab=00&TITLETITULOREPORTE=Cartera%20Financiera%20Contable&server=https%3A//sb.sigfe.gob.cl/jasperserver-pro/&reporte_link=ComparativoCompromiso_Relacionado&mostrar_filtros=true&expresion_valores=1&fecha_hasta=2025-12-31&nombre_vista=Cuenta/Principal&ambiente=SIGFE2&site=SB&standAlone=true&decorate=true&readOnly=true&userLocale=es")
	time.sleep(10)

if __name__ == "__main__":
	descargar_disponibilidad_devengos()
