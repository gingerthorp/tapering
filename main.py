import pandas
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import platform


# 운용체제 환경에 따라 글꼴 선택.
osSelect = platform.system()
if osSelect == 'Windows':
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
elif osSelect == 'Darwin':
    rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False
csv = pd.read_csv('result_data(2000).csv', encoding='euc-kr')
csv.index = csv['DATE']


kor_index_tikers = [
(1150, '코스피 200 커뮤니케이션서비스'),
(1151, '코스피 200 건설'),
(1152, '코스피 200 중공업'),
(1153, '코스피 200 철강/소재'),
(1154, '코스피 200 에너지/화학'),
(1155, '코스피 200 정보기술'),
(1156, '코스피 200 금융'),
(1157, '코스피 200 생활소비재'),
(1158, '코스피 200 경기소비재'),
(1159, '코스피 200 산업재'),
(1160, '코스피 200 헬스케어'),
(2212, '코스닥 150 소재'),
(2213, '코스닥 150 산업재'),
(2214, '코스닥 150 필수소비재'),
(2215, '코스닥 150 자유소비재'),
(2216, '코스닥 150 정보기술'),
(2217, '코스닥 150 헬스케어'),
(2218, '코스닥 150 커뮤니케이션서비스')
]
kor_index_desc = [desc for ticker,desc in kor_index_tikers] # 데이터 설명.

kor_sec = csv.loc[:,kor_index_desc]
kor_sec = kor_sec.loc['2014':'2014-12-31']

kor_sec = kor_sec.pct_change()
kor_sec = (1+kor_sec).cumprod()-1
kor_sec.loc['2014-01-31'] = 0
print(kor_sec.iloc[-1])
save = kor_sec.iloc[-1]
save.to_csv('sec.csv', encoding='euc-kr')
plt.rcParams["figure.figsize"] = (28,14)
plt.rcParams['axes.grid'] = True

kor_sec.plot()
plt.show()