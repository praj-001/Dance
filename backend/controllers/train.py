from email.mime import audio
from resemblyzer import preprocess_wav, VoiceEncoder
from pathlib import Path
import speech_recognition as sr
import os

#give the file path to your audio file
folder_location = os.getcwd()+'/backend/controllers/'

audio_file_path = folder_location +'demo.wav'
wav_fpath = Path(audio_file_path)

wav = preprocess_wav(wav_fpath)
encoder = VoiceEncoder("cpu")
_, cont_embeds, wav_splits = encoder.embed_utterance(wav, return_partials=True, rate=16)

from spectralcluster import SpectralClusterer

clusterer = SpectralClusterer(min_clusters=2,max_clusters=100)

labels = clusterer.predict(cont_embeds)

def create_labelling(labels,wav_splits):
    from resemblyzer.audio import sampling_rate
    times = [((s.start + s.stop) / 2) / sampling_rate for s in wav_splits]
    labelling = []
    start_time = 0

    for i,time in enumerate(times):
        if i>0 and labels[i]!=labels[i-1]:
            temp = [str(labels[i-1]),start_time,time]
            labelling.append(tuple(temp))
            start_time = time
        if i==len(times)-1:
            temp = [str(labels[i]),start_time,time]
            labelling.append(tuple(temp))

    return labelling
  
labelling = create_labelling(labels,wav_splits)





def transcribe_audio(star_time, end_time):
    from pydub import AudioSegment
    t1 = star_time * 1000 #Works in milliseconds
    t2 = end_time * 1000
    newAudio = AudioSegment.from_wav(folder_location+'demo.wav')
    newAudio = newAudio[t1:t2]
    newAudio.export(folder_location+'new.wav', format="wav")
    
    # obtain path to "english.wav" in the same folder as this script
    from os import path
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "new.wav")
    
    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        cut = r.record(source)  # read the entire audio file
    
    # recognize speech using Google Speech Recognition
    try:

        print(r.recognize_google(cut),"\n")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio","\n")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


for i in range(len(labelling)):
    print("Speaker",labelling[i][0],":","\n")
    transcribe_audio(labelling[i][1],labelling[i][2])

