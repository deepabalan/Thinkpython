import math

print math

signal_power = 120
noise_power = 12

ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)

print decibels
