import customtkinter as ctk
from PIL import Image
import os
from functions.yt import baixar_video



def setup_ui(frame, app):
    
    image = Image.open("src/assets/imgs/youtube.png")
    image_ctk = ctk.CTkImage(light_image=image, dark_image=image, size=(50,50))
    image_label = ctk.CTkLabel(frame, image=image_ctk, text="")
    image_label.place(x=280, y=35)


    title_font = ctk.CTkFont(family=("Verdana"), size=28, weight="bold")
    quality_font = ctk.CTkFont(family=("Verdana"), size=18, weight="bold")
    dropdown_font = ctk.CTkFont(family=("Verdana"), size=10, weight="bold")
    error_font = ctk.CTkFont(family=("Verdana"), size=12, weight="bold")
    download_btn_font = ctk.CTkFont(family="Trebuchet MS", size=18, weight="bold")

    title_label = ctk.CTkLabel(frame, text="YTDownloader", bg_color='transparent', text_color='white',font=title_font)
    title_label.place(x=70, y=40)


    entry_url = ctk.CTkEntry(frame, placeholder_text="Cole o link do vídeo que deseja baixar!", width=300, text_color='black', placeholder_text_color='black', fg_color='white', border_color='#565656')
    entry_url.place(x=50, y=95)

    status_label = ctk.CTkLabel(frame, text="", font=error_font, anchor="center")
    status_label.place(x=15, y=180, )

    

    quality_camp = ctk.CTkOptionMenu(frame, width=98, height=35,  values=["1080p", "720p", "480p"], 
                                     fg_color="white", button_color="white", button_hover_color="gray", 
                                     text_color="black", dropdown_fg_color="white", dropdown_hover_color="gray",  
                                     font=quality_font, dropdown_text_color="black",  hover=True,
                                     dropdown_font=dropdown_font)
    

    download_btn = ctk.CTkButton(frame, text="DOWNLOAD", width=130, height=30, fg_color='white',border_color='black' , font=download_btn_font, text_color='black', hover_color='gray', command=lambda: baixar_video(entry_url, status_label, quality_camp))
    download_btn.place(x=70, y=140)
    

    copyright = ctk.CTkLabel(app, text="", font=quality_font)
    copyright.place(x=200, y=550)
    
    quality_camp.place(x=230, y=140)
    return quality_camp

