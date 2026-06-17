import wave

# WAV 파일 정보 읽기
try:
    with wave.open("audio.wav", "rb") as wav_file:
        print(f"채널 수: {wav_file.getnchannels}")
        print(f"샘플 레이트: {wav_file.getframerate}Hz")
except:
    print("오디오 파일이 없습니다.")
