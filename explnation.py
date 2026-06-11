# Code Explanation

## Import Libraries

import random
import time

### random
Used to generate simulated sensor readings.

### time
Used to introduce delay between readings.

## Generate Temperature

temperature = random.randint(20,40)

Generates random temperature values.

## Generate Humidity

humidity = random.randint(30,90)

Generates random humidity values.

## Alert Logic

if temperature > 30

Generates High Temperature Alert.

if humidity > 70

Generates High Humidity Alert.

## Delay

time.sleep(2)

Waits 2 seconds before generating new sensor values.
