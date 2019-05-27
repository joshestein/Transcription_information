import glob 
import os

audio_dir = "/Users/joshstein/Documents/UCT/Engineering/4th_year/Design/Videos/"

def transcribe_model_selection(speech_file, model):
        from google.cloud import speech
        client = speech.SpeechClient()

        with open(speech_file, 'rb') as audio_file:
                content = audio_file.read()

        audio = speech.types.RecognitionAudio(content=content)

        config = speech.types.RecognitionConfig(
                        encoding = speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
                        language_code = 'en-US',
                        model = model)

        response = client.recognize(config, audio)

        transcript = ""
        for result in response.results:
                transcript += result.alternatives[0].transcript
        return transcript

def write_transcript(filename, transcript):
        f = open(filename, 'a')
        f.write(transcript)
        f.close()

def main():
        files = glob.glob(audio_dir+"*.wav")
        for file in files:
                root_name = os.path.basename(file)      # get basename
                root_name = root_name[:-8]              # remove trailing part number and extension
                transcript = transcribe_model_selection(file, 'default')
                write_transcript(root_name + '.txt', transcript)


if __name__ == '__main__':
        main()