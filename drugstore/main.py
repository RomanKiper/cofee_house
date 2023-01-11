from requests import Session

def post(json: dict, url: str) -> dict:
    with Session() as session:
        response = session.post(
            url=url,
            json=json
        )
        if response.status_code == 200:
            return response.json()

if __name__ == '__main__':
    print(post(
        {'username': "admin", 'password': 'admin'},
        "http://localhost:8000/api/v1/login/"
    ))

