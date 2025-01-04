import math
import matplotlib.pyplot as plt
import numpy as np


def plot_sector_and_dividing_line(R, phi1, phi2):
    # Преобразуем углы в радианы
    phi1_rad = math.radians(phi1)
    phi2_rad = math.radians(phi2)

    # Вычисление угола наклона разделительной линии
    mid_phi = (phi1_rad + phi2_rad) / 2
    k = math.tan(mid_phi)
    a, b, c = -k, 1, 0  # Общее уравнение прямой: ax + by + c = 0

    # Начерчение полного круга
    theta_circle = np.linspace(0, 2 * math.pi, 500)
    x_circle = R * np.cos(theta_circle)
    y_circle = R * np.sin(theta_circle)
    plt.plot(x_circle, y_circle, color="lightgray", linestyle="--", label="Full Circle")

    # Начерчение сектора
    theta = np.linspace(phi1_rad, phi2_rad, 100)
    x_arc = R * np.cos(theta)
    y_arc = R * np.sin(theta)
    plt.plot(x_arc, y_arc, label="Sector Arc")
    plt.plot(
        [0, R * math.cos(phi1_rad)],
        [0, R * math.sin(phi1_rad)],
        label=f"Radius φ1 ({phi1:.1f}°)",
    )
    plt.plot(
        [0, R * math.cos(phi2_rad)],
        [0, R * math.sin(phi2_rad)],
        label=f"Radius φ2 ({phi2:.1f}°)",
    )

    # Начерчение разделительной линии
    x_line = np.linspace(-R, R, 500)
    y_line = k * x_line
    plt.plot(
        x_line,
        y_line,
        label=f"Dividing Line: {a:.2f}x + {b:.2f}y + {c:.2f} = 0",
        linestyle="--",
    )

    # Настройки отображения, в общем
    plt.axis("equal")
    plt.xlim(-R * 1.1, R * 1.1)
    plt.ylim(-R * 1.1, R * 1.1)
    plt.legend()
    plt.title("Sector and Dividing Line")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()


def example():
    plot_sector_and_dividing_line(R=10, phi1=30, phi2=120)
