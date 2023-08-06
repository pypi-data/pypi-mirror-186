# 0.0.1
import datetime

def get_now(Y=True, Mon=True, D=True, H=True, Min=True, S=True):
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))) # 日本時間
    return now.strftime('%Y%m%d%H%M%S')  # yyyyMMddHHmmss

