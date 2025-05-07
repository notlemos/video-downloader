from app import _app, _frame
from widgets import setup_ui
from PIL import Image, ImageTk
def main():
    app = _app()
    frame = _frame(app)

    setup_ui(frame, app)

    img = Image.open("src/imgs/youtube.png")
    photo = ImageTk.PhotoImage(img)
    app.wm_iconphoto(True, photo)

    try:
        app.mainloop()
    except Exception as e:
        print(f"Erro ao fechar o aplicativo: {e}")
if __name__ == "__main__":
    main()