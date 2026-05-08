import tkinter as tk
from logic import decrypt

BG_MAIN = "#000000"
COLOR_GREEN = "#00C896"
FONT_TITLE = ("Courier New", 16, "bold")
FONT_MAIN = ("Courier New", 13, "bold")
FONT_SMALL = ("Courier New", 11)

def on_decrypt():
    key = key_field.get().strip()
    if key == "ввести ключ" or not key:
        return
    text = input_field.get("1.0", "end-1c").strip()
    if not text:
        return
    result = decrypt(text, key)
    output_field.config(state="normal")
    output_field.delete("1.0", "end")
    output_field.insert("1.0", result)
    output_field.config(state="disabled")

def build_ui(root):
    root.title("Дишефратор")
    root.geometry("320x420")
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
    ).pack(pady=(0, 24))

    # Поле для ключа з placeholder
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
        show="",
    )
    key_field.insert(0, "ввести ключ")

    def on_focus_in(e):
        if key_field.get() == "ввести ключ":
            key_field.delete(0, "end")
            key_field.config(show="*")

    def on_focus_out(e):
        if not key_field.get():
            key_field.config(show="")
            key_field.insert(0, "ввести ключ")

    key_field.bind("<FocusIn>", on_focus_in)
    key_field.bind("<FocusOut>", on_focus_out)
    key_field.pack(pady=(0, 16), ipady=8)

    # Кнопка
    tk.Button(
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
    ).pack(pady=(0, 16))

    # Вивід повідомлення
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
    output_field.pack()

    # Прихований input (зашифрований текст підтягується програмно)
    global input_field
    input_field = tk.Text(root, width=1, height=1)
    input_field.place(x=-100, y=-100)


if __name__ == "__main__":
    root = tk.Tk()
    build_ui(root)
    root.mainloop()