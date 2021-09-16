# requirements: playsound, soundfile and scipy
# command to install it: pip install playsound | pip install scipy | pip install soundfile

#Bibliotecas necessárias para rodar o script
import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write
from pathlib import Path

fs = 44100
second = int(input("Quantos segundos deseja gravar: "))
print("Gravando...")

record_voice = sd.rec(int(second * fs), samplerate=fs, channels=2)
sd.wait()

nome_Gravacao = input("Escolha o nome do arquio de áudio gravado (.wav): ")
fileName = r"./" + nome_Gravacao + ".wav"
fileObj = Path(fileName)

while fileObj.is_file():
    print("Arquivo com nome já existente! Por favor, escolha outro nome!")
    nome_Gravacao = input("Escolha o nome do arquio de áudio gravado (.wav): ")
    fileName = r"./" + nome_Gravacao + ".wav"
    fileObj = Path(fileName)
else:
    write(nome_Gravacao + ".wav", fs, record_voice)
    print("Gravação finalizada!")

data, fs = sf.read(nome_Gravacao + '.wav')
sd.play(data, fs)
sd.wait()
print("Reprodução realizada com sucesso!")