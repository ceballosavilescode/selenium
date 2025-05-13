from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
	NoSuchElementException,
	TimeoutException
)
import time

def descargar_disponibilidad_devengos(variables):
	print("🌐 Iniciando automatización Selenium en modo headless para múltiples URLs...")
	print("🌐 Iniciando automatización Selenium en modo headless para múltiples URLs...")

	geckodriver_path = variables.get("geckodriver_path")
	if not geckodriver_path:
		raise ValueError("❌ Ruta del geckodriver no proporcionada.")

	# Lista de URLs directamente en el archivo
	urls = [
	"https://sb.sigfe.gob.cl/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/SIGFE2/Reportes/SB_CarteraFinancieraContable&pp=u=admin&nombre_cuenta=21522%20Cuentas%20por%20Pagar%20-%20Bienes%20y%20Servicios%20de%20Consumo;&TITLESUBTITULOREPORTE=2111014%20Dirección_Regional_Metropolitana&TITLETIPOMONEDAREPORTE=Nacional%20-%20Unidad&TITLETITULOREPORTE2=Reporte%20Relacionado%20-%20Variaci%C3%83%C2%B3n%20Patrimonial%20Cartera%20Financiera&mostrar_detalle=true&ejercicio=2025&page=flow.html%3F_flowId=viewReportFlow&cuenta_contable=21522&unidad_ejecutora=2111014&vista_cuenta=CUENTA_PRINCIPAL&site=SB&contenido=T&cant_saldo=2025-01-01&ambiente=SIGFE2&url=http%3A//sb.sigfe.gob.cl%3A80/sigfeReports/comun/popup/popupJasperReportRelacionado.jsp&fecha_desde=2025-01-01&codigo_moneda=CLP&nombre_contenido=Saldos%20o%20Flujos&proceso_funcionalidad=VACF&codigo_contab=00&TITLETITULOREPORTE=Cartera%20Financiera%20Contable&server=https%3A//sb.sigfe.gob.cl/jasperserver-pro/&reporte_link=ComparativoCompromiso_Relacionado&mostrar_filtros=true&expresion_valores=1&fecha_hasta=2025-12-31&nombre_vista=Cuenta/Principal&ambiente=SIGFE2&site=SB&standAlone=true&decorate=true&readOnly=true&userLocale=es",
	"https://sb.sigfe.gob.cl/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/SIGFE2/Reportes/SB_CarteraFinancieraContable&pp=u=admin&nombre_cuenta=21522%20Cuentas%20por%20Pagar%20-%20Bienes%20y%20Servicios%20de%20Consumo;&TITLESUBTITULOREPORTE=2111015%20Dirección_Regional_Arica_y_Parinacota&TITLETIPOMONEDAREPORTE=Nacional%20-%20Unidad&TITLETITULOREPORTE2=Reporte%20Relacionado%20-%20Variaci%C3%83%C2%B3n%20Patrimonial%20Cartera%20Financiera&mostrar_detalle=true&ejercicio=2025&page=flow.html%3F_flowId=viewReportFlow&cuenta_contable=21522&unidad_ejecutora=2111015&vista_cuenta=CUENTA_PRINCIPAL&site=SB&contenido=T&cant_saldo=2025-01-01&ambiente=SIGFE2&url=http%3A//sb.sigfe.gob.cl%3A80/sigfeReports/comun/popup/popupJasperReportRelacionado.jsp&fecha_desde=2025-01-01&codigo_moneda=CLP&nombre_contenido=Saldos%20o%20Flujos&proceso_funcionalidad=VACF&codigo_contab=00&TITLETITULOREPORTE=Cartera%20Financiera%20Contable&server=https%3A//sb.sigfe.gob.cl/jasperserver-pro/&reporte_link=ComparativoCompromiso_Relacionado&mostrar_filtros=true&expresion_valores=1&fecha_hasta=2025-12-31&nombre_vista=Cuenta/Principal&ambiente=SIGFE2&site=SB&standAlone=true&decorate=true&readOnly=true&userLocale=es",
	"https://sb.sigfe.gob.cl/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/SIGFE2/Reportes/SB_CarteraFinancieraContable&pp=u=admin&nombre_cuenta=21522%20Cuentas%20por%20Pagar%20-%20Bienes%20y%20Servicios%20de%20Consumo;&TITLESUBTITULOREPORTE=2111016%20Dirección_Regional_Los_Ríos&TITLETIPOMONEDAREPORTE=Nacional%20-%20Unidad&TITLETITULOREPORTE2=Reporte%20Relacionado%20-%20Variaci%C3%83%C2%B3n%20Patrimonial%20Cartera%20Financiera&mostrar_detalle=true&ejercicio=2025&page=flow.html%3F_flowId=viewReportFlow&cuenta_contable=21522&unidad_ejecutora=2111016&vista_cuenta=CUENTA_PRINCIPAL&site=SB&contenido=T&cant_saldo=2025-01-01&ambiente=SIGFE2&url=http%3A//sb.sigfe.gob.cl%3A80/sigfeReports/comun/popup/popupJasperReportRelacionado.jsp&fecha_desde=2025-01-01&codigo_moneda=CLP&nombre_contenido=Saldos%20o%20Flujos&proceso_funcionalidad=VACF&codigo_contab=00&TITLETITULOREPORTE=Cartera%20Financiera%20Contable&server=https%3A//sb.sigfe.gob.cl/jasperserver-pro/&reporte_link=ComparativoCompromiso_Relacionado&mostrar_filtros=true&expresion_valores=1&fecha_hasta=2025-12-31&nombre_vista=Cuenta/Principal&ambiente=SIGFE2&site=SB&standAlone=true&decorate=true&readOnly=true&userLocale=es",
	"https://sb.sigfe.gob.cl/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/SIGFE2/Reportes/SB_CarteraFinancieraContable&pp=u=admin&nombre_cuenta=21522%20Cuentas%20por%20Pagar%20-%20Bienes%20y%20Servicios%20de%20Consumo;&TITLESUBTITULOREPORTE=2111017%20Dirección_Regional_Ñuble&TITLETIPOMONEDAREPORTE=Nacional%20-%20Unidad&TITLETITULOREPORTE2=Reporte%20Relacionado%20-%20Variaci%C3%83%C2%B3n%20Patrimonial%20Cartera%20Financiera&mostrar_detalle=true&ejercicio=2025&page=flow.html%3F_flowId=viewReportFlow&cuenta_contable=21522&unidad_ejecutora=2111017&vista_cuenta=CUENTA_PRINCIPAL&site=SB&contenido=T&cant_saldo=2025-01-01&ambiente=SIGFE2&url=http%3A//sb.sigfe.gob.cl%3A80/sigfeReports/comun/popup/popupJasperReportRelacionado.jsp&fecha_desde=2025-01-01&codigo_moneda=CLP&nombre_contenido=Saldos%20o%20Flujos&proceso_funcionalidad=VACF&codigo_contab=00&TITLETITULOREPORTE=Cartera%20Financiera%20Contable&server=https%3A//sb.sigfe.gob.cl/jasperserver-pro/&reporte_link=ComparativoCompromiso_Relacionado&mostrar_filtros=true&expresion_valores=1&fecha_hasta=2025-12-31&nombre_vista=Cuenta/Principal&ambiente=SIGFE2&site=SB&standAlone=true&decorate=true&readOnly=true&userLocale=es",
			
	]

	# Configuración de Firefox sin cabeza
	# Configuración de Selenium
	firefox_options = Options()
	firefox_options.add_argument("-headless")
	firefox_options.set_preference("browser.download.folderList", 2)
	#firefox_options.set_preference("browser.download.dir", download_directory)
	firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk",
		"application/vnd.ms-excel,application/csv,text/csv,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
	firefox_options.set_preference("pdfjs.disabled", True)
	firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
	
	service = Service(executable_path=geckodriver_path)
	driver = webdriver.Firefox(service=service, options=firefox_options)

	try:
		for index, url in enumerate(urls, start=1):
			print(f"➡️ Procesando URL {index}: {url}")
			wait_time = 10
			while True:
				try:
					driver.get(url)
					wait = WebDriverWait(driver, wait_time)

					menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="export"]/span/span[2]')))
					menu_button.click()
					time.sleep(2)

					opcion_excel = wait.until(EC.element_to_be_clickable((
						By.XPATH, '//p[normalize-space(text()) = "Como Excel"]'
					)))
					opcion_excel.click()
					time.sleep(10)

					print(f"✅ Descarga completada desde URL {index}.")
					break

				except (TimeoutException, NoSuchElementException) as e:
					print(f"⚠️ Fallo en URL {index}, reintentando con espera {wait_time}s. Error: {e}")
					wait_time += 10
	finally:
		driver.quit()
		print("🧹 Navegador cerrado.")
