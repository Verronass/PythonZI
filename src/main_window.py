import tkinter as tk

# --- Colors ---
BG_MAIN = "#8B5CF6"
COLOR_RED = "#EF4444"
COLOR_DARK = "#1a1a2e"
FONT_MAIN = ("Courier New", 13, "bold")
FONT_SMALL = ("Courier New", 11)

def on_encrypt():
    text = input_field.get("1.0", "end-1c").strip()
    if not text:
        return
    # Поки заглушка — логіка буде від партнера
    result = f"[encrypted]: {text[::-1]}"
    output_field.config(state="normal")
    output_field.delete("1.0", "end")
    output_field.insert("1.0", result)
    output_field.config(state="disabled")

def on_clear():
    input_field.delete("1.0", "end")
    output_field.config(state="normal")
    output_field.delete("1.0", "end")
    output_field.config(state="disabled")

def build_ui(root):
    root.title("CipherApp")
    root.geometry("380x420")
    root.configure(bg=BG_MAIN)
    root.resizable(False, False)

    card = tk.Frame(root, bg=BG_MAIN)
    card.place(relx=0.5, rely=0.5, anchor="center")

    # 1. "text code" — заголовок / поле вводу label
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

    # Поле вводу тексту
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

    # 2. "batton" — кнопка шифрування
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
        command=on_encrypt,
    )
    btn.pack(pady=(0, 10))

    # 3. "text" — поле виводу результату
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