# install_fonts.py
import os
import shutil
import platform

def install_font():
    font_path = os.path.abspath(os.path.join('src', 'assets', 'fonts', 'BebasNeue-Regular.otf'))

    




    if not os.path.exists(font_path):
        print(f"Fonte não encontrada no caminho: {font_path}")
        return

    
    if platform.system() == "Windows":
        fonts_dir = os.path.join(os.environ["WINDIR"], "Fonts")
    elif platform.system() == "Linux":
        fonts_dir = os.path.expanduser("~/.fonts")
    elif platform.system() == "Darwin":  # MacOS
        fonts_dir = os.path.expanduser("~/Library/Fonts")
    else:
        print("Sistema não suportado para instalação automática de fontes")
        return

    
    if not os.path.exists(os.path.join(fonts_dir, 'BebasNeue-Regular.ttf')):
        shutil.copy(font_path, fonts_dir)
        print(f"Fonte instalada em {fonts_dir}")
    else:
        print("Fonte já está instalada.")
