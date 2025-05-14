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
import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.common.exceptions import NoSuchElementException
import sys


def click_first_available(driver, wait, xpaths, delay_after_click=0):
	for xpath in xpaths:
		try:
			element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
			element.click()
			if delay_after_click > 0:
				time.sleep(delay_after_click)
			return True
		except TimeoutException:
			continue
	return False


def descargar_disponibilidad_devengos(variables):
	mensaje = "🌐 Ejecutando programa de automatización desarrollado por Héctor Ceballos..."
	print(mensaje, end='', flush=True)
	
	for _ in range(3):
	    for punto in ".  ..  ...  ".split():
	        sys.stdout.write('\r' + mensaje + punto)
	        sys.stdout.flush()
	        time.sleep(0.4)
	
	print("\n✅ Comenzando...")

	
	# Parámetros desde el diccionario
	geckodriver_path = variables.get("geckodriver_path")
	if not geckodriver_path:
		raise ValueError("❌ No se proporcionó la ruta al geckodriver.")


	# Lista de URLs directamente en el archivo
	urls = [
		"https://sb.sigfe.gob.cl/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/SIGFE2/Reportes/SB_CarteraFinancieraContable&pp=u=admin&nombre_cuenta=21522%20Cuentas%20por%20Pagar%20-%20Bienes%20y%20Servicios%20de%20Consumo;&TITLESUBTITULOREPORTE=2111001%20Dirección_Nacional&TITLETIPOMONEDAREPORTE=Nacional%20-%20Unidad&TITLETITULOREPORTE2=Reporte%20Relacionado%20-%20Variaci%C3%83%C2%B3n%20Patrimonial%20Cartera%20Financiera&mostrar_detalle=true&ejercicio=2025&page=flow.html%3F_flowId=viewReportFlow&cuenta_contable=21522&unidad_ejecutora=2111001&vista_cuenta=CUENTA_PRINCIPAL&site=SB&contenido=T&cant_saldo=2025-01-01&ambiente=SIGFE2&url=http%3A//sb.sigfe.gob.cl%3A80/sigfeReports/comun/popup/popupJasperReportRelacionado.jsp&fecha_desde=2025-01-01&codigo_moneda=CLP&nombre_contenido=Saldos%20o%20Flujos&proceso_funcionalidad=VACF&codigo_contab=00&TITLETITULOREPORTE=Cartera%20Financiera%20Contable&server=https%3A//sb.sigfe.gob.cl/jasperserver-pro/&reporte_link=ComparativoCompromiso_Relacionado&mostrar_filtros=true&expresion_valores=1&fecha_hasta=2025-12-31&nombre_vista=Cuenta/Principal&ambiente=SIGFE2&site=SB&standAlone=true&decorate=true&readOnly=true&userLocale=es",
		"https://sb.sigfe.gob.cl/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/SIGFE2/Reportes/SB_CarteraFinancieraContable&pp=u=admin&nombre_cuenta=21522%20Cuentas%20por%20Pagar%20-%20Bienes%20y%20Servicios%20de%20Consumo;&TITLESUBTITULOREPORTE=2111002%20Dirección_Regional_Tarapaca&TITLETIPOMONEDAREPORTE=Nacional%20-%20Unidad&TITLETITULOREPORTE2=Reporte%20Relacionado%20-%20Variaci%C3%83%C2%B3n%20Patrimonial%20Cartera%20Financiera&mostrar_detalle=true&ejercicio=2025&page=flow.html%3F_flowId=viewReportFlow&cuenta_contable=21522&unidad_ejecutora=2111002&vista_cuenta=CUENTA_PRINCIPAL&site=SB&contenido=T&cant_saldo=2025-01-01&ambiente=SIGFE2&url=http%3A//sb.sigfe.gob.cl%3A80/sigfeReports/comun/popup/popupJasperReportRelacionado.jsp&fecha_desde=2025-01-01&codigo_moneda=CLP&nombre_contenido=Saldos%20o%20Flujos&proceso_funcionalidad=VACF&codigo_contab=00&TITLETITULOREPORTE=Cartera%20Financiera%20Contable&server=https%3A//sb.sigfe.gob.cl/jasperserver-pro/&reporte_link=ComparativoCompromiso_Relacionado&mostrar_filtros=true&expresion_valores=1&fecha_hasta=2025-12-31&nombre_vista=Cuenta/Principal&ambiente=SIGFE2&site=SB&standAlone=true&decorate=true&readOnly=true&userLocale=es",
		"https://sb.sigfe.gob.cl/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/SIGFE2/Reportes/SB_CarteraFinancieraContable&pp=u=admin&nombre_cuenta=21522%20Cuentas%20por%20Pagar%20-%20Bienes%20y%20Servicios%20de%20Consumo;&TITLESUBTITULOREPORTE=2111003%20Dirección_Regional_Antofagasta&TITLETIPOMONEDAREPORTE=Nacional%20-%20Unidad&TITLETITULOREPORTE2=Reporte%20Relacionado%20-%20Variaci%C3%83%C2%B3n%20Patrimonial%20Cartera%20Financiera&mostrar_detalle=true&ejercicio=2025&page=flow.html%3F_flowId=viewReportFlow&cuenta_contable=21522&unidad_ejecutora=2111003&vista_cuenta=CUENTA_PRINCIPAL&site=SB&contenido=T&cant_saldo=2025-01-01&ambiente=SIGFE2&url=http%3A//sb.sigfe.gob.cl%3A80/sigfeReports/comun/popup/popupJasperReportRelacionado.jsp&fecha_desde=2025-01-01&codigo_moneda=CLP&nombre_contenido=Saldos%20o%20Flujos&proceso_funcionalidad=VACF&codigo_contab=00&TITLETITULOREPORTE=Cartera%20Financiera%20Contable&server=https%3A//sb.sigfe.gob.cl/jasperserver-pro/&reporte_link=ComparativoCompromiso_Relacionado&mostrar_filtros=true&expresion_valores=1&fecha_hasta=2025-12-31&nombre_vista=Cuenta/Principal&ambiente=SIGFE2&site=SB&standAlone=true&decorate=true&readOnly=true&userLocale=es",
		"https://sb.sigfe.gob.cl/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/SIGFE2/Reportes/SB_CarteraFinancieraContable&pp=u=admin&nombre_cuenta=21522%20Cuentas%20por%20Pagar%20-%20Bienes%20y%20Servicios%20de%20Consumo;&TITLESUBTITULOREPORTE=2111004%20Dirección_Regional_Atacama&TITLETIPOMONEDAREPORTE=Nacional%20-%20Unidad&TITLETITULOREPORTE2=Reporte%20Relacionado%20-%20Variaci%C3%83%C2%B3n%20Patrimonial%20Cartera%20Financiera&mostrar_detalle=true&ejercicio=2025&page=flow.html%3F_flowId=viewReportFlow&cuenta_contable=21522&unidad_ejecutora=2111004&vista_cuenta=CUENTA_PRINCIPAL&site=SB&contenido=T&cant_saldo=2025-01-01&ambiente=SIGFE2&url=http%3A//sb.sigfe.gob.cl%3A80/sigfeReports/comun/popup/popupJasperReportRelacionado.jsp&fecha_desde=2025-01-01&codigo_moneda=CLP&nombre_contenido=Saldos%20o%20Flujos&proceso_funcionalidad=VACF&codigo_contab=00&TITLETITULOREPORTE=Cartera%20Financiera%20Contable&server=https%3A//sb.sigfe.gob.cl/jasperserver-pro/&reporte_link=ComparativoCompromiso_Relacionado&mostrar_filtros=true&expresion_valores=1&fecha_hasta=2025-12-31&nombre_vista=Cuenta/Principal&ambiente=SIGFE2&site=SB&standAlone=true&decorate=true&readOnly=true&userLocale=es",
		"https://sb.sigfe.gob.cl/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/SIGFE2/Reportes/SB_CarteraFinancieraContable&pp=u=admin&nombre_cuenta=21522%20Cuentas%20por%20Pagar%20-%20Bienes%20y%20Servicios%20de%20Consumo;&TITLESUBTITULOREPORTE=2111005%20Dirección_Regional_Coquimbo&TITLETIPOMONEDAREPORTE=Nacional%20-%20Unidad&TITLETITULOREPORTE2=Reporte%20Relacionado%20-%20Variaci%C3%83%C2%B3n%20Patrimonial%20Cartera%20Financiera&mostrar_detalle=true&ejercicio=2025&page=flow.html%3F_flowId=viewReportFlow&cuenta_contable=21522&unidad_ejecutora=2111005&vista_cuenta=CUENTA_PRINCIPAL&site=SB&contenido=T&cant_saldo=2025-01-01&ambiente=SIGFE2&url=http%3A//sb.sigfe.gob.cl%3A80/sigfeReports/comun/popup/popupJasperReportRelacionado.jsp&fecha_desde=2025-01-01&codigo_moneda=CLP&nombre_contenido=Saldos%20o%20Flujos&proceso_funcionalidad=VACF&codigo_contab=00&TITLETITULOREPORTE=Cartera%20Financiera%20Contable&server=https%3A//sb.sigfe.gob.cl/jasperserver-pro/&reporte_link=ComparativoCompromiso_Relacionado&mostrar_filtros=true&expresion_valores=1&fecha_hasta=2025-12-31&nombre_vista=Cuenta/Principal&ambiente=SIGFE2&site=SB&standAlone=true&decorate=true&readOnly=true&userLocale=es",
		"https://sb.sigfe.gob.cl/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/SIGFE2/Reportes/SB_CarteraFinancieraContable&pp=u=admin&nombre_cuenta=21522%20Cuentas%20por%20Pagar%20-%20Bienes%20y%20Servicios%20de%20Consumo;&TITLESUBTITULOREPORTE=2111006%20Dirección_Regional_Valparaiso&TITLETIPOMONEDAREPORTE=Nacional%20-%20Unidad&TITLETITULOREPORTE2=Reporte%20Relacionado%20-%20Variaci%C3%83%C2%B3n%20Patrimonial%20Cartera%20Financiera&mostrar_detalle=true&ejercicio=2025&page=flow.html%3F_flowId=viewReportFlow&cuenta_contable=21522&unidad_ejecutora=2111006&vista_cuenta=CUENTA_PRINCIPAL&site=SB&contenido=T&cant_saldo=2025-01-01&ambiente=SIGFE2&url=http%3A//sb.sigfe.gob.cl%3A80/sigfeReports/comun/popup/popupJasperReportRelacionado.jsp&fecha_desde=2025-01-01&codigo_moneda=CLP&nombre_contenido=Saldos%20o%20Flujos&proceso_funcionalidad=VACF&codigo_contab=00&TITLETITULOREPORTE=Cartera%20Financiera%20Contable&server=https%3A//sb.sigfe.gob.cl/jasperserver-pro/&reporte_link=ComparativoCompromiso_Relacionado&mostrar_filtros=true&expresion_valores=1&fecha_hasta=2025-12-31&nombre_vista=Cuenta/Principal&ambiente=SIGFE2&site=SB&standAlone=true&decorate=true&readOnly=true&userLocale=es",
		"https://sb.sigfe.gob.cl/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/SIGFE2/Reportes/SB_CarteraFinancieraContable&pp=u=admin&nombre_cuenta=21522%20Cuentas%20por%20Pagar%20-%20Bienes%20y%20Servicios%20de%20Consumo;&TITLESUBTITULOREPORTE=2111007%20Dirección_Regional_Libertador_Bernardo_OHiggins&TITLETIPOMONEDAREPORTE=Nacional%20-%20Unidad&TITLETITULOREPORTE2=Reporte%20Relacionado%20-%20Variaci%C3%83%C2%B3n%20Patrimonial%20Cartera%20Financiera&mostrar_detalle=true&ejercicio=2025&page=flow.html%3F_flowId=viewReportFlow&cuenta_contable=21522&unidad_ejecutora=2111007&vista_cuenta=CUENTA_PRINCIPAL&site=SB&contenido=T&cant_saldo=2025-01-01&ambiente=SIGFE2&url=http%3A//sb.sigfe.gob.cl%3A80/sigfeReports/comun/popup/popupJasperReportRelacionado.jsp&fecha_desde=2025-01-01&codigo_moneda=CLP&nombre_contenido=Saldos%20o%20Flujos&proceso_funcionalidad=VACF&codigo_contab=00&TITLETITULOREPORTE=Cartera%20Financiera%20Contable&server=https%3A//sb.sigfe.gob.cl/jasperserver-pro/&reporte_link=ComparativoCompromiso_Relacionado&mostrar_filtros=true&expresion_valores=1&fecha_hasta=2025-12-31&nombre_vista=Cuenta/Principal&ambiente=SIGFE2&site=SB&standAlone=true&decorate=true&readOnly=true&userLocale=es",
		"https://sb.sigfe.gob.cl/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/SIGFE2/Reportes/SB_CarteraFinancieraContable&pp=u=admin&nombre_cuenta=21522%20Cuentas%20por%20Pagar%20-%20Bienes%20y%20Servicios%20de%20Consumo;&TITLESUBTITULOREPORTE=2111008%20Dirección_Regional_Del_Maule&TITLETIPOMONEDAREPORTE=Nacional%20-%20Unidad&TITLETITULOREPORTE2=Reporte%20Relacionado%20-%20Variaci%C3%83%C2%B3n%20Patrimonial%20Cartera%20Financiera&mostrar_detalle=true&ejercicio=2025&page=flow.html%3F_flowId=viewReportFlow&cuenta_contable=21522&unidad_ejecutora=2111008&vista_cuenta=CUENTA_PRINCIPAL&site=SB&contenido=T&cant_saldo=2025-01-01&ambiente=SIGFE2&url=http%3A//sb.sigfe.gob.cl%3A80/sigfeReports/comun/popup/popupJasperReportRelacionado.jsp&fecha_desde=2025-01-01&codigo_moneda=CLP&nombre_contenido=Saldos%20o%20Flujos&proceso_funcionalidad=VACF&codigo_contab=00&TITLETITULOREPORTE=Cartera%20Financiera%20Contable&server=https%3A//sb.sigfe.gob.cl/jasperserver-pro/&reporte_link=ComparativoCompromiso_Relacionado&mostrar_filtros=true&expresion_valores=1&fecha_hasta=2025-12-31&nombre_vista=Cuenta/Principal&ambiente=SIGFE2&site=SB&standAlone=true&decorate=true&readOnly=true&userLocale=es",
		"https://sb.sigfe.gob.cl/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/SIGFE2/Reportes/SB_CarteraFinancieraContable&pp=u=admin&nombre_cuenta=21522%20Cuentas%20por%20Pagar%20-%20Bienes%20y%20Servicios%20de%20Consumo;&TITLESUBTITULOREPORTE=2111009%20Dirección_Regional_Bio_Bio&TITLETIPOMONEDAREPORTE=Nacional%20-%20Unidad&TITLETITULOREPORTE2=Reporte%20Relacionado%20-%20Variaci%C3%83%C2%B3n%20Patrimonial%20Cartera%20Financiera&mostrar_detalle=true&ejercicio=2025&page=flow.html%3F_flowId=viewReportFlow&cuenta_contable=21522&unidad_ejecutora=2111009&vista_cuenta=CUENTA_PRINCIPAL&site=SB&contenido=T&cant_saldo=2025-01-01&ambiente=SIGFE2&url=http%3A//sb.sigfe.gob.cl%3A80/sigfeReports/comun/popup/popupJasperReportRelacionado.jsp&fecha_desde=2025-01-01&codigo_moneda=CLP&nombre_contenido=Saldos%20o%20Flujos&proceso_funcionalidad=VACF&codigo_contab=00&TITLETITULOREPORTE=Cartera%20Financiera%20Contable&server=https%3A//sb.sigfe.gob.cl/jasperserver-pro/&reporte_link=ComparativoCompromiso_Relacionado&mostrar_filtros=true&expresion_valores=1&fecha_hasta=2025-12-31&nombre_vista=Cuenta/Principal&ambiente=SIGFE2&site=SB&standAlone=true&decorate=true&readOnly=true&userLocale=es",
		"https://sb.sigfe.gob.cl/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/SIGFE2/Reportes/SB_CarteraFinancieraContable&pp=u=admin&nombre_cuenta=21522%20Cuentas%20por%20Pagar%20-%20Bienes%20y%20Servicios%20de%20Consumo;&TITLESUBTITULOREPORTE=2111010%20Dirección_Regional_Araucanía&TITLETIPOMONEDAREPORTE=Nacional%20-%20Unidad&TITLETITULOREPORTE2=Reporte%20Relacionado%20-%20Variaci%C3%83%C2%B3n%20Patrimonial%20Cartera%20Financiera&mostrar_detalle=true&ejercicio=2025&page=flow.html%3F_flowId=viewReportFlow&cuenta_contable=21522&unidad_ejecutora=2111010&vista_cuenta=CUENTA_PRINCIPAL&site=SB&contenido=T&cant_saldo=2025-01-01&ambiente=SIGFE2&url=http%3A//sb.sigfe.gob.cl%3A80/sigfeReports/comun/popup/popupJasperReportRelacionado.jsp&fecha_desde=2025-01-01&codigo_moneda=CLP&nombre_contenido=Saldos%20o%20Flujos&proceso_funcionalidad=VACF&codigo_contab=00&TITLETITULOREPORTE=Cartera%20Financiera%20Contable&server=https%3A//sb.sigfe.gob.cl/jasperserver-pro/&reporte_link=ComparativoCompromiso_Relacionado&mostrar_filtros=true&expresion_valores=1&fecha_hasta=2025-12-31&nombre_vista=Cuenta/Principal&ambiente=SIGFE2&site=SB&standAlone=true&decorate=true&readOnly=true&userLocale=es",
		"https://sb.sigfe.gob.cl/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/SIGFE2/Reportes/SB_CarteraFinancieraContable&pp=u=admin&nombre_cuenta=21522%20Cuentas%20por%20Pagar%20-%20Bienes%20y%20Servicios%20de%20Consumo;&TITLESUBTITULOREPORTE=2111011%20Dirección_Regional_Los_Lagos&TITLETIPOMONEDAREPORTE=Nacional%20-%20Unidad&TITLETITULOREPORTE2=Reporte%20Relacionado%20-%20Variaci%C3%83%C2%B3n%20Patrimonial%20Cartera%20Financiera&mostrar_detalle=true&ejercicio=2025&page=flow.html%3F_flowId=viewReportFlow&cuenta_contable=21522&unidad_ejecutora=2111011&vista_cuenta=CUENTA_PRINCIPAL&site=SB&contenido=T&cant_saldo=2025-01-01&ambiente=SIGFE2&url=http%3A//sb.sigfe.gob.cl%3A80/sigfeReports/comun/popup/popupJasperReportRelacionado.jsp&fecha_desde=2025-01-01&codigo_moneda=CLP&nombre_contenido=Saldos%20o%20Flujos&proceso_funcionalidad=VACF&codigo_contab=00&TITLETITULOREPORTE=Cartera%20Financiera%20Contable&server=https%3A//sb.sigfe.gob.cl/jasperserver-pro/&reporte_link=ComparativoCompromiso_Relacionado&mostrar_filtros=true&expresion_valores=1&fecha_hasta=2025-12-31&nombre_vista=Cuenta/Principal&ambiente=SIGFE2&site=SB&standAlone=true&decorate=true&readOnly=true&userLocale=es",
		"https://sb.sigfe.gob.cl/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/SIGFE2/Reportes/SB_CarteraFinancieraContable&pp=u=admin&nombre_cuenta=21522%20Cuentas%20por%20Pagar%20-%20Bienes%20y%20Servicios%20de%20Consumo;&TITLESUBTITULOREPORTE=2111012%20Dirección_Regional_Aysén&TITLETIPOMONEDAREPORTE=Nacional%20-%20Unidad&TITLETITULOREPORTE2=Reporte%20Relacionado%20-%20Variaci%C3%83%C2%B3n%20Patrimonial%20Cartera%20Financiera&mostrar_detalle=true&ejercicio=2025&page=flow.html%3F_flowId=viewReportFlow&cuenta_contable=21522&unidad_ejecutora=2111012&vista_cuenta=CUENTA_PRINCIPAL&site=SB&contenido=T&cant_saldo=2025-01-01&ambiente=SIGFE2&url=http%3A//sb.sigfe.gob.cl%3A80/sigfeReports/comun/popup/popupJasperReportRelacionado.jsp&fecha_desde=2025-01-01&codigo_moneda=CLP&nombre_contenido=Saldos%20o%20Flujos&proceso_funcionalidad=VACF&codigo_contab=00&TITLETITULOREPORTE=Cartera%20Financiera%20Contable&server=https%3A//sb.sigfe.gob.cl/jasperserver-pro/&reporte_link=ComparativoCompromiso_Relacionado&mostrar_filtros=true&expresion_valores=1&fecha_hasta=2025-12-31&nombre_vista=Cuenta/Principal&ambiente=SIGFE2&site=SB&standAlone=true&decorate=true&readOnly=true&userLocale=es",
		"https://sb.sigfe.gob.cl/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/SIGFE2/Reportes/SB_CarteraFinancieraContable&pp=u=admin&nombre_cuenta=21522%20Cuentas%20por%20Pagar%20-%20Bienes%20y%20Servicios%20de%20Consumo;&TITLESUBTITULOREPORTE=2111013%20Dirección_Regional_Magallanes&TITLETIPOMONEDAREPORTE=Nacional%20-%20Unidad&TITLETITULOREPORTE2=Reporte%20Relacionado%20-%20Variaci%C3%83%C2%B3n%20Patrimonial%20Cartera%20Financiera&mostrar_detalle=true&ejercicio=2025&page=flow.html%3F_flowId=viewReportFlow&cuenta_contable=21522&unidad_ejecutora=2111013&vista_cuenta=CUENTA_PRINCIPAL&site=SB&contenido=T&cant_saldo=2025-01-01&ambiente=SIGFE2&url=http%3A//sb.sigfe.gob.cl%3A80/sigfeReports/comun/popup/popupJasperReportRelacionado.jsp&fecha_desde=2025-01-01&codigo_moneda=CLP&nombre_contenido=Saldos%20o%20Flujos&proceso_funcionalidad=VACF&codigo_contab=00&TITLETITULOREPORTE=Cartera%20Financiera%20Contable&server=https%3A//sb.sigfe.gob.cl/jasperserver-pro/&reporte_link=ComparativoCompromiso_Relacionado&mostrar_filtros=true&expresion_valores=1&fecha_hasta=2025-12-31&nombre_vista=Cuenta/Principal&ambiente=SIGFE2&site=SB&standAlone=true&decorate=true&readOnly=true&userLocale=es",
		"https://sb.sigfe.gob.cl/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/SIGFE2/Reportes/SB_CarteraFinancieraContable&pp=u=admin&nombre_cuenta=21522%20Cuentas%20por%20Pagar%20-%20Bienes%20y%20Servicios%20de%20Consumo;&TITLESUBTITULOREPORTE=2111014%20Dirección_Regional_Metropolitana&TITLETIPOMONEDAREPORTE=Nacional%20-%20Unidad&TITLETITULOREPORTE2=Reporte%20Relacionado%20-%20Variaci%C3%83%C2%B3n%20Patrimonial%20Cartera%20Financiera&mostrar_detalle=true&ejercicio=2025&page=flow.html%3F_flowId=viewReportFlow&cuenta_contable=21522&unidad_ejecutora=2111014&vista_cuenta=CUENTA_PRINCIPAL&site=SB&contenido=T&cant_saldo=2025-01-01&ambiente=SIGFE2&url=http%3A//sb.sigfe.gob.cl%3A80/sigfeReports/comun/popup/popupJasperReportRelacionado.jsp&fecha_desde=2025-01-01&codigo_moneda=CLP&nombre_contenido=Saldos%20o%20Flujos&proceso_funcionalidad=VACF&codigo_contab=00&TITLETITULOREPORTE=Cartera%20Financiera%20Contable&server=https%3A//sb.sigfe.gob.cl/jasperserver-pro/&reporte_link=ComparativoCompromiso_Relacionado&mostrar_filtros=true&expresion_valores=1&fecha_hasta=2025-12-31&nombre_vista=Cuenta/Principal&ambiente=SIGFE2&site=SB&standAlone=true&decorate=true&readOnly=true&userLocale=es",
		"https://sb.sigfe.gob.cl/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/SIGFE2/Reportes/SB_CarteraFinancieraContable&pp=u=admin&nombre_cuenta=21522%20Cuentas%20por%20Pagar%20-%20Bienes%20y%20Servicios%20de%20Consumo;&TITLESUBTITULOREPORTE=2111015%20Dirección_Regional_Arica_y_Parinacota&TITLETIPOMONEDAREPORTE=Nacional%20-%20Unidad&TITLETITULOREPORTE2=Reporte%20Relacionado%20-%20Variaci%C3%83%C2%B3n%20Patrimonial%20Cartera%20Financiera&mostrar_detalle=true&ejercicio=2025&page=flow.html%3F_flowId=viewReportFlow&cuenta_contable=21522&unidad_ejecutora=2111015&vista_cuenta=CUENTA_PRINCIPAL&site=SB&contenido=T&cant_saldo=2025-01-01&ambiente=SIGFE2&url=http%3A//sb.sigfe.gob.cl%3A80/sigfeReports/comun/popup/popupJasperReportRelacionado.jsp&fecha_desde=2025-01-01&codigo_moneda=CLP&nombre_contenido=Saldos%20o%20Flujos&proceso_funcionalidad=VACF&codigo_contab=00&TITLETITULOREPORTE=Cartera%20Financiera%20Contable&server=https%3A//sb.sigfe.gob.cl/jasperserver-pro/&reporte_link=ComparativoCompromiso_Relacionado&mostrar_filtros=true&expresion_valores=1&fecha_hasta=2025-12-31&nombre_vista=Cuenta/Principal&ambiente=SIGFE2&site=SB&standAlone=true&decorate=true&readOnly=true&userLocale=es",
		"https://sb.sigfe.gob.cl/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/SIGFE2/Reportes/SB_CarteraFinancieraContable&pp=u=admin&nombre_cuenta=21522%20Cuentas%20por%20Pagar%20-%20Bienes%20y%20Servicios%20de%20Consumo;&TITLESUBTITULOREPORTE=2111016%20Dirección_Regional_Los_Ríos&TITLETIPOMONEDAREPORTE=Nacional%20-%20Unidad&TITLETITULOREPORTE2=Reporte%20Relacionado%20-%20Variaci%C3%83%C2%B3n%20Patrimonial%20Cartera%20Financiera&mostrar_detalle=true&ejercicio=2025&page=flow.html%3F_flowId=viewReportFlow&cuenta_contable=21522&unidad_ejecutora=2111016&vista_cuenta=CUENTA_PRINCIPAL&site=SB&contenido=T&cant_saldo=2025-01-01&ambiente=SIGFE2&url=http%3A//sb.sigfe.gob.cl%3A80/sigfeReports/comun/popup/popupJasperReportRelacionado.jsp&fecha_desde=2025-01-01&codigo_moneda=CLP&nombre_contenido=Saldos%20o%20Flujos&proceso_funcionalidad=VACF&codigo_contab=00&TITLETITULOREPORTE=Cartera%20Financiera%20Contable&server=https%3A//sb.sigfe.gob.cl/jasperserver-pro/&reporte_link=ComparativoCompromiso_Relacionado&mostrar_filtros=true&expresion_valores=1&fecha_hasta=2025-12-31&nombre_vista=Cuenta/Principal&ambiente=SIGFE2&site=SB&standAlone=true&decorate=true&readOnly=true&userLocale=es",
		"https://sb.sigfe.gob.cl/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/SIGFE2/Reportes/SB_CarteraFinancieraContable&pp=u=admin&nombre_cuenta=21522%20Cuentas%20por%20Pagar%20-%20Bienes%20y%20Servicios%20de%20Consumo;&TITLESUBTITULOREPORTE=2111017%20Dirección_Regional_Ñuble&TITLETIPOMONEDAREPORTE=Nacional%20-%20Unidad&TITLETITULOREPORTE2=Reporte%20Relacionado%20-%20Variaci%C3%83%C2%B3n%20Patrimonial%20Cartera%20Financiera&mostrar_detalle=true&ejercicio=2025&page=flow.html%3F_flowId=viewReportFlow&cuenta_contable=21522&unidad_ejecutora=2111017&vista_cuenta=CUENTA_PRINCIPAL&site=SB&contenido=T&cant_saldo=2025-01-01&ambiente=SIGFE2&url=http%3A//sb.sigfe.gob.cl%3A80/sigfeReports/comun/popup/popupJasperReportRelacionado.jsp&fecha_desde=2025-01-01&codigo_moneda=CLP&nombre_contenido=Saldos%20o%20Flujos&proceso_funcionalidad=VACF&codigo_contab=00&TITLETITULOREPORTE=Cartera%20Financiera%20Contable&server=https%3A//sb.sigfe.gob.cl/jasperserver-pro/&reporte_link=ComparativoCompromiso_Relacionado&mostrar_filtros=true&expresion_valores=1&fecha_hasta=2025-12-31&nombre_vista=Cuenta/Principal&ambiente=SIGFE2&site=SB&standAlone=true&decorate=true&readOnly=true&userLocale=es",
	]

	# Configuración de Selenium
	firefox_options = Options()
	firefox_options.add_argument("-headless")  # opcional para modo sin ventana
	firefox_options.set_preference("browser.download.folderList", 2)
	# firefox_options.set_preference("browser.download.dir", download_directory)
	firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk",
		"application/vnd.ms-excel,application/csv,text/csv,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
	firefox_options.set_preference("pdfjs.disabled", True)
	firefox_options.set_preference("browser.download.manager.showWhenStarting", False)

	service = Service(executable_path=geckodriver_path)
	driver = webdriver.Firefox(service=service, options=firefox_options)

	try:
		for index, url in enumerate(urls, start=1):
			print(f"\n🌐 Procesando URL {index}: {url}")
			try:
				driver.get(url)
				wait = WebDriverWait(driver, 15)

				export_xpaths = [
					'//*[@id="export"]/span/span[2]',
					'//*[@id="menuList_simpleAction_36"]/p'
				]

				if not click_first_available(driver, wait, export_xpaths, delay_after_click=4):
					print("⚠️ No se encontró ningún botón de exportar. Saltando esta URL.")
					continue

				try:
					opcion_excel = wait.until(EC.element_to_be_clickable((
						By.XPATH, '//p[normalize-space(text()) = "Como Excel"]'
					)))
					opcion_excel.click()
					print("📥 Opción 'Como Excel' seleccionada exitosamente.")
					time.sleep(6)
				except TimeoutException:
					print("⚠️ No se encontró la opción 'Como Excel'. Saltando esta URL.")
					continue

			except (TimeoutException, WebDriverException, NoSuchElementException) as e:
				print(f"❌ Error al procesar la URL {index}: {e}")

	finally:
		driver.quit()
		print("\n🔒 Navegador cerrado. Proceso finalizado.")
		sys.exit()

variables = {
	'user': 'yo',
	'password': '456',
	'usuario_pc': 'yo',
	'geckodriver_path': os.path.join(os.path.dirname(__file__), 'webdriver', 'geckodriver.exe'),
	'url': 'https://sb.sigfe.gob.cl/jasperserver-pro/flow.html?...'  # URL real aquí
}

if __name__ == '__main__':
	descargar_disponibilidad_devengos(variables)
