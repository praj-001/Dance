import speech_recognition as sr


from os import path
AUDIO_FILE = path.join(path.dirname(
    path.realpath(__file__)), "speakerstwo1.wav")

# use the audio file as the audio source
r = sr.Recognizer()

# the below comments are for splitting the audio file for bigger files, kindly use with caution
# from pydub import AudioSegment
# from pydub.utils import make_chunks
# myaudio = AudioSegment.from_file("demo.wav", "wav")
# chunk_length_ms = 1000  # pydub calculates in millisec
# chunks = make_chunks(myaudio, chunk_length_ms)  # Make chunks of one sec

# Export all of the individual chunks as wav files

# for i, chunk in enumerate(chunks):
#     chunk_name = "chunk{0}.wav".format(i)
#     print("exporting", chunk_name)
#     chunk.export(chunk_name, format="wav")

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

try:

    print(r.recognize_google(audio))
except sr.UnknownValueError:
    print("Speech Recognition could not understand audio\n")
except sr.RequestError as e:
    print(
        "Could not request results from Speech Recognition service; {0}".format(e))
