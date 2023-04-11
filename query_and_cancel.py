from atomic_queries import _query_orders, _cancel_one_order
from utils import random_from_list


def query_one_and_cancel(headers, uuid="4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f"):
    """
    查询order并取消order
    :param uuid:
    :param headers:
    :return:
    """
    pairs = _query_orders(headers=headers, types=tuple([0, 1]))
    pairs2 = _query_orders(headers=headers, types=tuple([0, 1]), query_other=True)

    if not pairs and not pairs2:
        return

    pairs = pairs + pairs2

    # (orderId, tripId) pair
    pair = random_from_list(pairs)

    order_id =_cancel_one_order(order_id=pair[0], uuid=uuid, headers=headers)
    if not order_id:
        return

    print(f"{order_id} queried and canceled")


if __name__ == '__main__':
    headers = {
        "Cookie": "JSESSIONID=C2FBC9F942C500363720049872A91AC3; YsbCaptcha=396BC310EE694084B10A12A5DDBFBD24",
        #"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTY4MTA5MzQ3NSwiZXhwIjoxNjgxMDk3MDc1fQ.JSiwEK47KF4vmWwbNNQo5pPY9XLQxm4TawgBMQDHJEI",
        "Content-Type": "application/json"
    }
    uuid = "4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f"

    query_one_and_cancel(headers=headers,
                         uuid=uuid,)
