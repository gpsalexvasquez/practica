from django.shortcuts import render
import os
from transformers import pipeline
from django.conf import settings
from moviepy.editor import VideoFileClip
import speech_recognition as sr

transcriber = pipeline("automatic-speech-recognition",model="openai/whisper-small")

def index(request):
    transcription = ""
    if request.method == "POST" and request.FILES.get("video_file"):
        video_file = request.FILES["video_file"]
        video_path = os.path.join(settings.MEDIA_ROOT, video_file.name)
        with open(video_path,"wb") as f:
            for chunk in video_file.chunks():
                f.write(chunk)
        audio, texto=extraer_audio_y_convertir_a_texto(video_path)
        # texto=""
        return render(request, "transcriber/index.html",{"transcription":texto})
    return render(request, "transcriber/index.html")

def extraer_audio_y_convertir_a_texto(input_video_path):

    video_clip = VideoFileClip(input_video_path)
    output_audio_path = input_video_path.replace('.mp4', '.wav')
    video_clip.audio.write_audiofile(output_audio_path)
    audio_text = ""

    recognizer = sr.Recognizer()
    # Ajustar la sensibilidad del reconocedor de voz
    with sr.AudioFile(output_audio_path) as source:
        recognizer.adjust_for_ambient_noise(source)

    file_name = os.path.splitext(os.path.basename(output_audio_path))[0]
    file_extension = os.path.splitext(output_audio_path)[1]
    nombre_audio=file_name+file_extension
    
    try:
        with sr.AudioFile(output_audio_path) as source:
            audio_data = recognizer.record(source)
            audio_text = recognizer.recognize_google(audio_data,language='es-ES')
    # except Exception as e:
    #     audio_text = f"Error al convertir el audio a texto: {str(e)}"
    except sr.RequestError as e:
        audio_text = f"Error al conectar con el servicio de reconocimiento de voz: {str(e)}"
    except sr.UnknownValueError:
        audio_text = "No se pudo entender el audio."
    except Exception as e:
        audio_text = f"Error al convertir el audio a texto: {str(e)}"
    
    return nombre_audio, audio_text
