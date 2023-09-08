import psutil
from plyer import notification
import time

def check_battery():
    while True:
        battery = psutil.sensors_battery()
        if battery.power_plugged or battery.percent >= 37:
            message = f"Battery level is {battery.percent}%."
            notification.notify(
                title="Battery Alert",
                message=message,
                timeout=10
            )
        time.sleep(60)  # Check battery status every minute

if __name__ == "__main__":
    check_battery()
