from pymavlink import mavutil
import time
from threading import Thread
master = mavutil.mavlink_connection('/dev/ttyACM0',baud=115200)

hiz = 0
def get_imu_data():

	while True:
	    msg = master.recv_match()
	    if not msg:
	        continue
	    if msg.get_type() == 'RAW_IMU':
	    	data = str(msg)
	    	try:
	    		global hiz
	    		ilk_zaman = 0			
	    		son_zaman = time.time()
		    	data = data.split(":")
		    	xacc = data[2].split(",")[0]
		    	yacc = data[3].split(",")[0]
		    	zacc = data[4].split(",")[0]
		    	print(xacc * (son_zaman-ilk_zaman))
		    	ilk_zaman = son_zaman
	    	except:	    	
	    		print("RAW_IMU Data: ",xacc,yacc,zacc)
	    		#print(hiz)
	    	
	    	
	    	
	    	
get_imu_data()	    	

	
