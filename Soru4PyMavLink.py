from pymavlink import mavutil
import time

# Bağlantı kurma (SITL kullanımı örneği)
master = mavutil.mavlink_connection('tcp:127.0.0.1:5760')

# Hedef konumu belirleme
target_location = (float(-35.363261), float(149.165230), float(20))  # Örnek bir hedef konumu

# Konuma git fonksiyonu
def go_to_location(target):
    msg = master.mav.mission_item_send(
        master.target_system, master.target_component,
        0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
        mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 2, 0, 0, 0,
        target[0], target[1], target[2]
    )

# Drone'u hedef konuma götür
go_to_location(target_location)

# Bir süre bekleme (örneğin, 30 saniye)
time.sleep(30)

# Bağlantıyı kapatma
master.close()
