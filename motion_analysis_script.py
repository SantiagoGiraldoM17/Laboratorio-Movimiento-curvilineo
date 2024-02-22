
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Load the data
file_path = 'uaj_gms_CoordsLaboratorio_ACT_time_x_y_z.txt'  
data = pd.read_csv(file_path, skiprows=lambda i: i % 3 != 0 and i != 0, header=None, usecols=[0, 1, 2], names=['time', 'x', 'y'])

# Preprocess and calculations
data['delta_x'] = data['x'].diff()
data['delta_y'] = data['y'].diff()
data['delta_t'] = data['time'].diff()
data['velocity_x'] = data['delta_x'] / data['delta_t']
data['velocity_y'] = data['delta_y'] / data['delta_t']
data['velocity'] = np.sqrt(data['velocity_x']**2 + data['velocity_y']**2)
data['acceleration_x'] = np.diff(data['velocity_x']) / data['delta_t'][1:]
data['acceleration_y'] = np.diff(data['velocity_y']) / data['delta_t'][1:]
data['delta_v'] = data['velocity'].diff()
data['normal_acceleration'] = np.sqrt(data['acceleration_x']**2 + data['acceleration_y']**2)
data['distance'] = np.sqrt(data['delta_x']**2 + data['delta_y']**2)
data['angle'] = np.arctan2(data['delta_y'], data['delta_x'])
data['delta_angle'] = data['angle'].diff()
data['angular_velocity'] = data['delta_angle'] / data['delta_t']
data['delta_angular_velocity'] = data['angular_velocity'].diff()
data['angular_acceleration'] = data['delta_angular_velocity'] / data['delta_t']
data['speed'] = np.sqrt(data['delta_x']**2 + data['delta_y']**2) / data['delta_t']
data['tangential_acceleration'] = data['speed'].diff() / data['delta_t']
data['total_acceleration'] = np.sqrt(data['tangential_acceleration']**2 + data['normal_acceleration']**2)

# Plotting
fig, axs = plt.subplots(4, 2, figsize=(14, 12), tight_layout=True)
axs[0, 0].plot(data['time'], data['distance'].cumsum())
axs[0, 0].set_title('Cumulative Distance')
axs[1, 0].plot(data['time'], data['velocity_x'])
axs[1, 0].set_title('Velocity x')
axs[2, 0].plot(data['time'], data['velocity'])
axs[2, 0].set_title('Velocity')
axs[3, 0].plot(data['time'], data['total_acceleration'])
axs[3, 0].set_title('Total Acceleration')
axs[0, 1].plot(data['time'], data['angular_velocity'])
axs[0, 1].set_title('Angular Velocity')
axs[1, 1].plot(data['time'], data['velocity_y'])
axs[1, 1].set_title('Velocity y')
axs[2, 1].plot(data['time'], data['normal_acceleration'])
axs[2, 1].set_title('Normal Acceleration')
axs[3, 1].plot(data['time'], data['tangential_acceleration'])
axs[3, 1].set_title('Tangential Acceleration')

plt.savefig("grafica.png", dpi=300)
plt.show()

print(data['radius_of_curvature'])





