import sounddevice as soundd
from scipy.io.wavfile import write

dur = int(input("Enter how many seconds you want to record: "))
name = input("Enter file name for your recorded sound: ")
fq = 44100


print("Recording\n")

mr = soundd.rec(int(dur*fq), samplerate=fq, channels=2)
soundd.wait()
write(name+".wav",fq,mr)
print("Finished")