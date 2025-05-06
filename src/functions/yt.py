import os
import subprocess
from pytubefix import YouTube

def baixar_video(entry_url, status_label, quality_camp):
    url = entry_url.get() 
    status_label.configure(text="Baixando...", text_color="orange")
    res = quality_camp.get()

    try:
        yt = YouTube(url)

        video = yt.streams.filter(only_video=True, file_extension='mp4', res=res).first()   
        audio = yt.streams.filter(only_audio=True, file_extension='mp4').first()
        
        
        output_path = "downloads"
        os.makedirs(output_path, exist_ok=True)

        
        video_path = video.download(output_path=output_path, filename="video.mp4")
        audio_path = audio.download(output_path=output_path, filename="audio.mp4")

        
        final_output = os.path.join(output_path, f"{yt.title}.mp4")
        comando_ffmpeg = f'ffmpeg -i "{video_path}" -i "{audio_path}" -c copy "{final_output}" -y'

        
        subprocess.run(comando_ffmpeg, shell=True, timeout=300)
        
        

        
        os.remove(video_path)
        os.remove(audio_path)

        
        status_label.configure(text="Download finalizado!", text_color="green", width=350)
    except Exception as e:
        
        status_label.configure(text=f"Erro: {str(e)}", text_color="red", width=100)

        

