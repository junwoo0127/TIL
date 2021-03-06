import os

# 1. 해당 파일들이 있는 위치로 이동
os.chdir(r'C:\Users\student\Desktop\TIL\00_startcamp\02_day\change_filenames')

# 2. 현재 폴더 안에 모든 파일 이름을 수집
filenames = os.listdir('.')  # 이미 위에서 폴더 위치로 이동했기 때문에 . 만 찍어서 폴더 위치 인식

# 3. 각가의 파일명을 돌면서 수정한다.
# for filename in filenames:
#     os.rename(filename, f'SAMSUNG_{filename}')

# 4. SAMSUNG 을 SSAFY로 변환
for filename in filenames:
    os.rename(filename, filename.replace('SAMSUNG', 'SSAFY'))