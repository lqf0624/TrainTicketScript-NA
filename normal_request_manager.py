from query_and_preserve import query_and_preserve
from query_order_and_pay import query_order_and_pay
from query_and_collect_ticket import query_and_collect_ticket
from query_and_enter_station import query_and_enter_station
from query_and_cancel import query_one_and_cancel

from atomic_queries import _login, _query_orders, _query_high_speed_ticket

from utils import random_boolean
import time

from threading import Thread


def main():
    headers = {
        "Cookie": "grafana_user=admin; grafana_remember=f3742a917102e9af9853e3f3cba72af9ccbe003ae3d0942da7b19ae732c450bd90; grafana_sess=a06913a72a0472dd; JSESSIONID=B002CEDCBDE33060245408B5EC037FD5; YsbCaptcha=8CB6736CFDAE445EAD36699B2DA2B2B0",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTY4MTE5ODgwNiwiZXhwIjoxNjgxMjAyNDA2fQ.T1VXQGkO0CbWZd092OM59VaMUMO2GSY_T15vA5f9i1Y",
        "Content-Type": "application/json"
    }

    for i in range(30):
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"now_time:{now_time}")

        if i % 20 == 0:
            uid, token = _login()
            if uid is not None and token is not None:
                headers['Authorization'] = "Bearer " + token

        print(f"idx:{i}")
        query_and_preserve(headers1=headers)

        # 1/4 几率取消
        if random_boolean() and random_boolean():
            query_one_and_cancel(headers)
        else:
            query_order_and_pay(headers)
            query_and_collect_ticket(headers)
            query_and_enter_station(headers)


def main_thread():
    threads = []

    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"start:{start_time}")

    for i in range(5):
        t = Thread(name="thread" + str(i), target=main)
        time.sleep(1)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"start:{start_time} end:{end_time}")


def query_order():
    headers = {
        "Cookie": "grafana_user=admin; grafana_remember=f3742a917102e9af9853e3f3cba72af9ccbe003ae3d0942da7b19ae732c450bd90; grafana_sess=a06913a72a0472dd; JSESSIONID=B002CEDCBDE33060245408B5EC037FD5; YsbCaptcha=8CB6736CFDAE445EAD36699B2DA2B2B0",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTY4MTE5ODgwNiwiZXhwIjoxNjgxMjAyNDA2fQ.T1VXQGkO0CbWZd092OM59VaMUMO2GSY_T15vA5f9i1Y",
        "Content-Type": "application/json"
    }
    uid, token = _login()
    if uid is not None and token is not None:
        headers['Authorization'] = "Bearer " + token

    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"start:{start_time}")

    for i in range(50):
        pairs = _query_orders(headers=headers, types=tuple([0, 1]), query_other=False)
        print(pairs)

    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"start:{start_time} end:{end_time}")


def query_tickets():
    headers = {
        "Cookie": "JSESSIONID=C2FBC9F942C500363720049872A91AC3; YsbCaptcha=396BC310EE694084B10A12A5DDBFBD24",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTY4MTA5MzQ3NSwiZXhwIjoxNjgxMDk3MDc1fQ.JSiwEK47KF4vmWwbNNQo5pPY9XLQxm4TawgBMQDHJEI",
        "Content-Type": "application/json"
    }
    uid, token = _login()
    if uid is not None and token is not None:
        headers['Authorization'] = "Bearer " + token


    date = time.strftime("%Y-%m-%d", time.localtime())

    start = "Shang Hai"
    end = "Su Zhou"
    high_speed_place_pair = (start, end)

    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"start:{start_time}")

    for i in range(50):
        trip_ids = _query_high_speed_ticket(place_pair=high_speed_place_pair, headers=headers,time=date)
        print(trip_ids)

    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"start:{start_time} end:{end_time}")


if __name__ == '__main__':
    main_thread()

