from pymavlink import mavutil
rate = 40

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
                print(msg['xacc'], msg['yacc'], msg['zacc'])

master = mavutil.mavlink_connection('/dev/ttyACM0', baud = 115200)
master.wait_heartbeat()

master.mav.request_data_stream_send(master.target_system, master.target_component, 1, rate, 1)
show_messages(master)
