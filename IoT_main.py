############################# Init actions
import triggers
import headers
import random
import reports
from firebase import firebase
from datetime import datetime

audio_edge = triggers.Edge(False)
tempt_edge = triggers.Edge(False)
light_edge = triggers.Edge(False)
acclt_edge = triggers.Edge(False)

print("Running...\n")

while True:
	############################# LECTURA DE DATOS #############################

	# Get sensor values
	keep_trying = True
	with open(headers.external_file, "r") as f:
		while keep_trying:
			try:
				sensor_data_dict = eval(f.readline())
				keep_trying = False
			except:
				pass
	
	
	############################# DIAGNOSTICO #############################

	TEMPT_Threshold = 29000
	AUDIO_Threshold = 100000
	LIGHT_Threshold = 3400	#Dark limit of civil twilight under a clear sky

	ACCLT_Offset = 500	

	report_status = {
		"Tempt":False,
		"Audio":False,
		"Light":False,
		"Acclt":False
	}

	# Set the flag to true if the value change
	report = TEMPT_Threshold < sensor_data_dict[headers.temp_SensID]

	if True == tempt_edge.rise( report ):
		report_status["Tempt"] = True	
	
	report = AUDIO_Threshold < sensor_data_dict[headers.acst_SensID]
	
	if True == audio_edge.rise( report ):
		report_status["Audio"] = True
	
	report = LIGHT_Threshold > sensor_data_dict[headers.lgth_SensID]

	if True == light_edge.rise( report ):
		report_status["Light"] = True
		
	report = ACCLT_Offset < abs( sensor_data_dict[headers.accl_SensID] - 1000 )

	if True == acclt_edge.rise( report ):
		print()
		report_status["Acclt"] = True


	############################# EMPAQUE #############################

	LatInf = 20.63
	LatSup = 20.69
	LonInf = -103.41
	LonSup = -103.28

	data_Report = []

	# Check if the report status is TRUE to send a report
	if True == report_status["Tempt"]:
		data = reports.template()
		if 0 == random.randint(0,1):
			data["autor"] = "IoT"
			data["titulo"] = "Registro de temperatura muy alto."
			data["descripcion"] = "Posible incendio en el bosque."
			data["likes"] = 0
			data["categoria"] = "Medio ambiente"
			data["latitud"] = random.uniform(LatInf, LatSup)
			data["longitud"] = random.uniform(LonInf, LonSup)
		else:
			data["autor"] = "IoT"
			data["titulo"] = "Registro de temperatura muy alto."
			data["descripcion"] = "Posible incendio urbano."
			data["likes"] = 0
			data["categoria"] = "Seguridad"
			data["latitud"] = random.uniform(LatInf, LatSup)
			data["longitud"] = random.uniform(LonInf, LonSup)
	
		data_Report.append(data)
	
	if True == report_status["Audio"]:
		data = reports.template()
		if 0 == random.randint(0,1):		
			data["autor"] = "IoT"
			data["titulo"] = "Registro de sonido muy alto."
			data["descripcion"] = "Posible asalto."
			data["likes"] = 0
			data["categoria"] = "Seguridad"
			data["latitud"] = random.uniform(LatInf, LatSup)
			data["longitud"] = random.uniform(LonInf, LonSup)
		else:
			data["autor"] = "IoT"
			data["titulo"] = "Registro de sonido muy alto."
			data["descripcion"] = "Posible choque."
			data["likes"] = 0
			data["categoria"] = "Movilidad"
			data["latitud"] = random.uniform(LatInf, LatSup)
			data["longitud"] = random.uniform(LonInf, LonSup)		
	
		data_Report.append(data)
	
	if True == report_status["Light"]:
		data = reports.template()
		if 0 == random.randint(0,1):
			data["autor"] = "IoT"
			data["titulo"] = "Registro de irregularidad en la iluminacion."
			data["descripcion"] = "Posible falla en faro."
			data["likes"] = 0
			data["categoria"] = "Movilidad"
			data["latitud"] = random.uniform(LatInf, LatSup)
			data["longitud"] = random.uniform(LonInf, LonSup)
		else:
			data["autor"] = "IoT"
			data["titulo"] = "Registro de irregularidad en la iluminacion."
			data["descripcion"] = "Apagon en toda la zona."
			data["likes"] = 0
			data["categoria"] = "Seguridad"
			data["latitud"] = random.uniform(LatInf, LatSup)
			data["longitud"] = random.uniform(LonInf, LonSup)	
	
		data_Report.append(data)
		
	if True == report_status["Acclt"]:
		data = reports.template()
		if 0 == random.randint(0,1):
			data["autor"] = "IoT"
			data["titulo"] = "Registro de movimiento intenso."
			data["descripcion"] = "Movimiento abrupto de la unidad."
			data["likes"] = 0
			data["categoria"] = "Seguridad"
			data["latitud"] = random.uniform(LatInf, LatSup)
			data["longitud"] = random.uniform(LonInf, LonSup)
		else:
			data["autor"] = "IoT"
			data["titulo"] = "Registro de movimiento intenso."
			data["descripcion"] = "Evento importante de seguridad en la zona."
			data["likes"] = 0
			data["categoria"] = "Seguridad"
			data["latitud"] = random.uniform(LatInf, LatSup)
			data["longitud"] = random.uniform(LonInf, LonSup)	
	
		data_Report.append(data)


	############################# MANDAR #############################
	fb_api = firebase.FirebaseApplication('https://hackaton-e3768.firebaseio.com', None)
	
	for report in data_Report:
		fb_api.post('/Reporte', report)
		with open("dummy_report", "a") as f:
			f.write(str(report))
			f.write("\n")
		print(str(datetime.now()) + " - REPORT_SENT: " + report["titulo"])

