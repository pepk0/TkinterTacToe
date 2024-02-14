from gui.window import MainFrame


def main() -> None:
    # this loops makes the game run indefinitely
    # until the quit game button is chosen
    while True:
        root = MainFrame()
        root.mainloop()


if __name__ == "__main__":
    main()
