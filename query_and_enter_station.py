from atomic_queries import _query_orders, _enter_station
from utils import random_from_list


def query_and_enter_station(headers):
    pairs = _query_orders(headers=headers, types=tuple([2]))
    pairs2 = _query_orders(headers=headers, types=tuple([2]), query_other=True)

    if not pairs and not pairs2:
        return

    pairs = pairs + pairs2

    # (orderId, tripId)
    pair = random_from_list(pairs)

    order_id = _enter_station(order_id=pair[0], headers=headers)
    if not order_id:
        return

    print(f"{order_id} queried and entered station")


if __name__ == '__main__':
    headers = {
        "Cookie": "JSESSIONID=C2FBC9F942C500363720049872A91AC3; YsbCaptcha=396BC310EE694084B10A12A5DDBFBD24",
        #"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTY4MTA5MzQ3NSwiZXhwIjoxNjgxMDk3MDc1fQ.JSiwEK47KF4vmWwbNNQo5pPY9XLQxm4TawgBMQDHJEI",
        "Content-Type": "application/json"
    }
    query_and_enter_station(headers=headers)
