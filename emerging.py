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

csv = pd.read_csv('emerging_data_set.csv')
csv['Date'] = pd.to_datetime(csv['Date'])
csv = csv.set_index('Date')
print(csv.index.dtype)

emerging_tikers = [
                ('인도 센섹스','BSESN'),
                ('상해종합','SSEC'),
                ('한국 코스피','KS11'),
                ('브라질 보베스파','BVSP'),
                ('러시아','IMOEX'),
                ('인도네시아','FTWIIDNL')
                ]

emerging_desc = [desc for desc, ticker in emerging_tikers] # 데이터 설명.

emerging = csv.loc[:, emerging_desc]

# emerging = emerging.loc['2013-1-31':'2016-12-31']
# print(emerging)

plt.rcParams["figure.figsize"] = (14,7)
plt.rcParams['axes.grid'] = True

emerging00 = emerging.loc['2013-1-31':'2017-12-31']
emerging00 = emerging00.pct_change()
emerging00 = (1+emerging00).cumprod()-1
emerging00.loc['2013-01-31'] = 0
emerging00.plot()
plt.show()


# emerging.plot()
emerging13 = emerging.loc['2013-1-31':'2013-12-31']
emerging13 = emerging13.pct_change()
emerging13 = (1+emerging13).cumprod()-1
emerging13.loc['2013-01-31'] = 0
emerging13.bar()
plt.show()

emerging14 = emerging.loc['2014-1-31':'2014-12-31']
emerging14 = emerging14.pct_change()
emerging14 = (1+emerging14).cumprod()-1
emerging14.loc['2014-01-31'] = 0
emerging14.bar()
plt.show()

emerging15 = emerging.loc['2015-1-31':'2015-12-31']
emerging15 = emerging15.pct_change()
emerging15 = (1+emerging15).cumprod()-1
emerging15.loc['2015-01-31'] = 0
emerging15.bar()
plt.show()

emerging16 = emerging.loc['2016-1-31':'2016-12-31']
emerging16 = emerging16.pct_change()
emerging16 = (1+emerging16).cumprod()-1
emerging16.loc['2016-01-31'] = 0
emerging16.bar()
plt.show()

save = emerging.iloc[-1]
print(save)
# save.to_csv('sec.csv', encoding='euc-kr')
