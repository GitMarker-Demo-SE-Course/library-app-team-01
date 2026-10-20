"""A first try at a window for the app. Not finished."""

import tkinter as tk


def main():
    window = tk.Tk()
    window.title("Library")
    tk.Label(window, text="Library app").pack(padx=40, pady=20)
    window.mainloop()


if __name__ == "__main__":
    main()
