import logging
import time

from atomic_queries import _query_admin_basic_config

logger = logging.getLogger("query_and_preserve")
# The UUID of user fdse_microservice is that
uuid = "4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f"
date = time.strftime("%Y-%m-%d", time.localtime())

base_address = "http://10.26.65.242:31000"


def query_admin_basic_config(headers):
    _query_admin_basic_config(headers=headers)


if __name__ == '__main__':
    cookie = "JSESSIONID=C2FBC9F942C500363720049872A91AC3; YsbCaptcha=396BC310EE694084B10A12A5DDBFBD24"
    Authorization = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTY4MTA5MzQ3NSwiZXhwIjoxNjgxMDk3MDc1fQ.JSiwEK47KF4vmWwbNNQo5pPY9XLQxm4TawgBMQDHJEI"
    headers = {
        'Connection': 'keep-alive',
        "Cookie": f"{cookie}",
        #"Authorization": f"Bearer {Authorization}",
        "Content-Type": "application/json"
    }

    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    for i in range(1000):
        try:
            query_admin_basic_config(headers=headers)
            print("*****************************INDEX:" + str(i))
        except Exception as e:
            print(e)

    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    print(f"start:{start_time} end:{end_time}")
