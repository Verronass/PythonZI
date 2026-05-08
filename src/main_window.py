import tkinter as tk
from tkinter import ttk
from logic import encrypt, decrypt

# --- Colors ---
BG_MAIN = "#8B5CF6"
COLOR_RED = "#EF4444"
COLOR_DARK = "#1a1a2e"
FONT_MAIN = ("Courier New", 13, "bold")
FONT_SMALL = ("Courier New", 11)

ALGORITHMS = ["Caesar", "AES-256", "RSA"]

def on_decrypt():
    text = input_field.get("1.0", "end-1c").strip()
    key = key_field.get().strip()
    if not text:
        return
    method = algo_var.get()
    result = decrypt(text, method, key)
    output_field.config(state="normal")
    output_field.delete("1.0", "end")
    output_field.insert("1.0", result)
    output_field.config(state="disabled")

def on_clear():
    input_field.delete("1.0", "end")
    key_field.delete(0, "end")
    output_field.config(state="normal")
    output_field.delete("1.0", "end")
    output_field.config(state="disabled")

def build_ui(root):
    root.title("CipherApp")
    root.geometry("380x510")
    root.configure(bg=BG_MAIN)
    root.resizable(False, False)

    card = tk.Frame(root, bg=BG_MAIN)
    card.place(relx=0.5, rely=0.5, anchor="center")

    # 1. "text code" — поле вводу зашифрованого тексту
    lbl_code = tk.Label(
        card,
        text="text code",
        font=("Courier New", 15, "bold"),
        fg=COLOR_RED,
        bg=BG_MAIN,
        bd=2,
        relief="solid",
        padx=18,
        pady=6,
        highlightbackground="#F97316",
        highlightthickness=2,
    )
    lbl_code.pack(pady=(0, 8))

    global input_field
    input_field = tk.Text(
        card,
        font=FONT_SMALL,
        fg=COLOR_DARK,
        bg="#EDE9FE",
        bd=2,
        relief="solid",
        width=32,
        height=4,
        padx=8,
        pady=6,
        wrap="word",
    )
    input_field.pack(pady=(0, 10))

    # Dropdown — вибір алгоритму
    global algo_var
    algo_var = tk.StringVar(value=ALGORITHMS[0])

    algo_frame = tk.Frame(card, bg=BG_MAIN)
    algo_frame.pack(pady=(0, 8), fill="x")

    tk.Label(
        algo_frame,
        text="Алгоритм:",
        font=("Courier New", 10),
        fg="#EDE9FE",
        bg=BG_MAIN,
    ).pack(side="left", padx=(0, 8))

    algo_menu = ttk.Combobox(
        algo_frame,
        textvariable=algo_var,
        values=ALGORITHMS,
        state="readonly",
        width=18,
        font=("Courier New", 11),
    )
    algo_menu.pack(side="left")

    # Поле для ключа
    key_frame = tk.Frame(card, bg=BG_MAIN)
    key_frame.pack(pady=(0, 10), fill="x")

    tk.Label(
        key_frame,
        text="Ключ:     ",
        font=("Courier New", 10),
        fg="#EDE9FE",
        bg=BG_MAIN,
    ).pack(side="left", padx=(0, 8))

    global key_field
    key_field = tk.Entry(
        key_frame,
        font=FONT_SMALL,
        fg=COLOR_DARK,
        bg="#EDE9FE",
        bd=2,
        relief="solid",
        width=20,
        show="*",
    )
    key_field.pack(side="left")

    # 2. "batton" — кнопка розшифрування
    btn = tk.Button(
        card,
        text="batton",
        font=FONT_MAIN,
        fg=COLOR_DARK,
        bg=BG_MAIN,
        activebackground="#7C3AED",
        bd=2,
        relief="solid",
        padx=18,
        pady=6,
        cursor="hand2",
        command=on_decrypt,
    )
    btn.pack(pady=(0, 10))

    # 3. "text" — вивід розшифрованого тексту
    global output_field
    output_field = tk.Text(
        card,
        font=FONT_SMALL,
        fg=COLOR_DARK,
        bg="#EDE9FE",
        bd=2,
        relief="solid",
        width=32,
        height=4,
        padx=8,
        pady=6,
        wrap="word",
        state="disabled",
    )
    output_field.pack(pady=(0, 8))

    # Кнопка очищення
    btn_clear = tk.Button(
        card,
        text="clear",
        font=("Courier New", 10),
        fg="#9CA3AF",
        bg=BG_MAIN,
        bd=1,
        relief="solid",
        padx=10,
        pady=3,
        cursor="hand2",
        command=on_clear,
    )
    btn_clear.pack()


if __name__ == "__main__":
    root = tk.Tk()
    build_ui(root)
    root.mainloop()