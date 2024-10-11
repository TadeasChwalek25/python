import tkinter as tk
from tkinter import messagebox

def odeslat_formular():
    jmeno = entry_jmeno.get()
    email = entry_email.get()
    zprava = text_zprava.get("1.0", tk.END)
    
    if not jmeno or not email or not zprava.strip():
        messagebox.showerror("Chyba", "Všechny pole jsou povinné!")
    else:
        messagebox.showinfo("Odesláno", f"Děkujeme, {jmeno}! Vaše zpráva byla odeslána.")
        entry_jmeno.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        text_zprava.delete("1.0", tk.END)

root = tk.Tk()
root.title("Jednoduchý formulář")

label_nazev = tk.Label(root, text="Kontaktujte nás", font=("Arial", 16))
label_nazev.pack(pady=10)


label_jmeno = tk.Label(root, text="Jméno:")
label_jmeno.pack()
entry_jmeno = tk.Entry(root, width=40)
entry_jmeno.pack(pady=5)

label_email = tk.Label(root, text="Email:")
label_email.pack()
entry_email = tk.Entry(root, width=40)
entry_email.pack(pady=5)

label_zprava = tk.Label(root, text="Zpráva:")
label_zprava.pack()
text_zprava = tk.Text(root, height=5, width=40)
text_zprava.pack(pady=5)

button_odeslat = tk.Button(root, text="Odeslat", command=odeslat_formular)
button_odeslat.pack(pady=10)

root.mainloop()
