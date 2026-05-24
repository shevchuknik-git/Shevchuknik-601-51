import tkinter as tk
from tkinter import ttk, messagebox
from itertools import islice
from my_package.lab6_logic import prime_gen

def generate_primes():
    try:
        count = int(entry_count.get())
        if count <= 0:
            raise ValueError
        
        gen = prime_gen()
        result = list(islice(gen, count))
        
        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, str(result))
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное положительное число!")

root = tk.Tk()
root.title("GUI для Лабораторной №7")
root.geometry("400x250")
root.resizable(False, False)

ttk.Label(root, text="Сколько простых чисел сгенерировать?", font=("Arial", 12)).pack(pady=10)

entry_count = ttk.Entry(root, font=("Arial", 12), justify="center")
entry_count.insert(0, "10")
entry_count.pack(pady=5)

ttk.Button(root, text="Сгенерировать", command=generate_primes).pack(pady=10)

text_result = tk.Text(root, height=5, width=45, font=("Arial", 10))
text_result.pack(pady=5)

root.mainloop()