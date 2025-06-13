# newton_cooling.py
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def racire(T, t, k, T_mediu):
    return -k * (T - T_mediu)

def simulate_and_plot(T_initial, k, T_mediu, label):
    t = np.linspace(0, 60, 300)
    T = odeint(racire, T_initial, t, args=(k, T_mediu))
    plt.plot(t, T, label=label)

def main():
    params = [
        (90, 0.1, "T_ini=90°C, k=0.1"),
        (60, 0.2, "T_ini=60°C, k=0.2"),
        (100, 0.05, "T_ini=100°C, k=0.05"),
    ]
    T_mediu = 20
    for T_ini, k, label in params:
        simulate_and_plot(T_ini, k, T_mediu, label)
    plt.axhline(T_mediu, color='r', linestyle='--', label="T_mediu=20°C")
    plt.xlabel("Timp (minute)")
    plt.ylabel("Temperatură (°C)")
    plt.title("Răcirea conform legii lui Newton")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("racirea_newton.png")
    plt.show()

if __name__ == "__main__":
    main()
