import tkinter as tk
from logic import decrypt

BG = "#0d0d0d"
BG_CARD = "#111111"
GREEN = "#00c896"
GREEN_DIM = "#005940"
GREEN_HINT = "#1a3d32"
FONT_TITLE = ("Courier New", 18, "bold")
FONT_BTN   = ("Courier New", 13, "bold")
FONT_SMALL = ("Courier New", 11)
FONT_HINT  = ("Courier New", 9)

PLACEHOLDER = "ввести ключ"

def on_decrypt():
    key = key_field.get().strip()
    if key == PLACEHOLDER or not key:
        _set_output("⚠  введіть ключ")
        return
    result = decrypt(key=key)
    _set_output(result)

def _set_output(text):
    output_field.config(state="normal")
    output_field.delete("1.0", "end")
    output_field.insert("1.0", text)
    output_field.config(state="disabled")

def build_ui(root):
    root.title("Дишефратор")
    root.geometry("360x400")
    root.configure(bg=BG)
    root.resizable(False, False)

    # Зовнішня рамка — картка
    card = tk.Frame(root, bg=BG_CARD, bd=0, highlightbackground=GREEN_DIM,
                    highlightthickness=1)
    card.place(relx=0.5, rely=0.5, anchor="center", width=300, height=340)

    # Заголовок
    tk.Label(card, text="дишефратор", font=FONT_TITLE,
             fg=GREEN, bg=BG_CARD).place(relx=0.5, y=32, anchor="center")

    # Роздільник
    tk.Frame(card, bg=GREEN_DIM, height=1).place(x=20, y=58, width=260)

    # Поле ключа
    global key_field
    key_field = tk.Entry(card, font=FONT_BTN, fg=GREEN_DIM, bg=BG,
                         bd=0, highlightbackground=GREEN_DIM,
                         highlightthickness=1, insertbackground=GREEN,
                         relief="flat", width=22)
    key_field.insert(0, PLACEHOLDER)
    key_field.place(relx=0.5, y=110, anchor="center", height=38, width=260)

    def focus_in(e):
        if key_field.get() == PLACEHOLDER:
            key_field.delete(0, "end")
            key_field.config(fg=GREEN, show="*")

    def focus_out(e):
        if not key_field.get():
            key_field.config(show="", fg=GREEN_DIM)
            key_field.insert(0, PLACEHOLDER)

    key_field.bind("<FocusIn>", focus_in)
    key_field.bind("<FocusOut>", focus_out)
    key_field.bind("<Return>", lambda e: on_decrypt())

    # Кнопка
    btn = tk.Button(card, text="розшифрувати", font=FONT_BTN,
                    fg=GREEN, bg=BG, activebackground=GREEN_HINT,
                    activeforeground=GREEN, bd=0,
                    highlightbackground=GREEN, highlightthickness=1,
                    relief="flat", cursor="hand2", command=on_decrypt)
    btn.place(relx=0.5, y=178, anchor="center", height=38, width=200)

    # Роздільник
    tk.Frame(card, bg=GREEN_DIM, height=1).place(x=20, y=210, width=260)

    # Вивід
    global output_field
    output_field = tk.Text(card, font=FONT_SMALL, fg=GREEN, bg=BG,
                           bd=0, highlightbackground=GREEN_DIM,
                           highlightthickness=1, relief="flat",
                           wrap="word", state="disabled",
                           padx=10, pady=8)
    output_field.place(x=20, y=222, width=260, height=90)

    # Підказка внизу
    tk.Label(card, text="XOR · first.txt", font=FONT_HINT,
             fg=GREEN_DIM, bg=BG_CARD).place(relx=0.5, y=326, anchor="center")


if __name__ == "__main__":
    root = tk.Tk()
    build_ui(root)
    root.mainloop()