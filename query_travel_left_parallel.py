from atomic_queries import _query_high_speed_ticket, _query_normal_ticket, _query_high_speed_ticket_parallel
from utils import random_boolean

import logging
import time

logger = logging.getLogger("query_and_preserve")
# The UUID of user fdse_microservice is that
uuid = "4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f"
date = time.strftime("%Y-%m-%d", time.localtime())

base_address = "http://10.26.65.242:31000"


def query_travel_left_parallel(headers):
    """
    1. 查票（随机高铁或普通）
    2. 查保险、Food、Contacts
    3. 随机选择Contacts、保险、是否买食物、是否托运
    4. 买票
    :return:
    """
    start = ""
    end = ""
    trip_ids = []
    PRESERVE_URL = ""

    start = "Su Zhou"
    end = "Shang Hai"
    high_speed_place_pair = (start, end)
    trip_ids = _query_high_speed_ticket_parallel(place_pair=high_speed_place_pair, headers=headers, time=date)


if __name__ == '__main__':

    cookie = "grafana_user=admin; grafana_remember=f3742a917102e9af9853e3f3cba72af9ccbe003ae3d0942da7b19ae732c450bd90; grafana_sess=a06913a72a0472dd; JSESSIONID=B002CEDCBDE33060245408B5EC037FD5; YsbCaptcha=0312AF0347BB4184915ED9E61C49C928"
    Authorization = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTY4MTE5ODgwNiwiZXhwIjoxNjgxMjAyNDA2fQ.T1VXQGkO0CbWZd092OM59VaMUMO2GSY_T15vA5f9i1Y"
    headers = {
        'Connection': 'keep-alive',
        "Cookie": f"{cookie}",
        "Authorization": f"Bearer {Authorization}",
        "Content-Type": "application/json"
    }

    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"start:{start_time}")

    for i in range(320):
        try:
            query_travel_left_parallel(headers=headers)
            print("*****************************INDEX:" + str(i))
        except Exception as e:
            print(e)
    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    print(f"start:{start_time} end:{end_time}")
