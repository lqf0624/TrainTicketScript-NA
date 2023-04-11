from atomic_queries import _query_orders, _collect_one_order, _login, _rebook_ticket
from utils import random_from_list
import time

base_address = "http://10.26.65.242:32677"


def query_and_rebook(headers):

    pairs = _query_orders(headers=headers, types=tuple([1]))
    #pairs2 = _query_orders(headers=headers, types=tuple([1]), query_other=True)

    # if not pairs and not pairs2:
    #     return

    # pairs = pairs + pairs2

    # (orderId, tripId)
    # pair = random_form_list(pairs)
    new_trip_id = "D1345"
    new_date = time.strftime("%Y-%m-%d", time.localtime())
    new_seat_type = "3"

    for pair in pairs: 
        #print(pair)
        _rebook_ticket(old_order_id=pair[0], old_trip_id=pair[1], new_trip_id=new_trip_id, new_date=new_date, new_seat_type=new_seat_type, headers=headers)





if __name__ == '__main__':
    _, token = _login()

    headers = {
        "Cookie": "JSESSIONID=C2FBC9F942C500363720049872A91AC3; YsbCaptcha=396BC310EE694084B10A12A5DDBFBD24",
        "Authorization": "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTY4MTA5MzQ3NSwiZXhwIjoxNjgxMDk3MDc1fQ.JSiwEK47KF4vmWwbNNQo5pPY9XLQxm4TawgBMQDHJEI",
        "Content-Type": "application/json"
    }
    headers["Authorization"] = "Bearer " + token
    
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    query_and_rebook(headers=headers)

    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    print(f"start:{start_time} end:{end_time}")