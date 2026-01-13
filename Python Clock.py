import tkinter as tk
import time
import math

class DarkClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Dark Python Clock")
        self.root.geometry("400x450")
        self.root.configure(bg="#121212")

        # Vytvoření plátna pro kreslení
        self.canvas = tk.Canvas(root, width=400, height=400, bg="#121212", highlightthickness=0)
        self.canvas.pack()

        # Štítek pro datum
        self.date_label = tk.Label(root, font=("Segoe UI", 12, "bold"), bg="#121212", fg="#ff4757")
        self.date_label.pack(pady=10)

        self.update_clock()

    def update_clock(self):
        self.canvas.delete("all")  # Vymazat plátno
        
        # Základní parametry
        center_x, center_y = 200, 200
        radius = 150

        # Kreslení ciferníku (vnější kruh)
        self.canvas.create_oval(center_x - radius - 10, center_y - radius - 10,
                                center_x + radius + 10, center_y + radius + 10,
                                outline="#282828", width=10)
        
        # Kreslení čísel 1-12
        for i in range(1, 13):
            angle = math.radians(i * 30 - 90)
            x = center_x + (radius - 30) * math.cos(angle)
            y = center_y + (radius - 30) * math.sin(angle)
            self.canvas.create_text(x, y, text=str(i), fill="#888888", font=("Segoe UI", 16, "bold"))

        # Získání času
        t = time.localtime()
        hr = t.tm_hour
        min = t.tm_min
        sec = t.tm_sec
        
        # Výpočet úhlů
        sec_angle = math.radians(sec * 6 - 90)
        min_angle = math.radians(min * 6 + sec * 0.1 - 90)
        hr_angle = math.radians((hr % 12) * 30 + min * 0.5 - 90)

        # Kreslení ručiček (střed -> konec)
        # Hodinová
        self.draw_hand(center_x, center_y, hr_angle, radius * 0.5, "#ffffff", 8)
        # Minutová
        self.draw_hand(center_x, center_y, min_angle, radius * 0.8, "#b3b3b3", 5)
        # Vteřinová
        self.draw_hand(center_x, center_y, sec_angle, radius * 0.9, "#ff4757", 2)

        # Středový bod
        self.canvas.create_oval(center_x - 7, center_y - 7, center_x + 7, center_y + 7, fill="#ffffff")

        # Aktualizace data
        date_str = time.strftime("%d. %m. %Y")
        self.date_label.config(text=date_str)

        # Naplánovat další aktualizaci za 1000ms (1 sekunda)
        self.root.after(1000, self.update_clock)

    def draw_hand(self, cx, cy, angle, length, color, width):
        x = cx + length * math.cos(angle)
        y = cy + length * math.sin(angle)
        self.canvas.create_line(cx, cy, x, y, fill=color, width=width, capstyle="round")

# Spuštění aplikace
if __name__ == "__main__":
    root = tk.Tk()
    app = DarkClock(root)
    root.mainloop()
