ffmpeg -i "%~1" -ar 16000 -ac 1 -c:a pcm_s16le "%~1.wav"
main.exe -m C:\Users\SUKHMAN\Desktop\Coding\Whisper\ggml-model-whisper-base.en.bin "%~1.wav" -otxt