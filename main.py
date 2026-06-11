import random
import time

print("====================================")
print(" Temperature & Humidity Monitoring ")
print("====================================")

while True:

    temperature = random.randint(20, 40)
    humidity = random.randint(30, 90)

    print("\nSensor Readings")
    print("-----------------------")
    print(f"Temperature : {temperature} °C")
    print(f"Humidity    : {humidity} %")

    if temperature > 30:
        print("Temperature Alert : HIGH")
    else:
        print("Temperature Alert : NORMAL")

    if humidity > 70:
        print("Humidity Alert    : HIGH")
    else:
        print("Humidity Alert    : NORMAL")

    time.sleep(2)
