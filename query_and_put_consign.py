import time

from atomic_queries import _query_orders_all_info, _put_consign
from utils import random_from_list


def query_one_and_put_consign(headers, pairs):
    """
    查询order并put consign
    :param uuid:
    :param headers:
    :return:
    """

    pair = random_from_list(pairs)

    order_id = _put_consign(result=pair, headers=headers)
    if not order_id:
        return

    print(f"{order_id} queried and put consign")


if __name__ == '__main__':
    cookie = "JSESSIONID=C2FBC9F942C500363720049872A91AC3; YsbCaptcha=396BC310EE694084B10A12A5DDBFBD24"
    Authorization = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTY4MTA5MzQ3NSwiZXhwIjoxNjgxMDk3MDc1fQ.JSiwEK47KF4vmWwbNNQo5pPY9XLQxm4TawgBMQDHJEI"
    headers = {
        'Connection': 'close',
        "Cookie": f"{cookie}",
        "Authorization": f"Bearer {Authorization}",
        "Content-Type": "application/json"
    }
    uuid = "4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f"

    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    pairs = _query_orders_all_info(headers=headers)
    pairs2 = _query_orders_all_info(headers=headers, query_other=True)

    pairs = pairs + pairs2

    for i in range(330):
        try:
            query_one_and_put_consign(headers=headers, pairs=pairs)
            print("*****************************INDEX:" + str(i))
        except Exception as e:
            print(e)

    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    print(f"start:{start_time} end:{end_time}")
