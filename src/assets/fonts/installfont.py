import os
import shutil
import platform

def install_font():
    font_path = os.path.join('assets', 'fonts', 'BebasNeue-Regular.ttf')

    if not os.path.exists(font_path):
        print("Fonte não encontrada!")
        return

    # Determina o diretório de fontes dependendo do sistema operacional
    if platform.system() == "Windows":
        fonts_dir = os.path.join(os.environ["WINDIR"], "Fonts")
    elif platform.system() == "Linux":
        fonts_dir = os.path.expanduser("~/.fonts")
    elif platform.system() == "Darwin":  # MacOS
        fonts_dir = os.path.expanduser("~/Library/Fonts")
    else:
        print("Sistema não suportado para instalação automática de fontes")
        return

    # Copia a fonte para o diretório apropriado
    shutil.copy(font_path, fonts_dir)
    print(f"Fonte instalada em {fonts_dir}")

# Executar a instalação
install_font()