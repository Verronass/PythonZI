import tkinter as tk
from logic import decrypt, read_encrypted

BG        = "#080808"
BG_FIELD  = "#0f1f18"
BG_BTN    = "#0d2e20"
GREEN     = "#00c896"
GREEN_MID = "#008c68"
GREEN_DIM = "#1a4a38"

FONT_TITLE = ("Courier New", 18, "bold")
FONT_LABEL = ("Courier New",  9)
FONT_FIELD = ("Courier New", 10)
FONT_BTN   = ("Courier New", 11, "bold")

PLACEHOLDER = "ввести ключ"

def on_decrypt():
    key = key_field.get().strip()
    if key == PLACEHOLDER or not key:
        _set_output("⚠  введіть ключ")
        return
    _set_output(decrypt(key=key))

def _set_output(text):
    output_field.config(state="normal")
    output_field.delete("1.0", "end")
    output_field.insert("1.0", text)
    output_field.config(state="disabled")

def build_ui(root):
    root.title("Дешифратор")
    root.configure(bg=BG)
    root.resizable(False, False)

    outer = tk.Frame(root, bg=BG, padx=24, pady=20)
    outer.pack()

    # Заголовок
    tk.Label(outer, text="[ дешифратор ]", font=FONT_TITLE,
             fg=GREEN, bg=BG).pack(pady=(0, 4))
    tk.Frame(outer, bg=GREEN_DIM, height=1, width=340).pack(pady=(0, 8))

    # Зашифрований текст
    tk.Label(outer, text="// зашифрована інформація з файлу",
             font=FONT_LABEL, fg=GREEN_DIM, bg=BG, anchor="w",
             width=40).pack(anchor="w", pady=(0, 2))
    enc = tk.Text(outer, font=("Courier New", 8), fg=GREEN_MID, bg=BG_FIELD,
                  bd=0, highlightbackground=GREEN_DIM, highlightthickness=1,
                  relief="flat", wrap="char", height=4,
                  padx=10, pady=8, width=40, cursor="arrow")
    enc.insert("1.0", read_encrypted())
    enc.config(state="disabled")
    enc.pack()

    # Ключ
    tk.Label(outer, text="// ключ розшифрування",
             font=FONT_LABEL, fg=GREEN_DIM, bg=BG, anchor="w",
             width=40).pack(anchor="w", pady=(12, 2))

    global key_field
    key_field = tk.Entry(outer, font=FONT_FIELD, fg=GREEN_DIM, bg=BG_FIELD,
                         bd=0, highlightbackground=GREEN_DIM,
                         highlightthickness=1, insertbackground=GREEN,
                         relief="flat", width=40)
    key_field.insert(0, PLACEHOLDER)
    key_field.pack(ipady=9)

    def fi(e):
        if key_field.get() == PLACEHOLDER:
            key_field.delete(0, "end")
            key_field.config(fg=GREEN, show="*", highlightbackground=GREEN_MID)

    def fo(e):
        if not key_field.get():
            key_field.config(show="", fg=GREEN_DIM, highlightbackground=GREEN_DIM)
            key_field.insert(0, PLACEHOLDER)

    key_field.bind("<FocusIn>", fi)
    key_field.bind("<FocusOut>", fo)
    key_field.bind("<Return>", lambda e: on_decrypt())

    # Кнопка — примусово темна через canvas trick
    btn_frame = tk.Frame(outer, bg=BG_BTN,
                         highlightbackground=GREEN_MID, highlightthickness=1)
    btn_frame.pack(pady=12)

    btn = tk.Label(btn_frame, text="▶  розшифрувати", font=FONT_BTN,
                   fg=GREEN, bg=BG_BTN, cursor="hand2",
                   padx=40, pady=8)
    btn.pack()
    btn.bind("<Button-1>", lambda e: on_decrypt())
    btn.bind("<Enter>",    lambda e: btn.config(bg="#0d3d28"))
    btn.bind("<Leave>",    lambda e: btn.config(bg=BG_BTN))
    btn_frame.bind("<Button-1>", lambda e: on_decrypt())

    # Вивід
    tk.Label(outer, text="// розшифрований текст",
             font=FONT_LABEL, fg=GREEN_DIM, bg=BG, anchor="w",
             width=40).pack(anchor="w", pady=(0, 2))

    global output_field
    output_field = tk.Text(outer, font=FONT_FIELD, fg=GREEN, bg=BG_FIELD,
                           bd=0, highlightbackground=GREEN_DIM,
                           highlightthickness=1, relief="flat",
                           wrap="word", height=4, padx=10, pady=8,
                           width=40, state="disabled")
    output_field.pack()

    # Футер
    tk.Frame(outer, bg=GREEN_DIM, height=1, width=340).pack(pady=(12, 4))
    tk.Label(outer, text="XOR encryption  ·  first.txt",
             font=FONT_LABEL, fg=GREEN_DIM, bg=BG).pack()


if __name__ == "__main__":
    root = tk.Tk()
    build_ui(root)
    root.mainloop()