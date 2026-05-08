import tkinter as tk

# --- Colors ---
BG_MAIN = "#8B5CF6"       # purple background
BG_WIDGET = "#7C3AED"
COLOR_RED = "#EF4444"
COLOR_DARK = "#1a1a2e"
COLOR_TEXT = "#1a1a2e"
FONT_MAIN = ("Courier New", 13, "bold")

def build_ui(root):
    root.title("CipherApp")
    root.geometry("340x280")
    root.configure(bg=BG_MAIN)
    root.resizable(False, False)

    # Center frame (purple card like on the screenshot)
    card = tk.Frame(root, bg=BG_MAIN, bd=0)
    card.place(relx=0.5, rely=0.5, anchor="center")

    # 1. "text code" — red text with orange border
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
    lbl_code.pack(pady=(0, 10))

    # 2. "batton" — button with dark border
    btn = tk.Button(
        card,
        text="batton",
        font=FONT_MAIN,
        fg=COLOR_TEXT,
        bg=BG_MAIN,
        activebackground=BG_WIDGET,
        bd=2,
        relief="solid",
        padx=18,
        pady=6,
        cursor="hand2",
        command=lambda: print("batton clicked"),
    )
    btn.pack(pady=(0, 10))

    # 3. "text" — label with dark border
    lbl_text = tk.Label(
        card,
        text="text",
        font=FONT_MAIN,
        fg=COLOR_TEXT,
        bg=BG_MAIN,
        bd=2,
        relief="solid",
        padx=18,
        pady=6,
    )
    lbl_text.pack()


if __name__ == "__main__":
    root = tk.Tk()
    build_ui(root)
    root.mainloop()
