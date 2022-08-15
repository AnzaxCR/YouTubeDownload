from pytube import YouTube;
import moviepy.editor as mp;
import re;
import os;
import pathlib;

link = input("Digite el link del video que desea descargar: ");
path = pathlib.Path(__file__).parent.absolute();
# path = input("Digite el directorio donde desea guardar el archivo: ");
yt = YouTube(link);

print("Buscando...");
ys = yt.streams.filter(only_audio=True).first().download(path);
print("Descarga completa.");

#Convertir MP4 a MP3

print("Convirtiendo archivo...");
for file in os.listdir(path):
    if re.search('mp4', file):
        mp4_path = os.path.join(path, file);
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3');
        new_file = mp.AudioFileClip(mp4_path);
        new_file.write_audiofile(mp3_path);
        os.remove(mp4_path);
print("Finalizado.")
os.system("pause");