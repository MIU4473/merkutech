from pymavlink import mavutil

# Bağlantı kurma
master = mavutil.mavlink_connection('udp:127.0.0.1:14550')

# Gyro kalibrasyon komutu gönderme
def send_calibration_command():
    master.mav.command_long_send(
        master.target_system,  # Sistem ID'si
        master.target_component,  # Component ID'si
        mavutil.mavlink.MAV_CMD_PREFLIGHT_CALIBRATION,  # Kalibrasyon komutu
        0,  # Parametre 1 (0: Gyro kalibrasyonu için)
        0,  # Parametre 2
        0,  # Parametre 3
        0,  # Parametre 4
        0,  # Parametre 5
        0,  # Parametre 6
        0   # Parametre 7
    )

# Kalibrasyon komutunu gönder
send_calibration_command()
