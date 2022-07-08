from pprint import pprint
from vosk import KaldiRecognizer
from vosk import Model
from email.mime import audio
from resemblyzer import preprocess_wav, VoiceEncoder
from pathlib import Path
FRAME_RATE = 16000
CHANNELS=1

from pydub import AudioSegment

import json
import os

folder = os.getcwd()+'/backend/controllers/'

# RECOGNITION

def voice_recognition(filename):
    model = Model(model_name="vosk-model-small-en-us-0.15")
    rec = KaldiRecognizer(model, FRAME_RATE)
    rec.SetWords(True)

    wav = AudioSegment.from_wav(folder+"new.wav")
    wav = wav.set_channels(CHANNELS)
    wav = wav.set_frame_rate(FRAME_RATE)

    step = 45000
    transcript = ""

    for i in range(0,len(wav),step):
        # print(f"Progress: {i/len(wav)}")
        segment = wav[i:(i+step)]

        rec.AcceptWaveform(segment.raw_data)
        result = rec.Result()

        text = json.loads(result)["text"]
        transcript += text
    
    return(transcript)


#DIARIZATION

audio_file_path = 'demo.wav'
wav_fpath = Path(folder+audio_file_path)

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

# Splits audio file for individual speaker instances

for i in range(len(labelling)):
    print("Speaker",labelling[i][0],":",end=' ')
    t1 = labelling[i][1]*1000 #Works in milliseconds
    t2 = labelling[i][2]*1000
    newAudio = AudioSegment.from_wav(folder+"demo.wav")
    newAudio = newAudio[t1:t2]
    newAudio.export(folder+'new.wav', format="wav")
    print(voice_recognition(folder+"demo.wav"),end='')