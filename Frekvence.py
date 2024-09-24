import numpy as np
import matplotlib.pyplot as plt

# Vytvoříme časovou osu
sampling_rate = 1000  # vzorkovací frekvence v Hz
T = 1.0 / sampling_rate  # délka vzorkovacího intervalu
x = np.linspace(0.0, 1.0, sampling_rate)  # časová osa

# Vytvoříme signál složený z několika frekvencí
f1, f2 = 50, 120  # frekvence v Hz
y = np.sin(f1 * 2.0 * np.pi * x) + 0.5 * np.sin(f2 * 2.0 * np.pi * x)

# Aplikujeme rychlou Fourierovu transformaci
yf = np.fft.fft(y)
xf = np.fft.fftfreq(len(y), T)[:len(y)//2]

# Vykreslení původního signálu
plt.subplot(2, 1, 1)
plt.plot(x, y)
plt.title("Původní signál")
plt.xlabel("Čas [s]")
plt.ylabel("Amplituda")

# Vykreslení výsledku Fourierovy transformace (frekvenční spektrum)
plt.subplot(2, 1, 2)
plt.plot(xf, 2.0/len(y) * np.abs(yf[:len(y)//2]))
plt.title("Frekvenční spektrum")
plt.xlabel("Frekvence [Hz]")
plt.ylabel("Amplituda")

plt.tight_layout()
plt.show()
