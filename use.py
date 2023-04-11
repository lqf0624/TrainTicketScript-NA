import logging

from atomic_queries import _query_admin_basic_price
from queries import Query
from scenarios import query_and_preserve


url = "http://10.26.65.242:32677"
# login train-ticket and store the cookies
q = Query(url)
if not q.login():
    logging.fatal('login failed')

if __name__ == '__main__':
    # execute scenario on current user
    q.query_food()