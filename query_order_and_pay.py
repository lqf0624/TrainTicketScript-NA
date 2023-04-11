import time

from atomic_queries import _query_orders, _pay_one_order
from utils import random_from_list


def query_order_and_pay(headers, pairs):
    """
    查询Order并付款未付款Order
    :return:
    """

    # (orderId, tripId) pair
    pair = random_from_list(pairs)

    order_id = _pay_one_order(pair[0], pair[1], headers=headers)
    if not order_id:
        return

    print(f"{order_id} queried and paid")


if __name__ == '__main__':
    cookie = "grafana_user=admin; grafana_remember=f3742a917102e9af9853e3f3cba72af9ccbe003ae3d0942da7b19ae732c450bd90; grafana_sess=a06913a72a0472dd; JSESSIONID=B002CEDCBDE33060245408B5EC037FD5; YsbCaptcha=0312AF0347BB4184915ED9E61C49C928"
    Authorization = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTY4MTE5ODgwNiwiZXhwIjoxNjgxMjAyNDA2fQ.T1VXQGkO0CbWZd092OM59VaMUMO2GSY_T15vA5f9i1Y"
    headers = {
        'Connection': 'close',
        "Cookie": f"{cookie}",
        "Authorization": f"Bearer {Authorization}",
        "Content-Type": "application/json"
    }

    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    pairs = _query_orders(headers=headers, types=tuple([0, 1]))
    pairs2 = _query_orders(headers=headers, types=tuple([0, 1]), query_other=True)

    pairs = pairs + pairs2

    for i in range(330):
        try:
            query_order_and_pay(headers=headers, pairs=pairs)
            print("*****************************INDEX:" + str(i))
        except Exception as e:
            print(e)

    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    print(f"start:{start_time} end:{end_time}")
