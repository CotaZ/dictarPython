import os
import tempfile
import wave
import pyaudio
import keyboard
import pyperclip
import pyautogui
from dotenv import load_dotenv
from groq import Groq

load_dotenv()  # Cargar las variables de entorno desde el archivo .env
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def grabar_audio(frecuencia_muestreo=16000, canales=1, fragmento=1024):
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=canales,
        rate=frecuencia_muestreo,
        input=True,
        frames_per_buffer=fragmento,)
    print("Presiona y manten presionado 'Insertar' para comenzar a grabar...")
    frames = []
    keyboard.wait('insert')
    print("Grabando... (Suelta Insertar para detener)")
    while keyboard.is_pressed('insert'):
        data = stream.read(fragmento)
        frames.append(data)
    print("Grabación finalizada.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    return frames, frecuencia_muestreo 
    
def guardar_audio(frames, frecuencia_muestreo):
    with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as audio_temp:
        wf = wave.open(audio_temp.name, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
        wf.setframerate(frecuencia_muestreo)
        wf.writeframes(b''.join(frames))
        wf.close()
        return audio_temp.name

def transcribir_audio(ruta_archivo_audio):
    try:
        with open(ruta_archivo_audio, 'rb') as archivo:
            transcripcion = client.audio.transcriptions.create(
                file=(os.path.basename(ruta_archivo_audio), archivo.read()),
                model="whisper-large-v3",
                prompt="""el audito es de una persona normal trabajando""",
                response_format="text",
                language="es",
            )
        return transcripcion
    except Exception as e:
        print(f"Error al transcribir el audio: {e}")
        return None

def copiar_transcripcion_al_portapapeles(texto):
    pyperclip.copy(texto)
    pyautogui.hotkey("ctrl", "v")
    
def main():
    while True:
        frames, frecuencia_muestreo = grabar_audio()
        archivo_audio_temp = guardar_audio(frames, frecuencia_muestreo)
        print("Transcribiendo audio...")
        transcripcion = transcribir_audio(archivo_audio_temp)
        if transcripcion:
            print("\nTranscripción:")
            print("Copiando transcripcion al portapapeles.")
            copiar_transcripcion_al_portapapeles(transcripcion)
            print("Transcripción copiada al portapapeles y pegada en la aplicacion.")
        else:
            print("No se pudo transcribir, porque falló.")
        os.unlink(archivo_audio_temp)
        print("\nListo para la próxima grabación. Presiona 'Insertar' para comenzar de nuevo.")
        
if __name__ == "__main__":
    main()
    
