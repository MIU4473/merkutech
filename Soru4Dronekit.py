from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

# Bağlantı kurma (SITL kullanımı örneği)
vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)

# Hedef konumu belirleme
target_location = LocationGlobalRelative(-35.363261, 149.165230, 20)  # Örnek bir hedef konumu

# Konuma git fonksiyonu
def go_to_location(target):
    vehicle.simple_goto(target)

# Drone'u hedef konuma götür
go_to_location(target_location)

# Bir süre bekleme (örneğin, 30 saniye)
time.sleep(30)

# Bağlantıyı kapatma
vehicle.close()
