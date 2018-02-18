import serial
import headers

# Initialize the data
data = {
	headers.temp_SensID:0,
	headers.acst_SensID:0,
	headers.lgth_SensID:0,	
	headers.accl_SensID:0
}

while True:
#for i in range(10):
	# Read the data from the XDK
	port = serial.Serial("/dev/ttyACM0", 9600, timeout=1.0)
	
	serial_data = port.readlines()
	print("Data received.", serial_data)
	#serial_data = "[Light sensor #20000]"
	
	# Filter the data and add it to the dictionary
	if serial_data != []:
		print("Processing data...")
		for msg in serial_data:
			if headers.temp_SensID in msg:
				from_idx = msg.index("#")
				data[headers.temp_SensID] = int(msg[from_idx+1:])
		
			elif headers.acst_SensID in msg:
				from_idx = msg.index("#")
				data[headers.acst_SensID] = int(msg[from_idx+1:])
		
			elif headers.lgth_SensID in msg:
				from_idx = msg.index("#")
				data[headers.lgth_SensID] = int(msg[from_idx+1:])
				
			elif headers.accl_SensID in msg:
				from_idx = msg.index("#")
				data[headers.accl_SensID] = int(msg[from_idx+1:])
		
			else:
				pass
		
		# Write the values to a external file
		print("Exporting data...")
		with open(headers.external_file, "w") as f:
			f.write(str(data))
				
		print("Done.\n")
	
	else:
		print("Invalid data.")
	
	
