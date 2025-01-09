from pygame import mixer
from gtts import gTTS
def main():
   tts = gTTS('Tendulkar took up cricket at the age of eleve, made his Test match debut on 15 November 1989 against Pakistan in Karachi at the age of sixteen, and went on to represent Mumbai domestically and India internationally for close to twenty-four years. ')
   tts.save('output.mp3')
   mixer.init()
   mixer.music.load('output.mp3')
   mixer.music.play()
if __name__ == "__main__":
   main()
