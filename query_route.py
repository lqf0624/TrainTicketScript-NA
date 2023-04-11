from atomic_queries import _query_route

if __name__ == '__main__':
    headers = {
        "Cookie": "grafana_user=admin; grafana_remember=f3742a917102e9af9853e3f3cba72af9ccbe003ae3d0942da7b19ae732c450bd90; grafana_sess=a06913a72a0472dd; JSESSIONID=B002CEDCBDE33060245408B5EC037FD5; YsbCaptcha=0312AF0347BB4184915ED9E61C49C928",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTY4MTE5ODgwNiwiZXhwIjoxNjgxMjAyNDA2fQ.T1VXQGkO0CbWZd092OM59VaMUMO2GSY_T15vA5f9i1Y",
        "Content-Type": "application/json"
    }

    _query_route(headers=headers)
