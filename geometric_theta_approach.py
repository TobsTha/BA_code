import numpy as np

theta = 8

def snell_to_air(theta_SiO2):
    n_air = 1
    n_SiO2 = 1.44
    theta_SiO2 = np.radians(theta_SiO2)
    theta_air = np.arcsin(n_SiO2/n_air * np.sin(theta_SiO2))
    theta_air = np.degrees(theta_air)
    return theta_air

def snell_to_SiO2(theta_air):
    n_air = 1
    n_SiO2 = 1.44
    theta_air = np.radians(theta_air)
    theta_SiO2 = np.arcsin(n_air/n_SiO2 * np.sin(theta_air))
    theta_SiO2 = np.degrees(theta_SiO2)
    return theta_SiO2

def theta_45d_to_theta(theta_45d, phi = 45):
    theta_45d = np.radians(theta_45d)
    phi = np.radians(phi)
    theta = np.arctan(np.tan(theta_45d)/np.sqrt(1 + (np.tan(phi))**2))
    theta = np.degrees(theta)
    return theta

print(snell_to_air(5.65))
print(snell_to_SiO2(8))
print(theta_45d_to_theta(11.56))
print(theta_45d_to_theta(snell_to_air(8)))
print(snell_to_air(theta_45d_to_theta(8)))