import time
from datetime import datetime
from pytz import timezone

# utilizando a Lib TIME
# print(time.localtime())
# print(time.localtime().tm_year)
# print(f'{time.localtime().tm_mday}/ {time.localtime().tm_mon}/ {time.localtime().tm_year}') # função manual para separar dia/mes/ano


# utilizando a Lib DATETIME
# print(datetime.today()) # buscar data completa
# print(datetime.now().date())# buscar apenas data
# print(datetime.now().time())# buscar apenas o tempo
# utilizando a Lib PYTZ
dthr = datetime.now()
fuso_sp = timezone ('America/Sao_Paulo')
fuso_africa= timezone ('Africa/abidjan')
fuso_tokio= timezone ('Asia/Tokyo')
fuso_mexico= timezone ('America/Mexico_city')

dt_tz=dthr.astimezone(fuso_mexico)
dt_formatada = dt_tz.strftime('fuso de mexico -> dia %d/ mes %m/ ano %Y.hora%H/ minuto%M')
print(dt_formatada)
