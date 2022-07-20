from pymavlink import mavutil
import enumm
rate = 40 #belli bir kivama kadar kulak memesi kıvamına kadar hzi bu kısımda arttırabilirsin ama bazi datalarda limit var

def show_messages(m):
    '''show incoming mavlink messages'''
    
    while True:
        msg = m.recv_match(blocking=True)
        if not msg:
            return
        if msg.get_type() == "BAD_DATA":
            if mavutil.all_printable(msg.data):
                sys.stdout.write(msg.data)
                sys.stdout.flush()
        else:
            msg = msg.to_dict()
            if (msg['mavpackettype'] == 'RAW_IMU'):
                #print(msg['xacc'], msg['yacc'], msg['zacc']) orjinalinde printliyorduk ki görelim doğru mu diye ara ara açarız diye biraktim
                enumm.altitude = (msg[''])
                enumm.imu_pitch = (msg['xgyro']) #----------------------------------Heading ve altitude'u halletmem lazım Batuhan -ykg
                enumm.imu_roll = (msg['yacc'])
                enumm.imu_yaw = (msg['zgyro'])
                enumm.ax = (msg['xacc'])/100
                enumm.ay = (msg['yacc'])/100
                enumm.az = (msg['zacc'])/100
                enumm.vx = enumm.ivx + ( (a/100) * time.time() )
                enumm.vy = enumm.ivy + ( (a/100) * time.time() )
                enumm.vz = enumm.ivz + ( (a/100) * time.time() )
            #if(msg['mavpackettype'] == 'VFR_HUD'): 
            #    print(msg['heading'])


master = mavutil.mavlink_connection('/dev/ttyACM0', baud = 115200)
master.wait_heartbeat()

master.mav.request_data_stream_send(master.target_system, master.target_component, 1, rate, 1)
show_messages(master)

