temperature_fahrenheit = [32, 212, 275]

degrees_celsius = [(n-32)*(5/9) for n in temperature_fahrenheit]
print(degrees_celsius)