from pathlib import Path

# 현재 디렉토리에서 'logs' 폴더 안의 'app.log' 파일 경로 생성
log_file = Path.cwd() / "logs" / "app.log"

if not log_file.exists():
    print("로그 파일이 존재하지 않습니다.")