import logging
import time

from atomic_queries import _query_admin_basic_price

logger = logging.getLogger("query_and_preserve")
# The UUID of user fdse_microservice is that
uuid = "4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f"
date = time.strftime("%Y-%m-%d", time.localtime())

base_address = "http://10.26.65.242:32677"


def query_admin_basic_price(headers):
    _query_admin_basic_price(headers=headers)


if __name__ == '__main__':
    cookie = "grafana_user=admin; grafana_remember=f3742a917102e9af9853e3f3cba72af9ccbe003ae3d0942da7b19ae732c450bd90; grafana_sess=a06913a72a0472dd; JSESSIONID=8BC172A4EA2D7279826DE2A869423052"
    Authorization = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTY4MTA5MzQ3NSwiZXhwIjoxNjgxMDk3MDc1fQ.JSiwEK47KF4vmWwbNNQo5pPY9XLQxm4TawgBMQDHJEI"
    headers = {
        "Cookie": f"{cookie}",
        #"Authorization": f"Bearer {Authorization}",
        "Content-Type": "application/json",
        "Connection" : "keep-alive",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62"
    }

    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    for i in range(1000):
        try:
            query_admin_basic_price(headers=headers)
            print("*****************************INDEX:" + str(i))
        except Exception as e:
            print(e)
    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    print(f"start:{start_time} end:{end_time}")
