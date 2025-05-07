import customtkinter as ctk


def _app():
    ctk.set_appearance_mode("dark")
    
    app = ctk.CTk()
    
    app.title("YTDownloader")
    
    app.geometry("500x600")
    app.resizable(width=False, height=False)
    return app

def _frame(app):
    frame = ctk.CTkFrame(master=app, width=400, height=250, fg_color='#565656')
    frame.place(x=50, y=150)  
    
    return frame



