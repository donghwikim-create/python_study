# 모듈을 읽어 들입니다.
import os

# 폴더를 읽어 들이는 함수
def read_folder(path):
    # 폴더의 요소 읽어 들이기
    output = os.listdir(path)
    
    # 폴더의 요소 구분하기
    for item in output:
        # 상위 폴더 경로와 현재 아이템(파일/폴더명)을 합쳐서 전체 경로를 만듭니다.
        full_path = os.path.join(path, item)
        
        # 만약 폴더(디렉토리)라면 재귀적으로 다시 함수를 호출합니다.
        if os.path.isdir(full_path):
            read_folder(full_path)
        else:
            # 파일이라면 출력하기
            print("파일:", item)
    
# 현재 폴더의 파일/폴더를 출력합니다.
read_folder(".")