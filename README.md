🎤 DictarPython
DictarPython es una aplicación de escritorio en Python que permite grabar audio, transcribirlo automáticamente a texto usando la API de Groq (modelo Whisper), y pegar la transcripción en cualquier aplicación activa.

🚀 Características principales
Grabación de audio manteniendo presionada la tecla Insertar.
Transcripción automática del audio a texto en español usando Groq Whisper.
Copia y pegado automático de la transcripción en la aplicación activa.
Gestión segura de claves mediante un archivo .env (no se sube a GitHub).

🛠️ Instalación y configuración
Clona este repositorio:

Crea y activa un entorno virtual:

Instala las dependencias:

Crea un archivo .env en la raíz del proyecto con tu clave de API:
Pagina para obtener tu clave de Api: https://groq.com/

Asegúrate de que el archivo .env está en tu .gitignore:

🖥️ Uso
Ejecuta la aplicación:

Mantén presionada la tecla Insertar para grabar audio.

Suelta la tecla para detener la grabación.

El audio se transcribe automáticamente y el texto se copia y pega en la aplicación activa.

Repite el proceso tantas veces como quieras.

📦 Dependencias principales
# pip install pyaudio keyboard pyperclip pyautogui python-dotenv groq
pyaudio
keyboard
pyperclip
pyautogui
python-dotenv
groq
🔒 Seguridad
La clave de API se almacena en .env y nunca se sube a GitHub.
No compartas tu archivo .env ni tu clave de API.
✨ Créditos
Desarrollado por Luis Alvarez.
