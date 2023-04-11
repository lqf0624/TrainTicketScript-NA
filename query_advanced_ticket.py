from atomic_queries import _query_advanced_ticket, _login

import logging
import random
import time

logger = logging.getLogger("query_advanced_ticket")
# The UUID of user fdse_microservice is that
uuid = "4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f"
date = time.strftime("%Y-%m-%d", time.localtime())

base_address = "http://10.26.65.242:32677"

if __name__ == '__main__':
    _, token = _login()
    cookie = "grafana_user=admin; grafana_remember=f3742a917102e9af9853e3f3cba72af9ccbe003ae3d0942da7b19ae732c450bd90; grafana_sess=a06913a72a0472dd; JSESSIONID=5D1FF5A3CECAF9DB0046446E704F001C; YsbCaptcha=A3EC4857A6304ACEADADB2EB1F968F8C"
    # Authorization = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTY4MTA5MzQ3NSwiZXhwIjoxNjgxMDk3MDc1fQ.JSiwEK47KF4vmWwbNNQo5pPY9XLQxm4TawgBMQDHJEI"
    headers = {
        "Cookie": f"{cookie}",
        # "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62"
    }

    #start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    start_time = "2023-04-11 00:00:00"
    place_pairs = [("Shang Hai", "Su Zhou"),
                   ("Su Zhou", "Shang Hai"),
                   ("Nan Jing", "Shang Hai")]
    types = ["cheapest", "minStation", "quickest"]
    for i in range(2):
        type = random.choice(types)
        place_pair = random.choice(place_pairs)
        print(f"search {type} between {place_pair[0]} to {place_pair[1]}")
        try:
            trip_ids = _query_advanced_ticket(place_pair=place_pair, headers=headers, time=date, type=type)
            print(f"get {len(trip_ids)} routes.")
            print("*****************************INDEX:" + str(i))
        except Exception as e:
            print(e)

    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    print(f"start:{start_time} end:{end_time}")
