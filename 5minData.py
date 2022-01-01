import pandas as pd

asos_codes = ['159', '156', '155', '152', '143', '138', '133', '131', '119', '112', '108']
years = ['2018', '2019', '2020', '2021']
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '12']

df2 = pd.DataFrame(['지점', '일시', '기온(°C)', '누적강수량(mm)', '풍향(deg)', '풍속(m/s)', '현지기압(hPa)', '해면기압(hPa)', '습도(%)',
                    '일사(MJ/m^2)', '일조(Sec)'])

for asos_code in asos_codes:
    for year in years:
        for month in months:
            if(month == '12'):
                if(year == '2020'):
                    title = 'SURFACE_ASOS_RawData\MIN\SURFACE_ASOS_' + asos_code + '_MI_' + year + '-' + month + '_' + year + '-' + month + '_' + year + '.csv'
                elif(year == '2021'):
                    continue
                else:
                    title = title = 'SURFACE_ASOS_RawData\MIN\SURFACE_ASOS_' + asos_code + '_MI_' + year + '-' + month + '_' + year + '-' + month + '_' + str(int(year)+1) + '.csv'
            else:
                title = 'SURFACE_ASOS_RawData\MIN\SURFACE_ASOS_' + asos_code + '_MI_' + year + '-' + month + '_' + year + '-' + month + '_' + year + '.csv'
            df1 = pd.read_csv(title)
            df2 = pd.concat([df1, df2])
            
                    
            
            
            
#SURFACE_ASOS_108_MI_2019-09_2019-09_2019.csv