import tkinter as tk
from tkinter import ttk
from logic import encrypt, decrypt

# --- Colors ---
BG_MAIN = "#000000"
COLOR_GREEN = "#00C896"
COLOR_DARK = "#000000"
FONT_TITLE = ("Courier New", 16, "bold")
FONT_MAIN = ("Courier New", 13, "bold")
FONT_SMALL = ("Courier New", 11)

ALGORITHMS = ["Caesar", "AES-256", "RSA"]

def on_decrypt():
    key = key_field.get().strip()
    text = input_field.get("1.0", "end-1c").strip()
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
    root.title("Дишефратор")
    root.geometry("340x480")
    root.configure(bg=BG_MAIN)
    root.resizable(False, False)

    card = tk.Frame(root, bg=BG_MAIN)
    card.place(relx=0.5, rely=0.5, anchor="center")

    # Заголовок
    tk.Label(
        card,
        text="дишефратор",
        font=FONT_TITLE,
        fg=COLOR_GREEN,
        bg=BG_MAIN,
    ).pack(pady=(0, 20))

    # Поле вводу зашифрованого тексту (прихований, підтягується з файлу/партнера)
    global input_field
    input_field = tk.Text(
        card,
        font=FONT_SMALL,
        fg=COLOR_GREEN,
        bg=BG_MAIN,
        bd=2,
        relief="solid",
        highlightbackground=COLOR_GREEN,
        highlightthickness=1,
        insertbackground=COLOR_GREEN,
        width=28,
        height=3,
        padx=8,
        pady=6,
        wrap="word",
    )
    input_field.pack(pady=(0, 12))

    # Dropdown алгоритму (компактний)
    global algo_var
    algo_var = tk.StringVar(value=ALGORITHMS[0])
    algo_frame = tk.Frame(card, bg=BG_MAIN)
    algo_frame.pack(pady=(0, 12), fill="x")

    tk.Label(algo_frame, text="алгоритм:", font=("Courier New", 9),
             fg=COLOR_GREEN, bg=BG_MAIN).pack(side="left", padx=(0, 6))

    style = ttk.Style()
    style.theme_use("default")
    style.configure("Green.TCombobox",
        fieldbackground=BG_MAIN,
        background=BG_MAIN,
        foreground=COLOR_GREEN,
        selectbackground=BG_MAIN,
        selectforeground=COLOR_GREEN,
    )
    algo_menu = ttk.Combobox(
        algo_frame,
        textvariable=algo_var,
        values=ALGORITHMS,
        state="readonly",
        width=12,
        font=("Courier New", 10),
        style="Green.TCombobox",
    )
    algo_menu.pack(side="left")

    # "ввести ключ" — поле вводу ключа
    global key_field
    key_field = tk.Entry(
        card,
        font=FONT_MAIN,
        fg=COLOR_GREEN,
        bg=BG_MAIN,
        bd=2,
        relief="solid",
        highlightbackground=COLOR_GREEN,
        highlightthickness=1,
        insertbackground=COLOR_GREEN,
        width=22,
        show="*",
    )
    key_field.insert(0, "")
    key_field.pack(pady=(0, 12), ipady=8)

    # Підказка над полем
    # (вставляємо placeholder через bind)
    placeholder = "ввести ключ"
    def on_focus_in(e):
        if key_field.get() == placeholder:
            key_field.delete(0, "end")
            key_field.config(show="*")
    def on_focus_out(e):
        if not key_field.get():
            key_field.config(show="")
            key_field.insert(0, placeholder)
    key_field.config(show="")
    key_field.insert(0, placeholder)
    key_field.config(fg="#00C896")
    key_field.bind("<FocusIn>", on_focus_in)
    key_field.bind("<FocusOut>", on_focus_out)

    # "кнопка" — кнопка розшифрування
    btn = tk.Button(
        card,
        text="кнопка",
        font=FONT_MAIN,
        fg=COLOR_GREEN,
        bg=BG_MAIN,
        activebackground="#001a12",
        activeforeground=COLOR_GREEN,
        bd=2,
        relief="solid",
        highlightbackground=COLOR_GREEN,
        highlightthickness=1,
        padx=24,
        pady=6,
        cursor="hand2",
        command=on_decrypt,
    )
    btn.pack(pady=(0, 12))

    # "повідомлення" — вивід результату
    global output_field
    output_field = tk.Text(
        card,
        font=FONT_SMALL,
        fg=COLOR_GREEN,
        bg=BG_MAIN,
        bd=2,
        relief="solid",
        highlightbackground=COLOR_GREEN,
        highlightthickness=1,
        width=28,
        height=3,
        padx=8,
        pady=6,
        wrap="word",
        state="disabled",
    )
    output_field.pack(pady=(0, 10))

    # Clear
    tk.Button(
        card,
        text="очистити",
        font=("Courier New", 9),
        fg="#005940",
        bg=BG_MAIN,
        bd=1,
        relief="solid",
        padx=8,
        pady=2,
        cursor="hand2",
        command=on_clear,
    ).pack()


if __name__ == "__main__":
    root = tk.Tk()
    build_ui(root)
    root.mainloop()