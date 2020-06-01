import numpy as np

A, B, H, M = map(int, input().split())
delta_min = 360 / 60
deg_min = delta_min * M
delta_hour = 360 / 12
delta_min_in_hour = 30 / 60
deg_hour = delta_hour * H + delta_min_in_hour * M

hour_X = A * np.sin(np.deg2rad(deg_hour))
hour_Y = A * np.cos(np.deg2rad(deg_hour))
min_X = B * np.sin(np.deg2rad(deg_min))
min_Y = B * np.cos(np.deg2rad(deg_min))

print(np.sqrt((hour_X - min_X)**2 + (hour_Y-min_Y)**2))
