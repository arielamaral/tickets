import requests

class JiraService:
    def __init__(self, base_url, username, api_token):
        self.base_url = base_url
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        self.auth = (username, api_token)

    def get(self, endpoint):
        response = requests.get(f"{self.base_url}{endpoint}", headers=self.headers, auth=self.auth)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data):
        response = requests.post(f"{self.base_url}{endpoint}", headers=self.headers, auth=self.auth, json=data)
        response.raise_for_status()
        return response.json()

    def put(self, endpoint, data):
        response = requests.put(f"{self.base_url}{endpoint}", headers=self.headers, auth=self.auth, json=data)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint):
        response = requests.delete(f"{self.base_url}{endpoint}", headers=self.headers, auth=self.auth)
        response.raise_for_status()
        return response.status_code

    def create_issue(self, project_key, summary, description, issue_type):
        data = {
            "fields": {
                "project": {
                    "key": project_key
                },
                "summary": summary,
                "description": description,
                "issuetype": {
                    "name": issue_type
                }
            }
        }
        return self.post("/issue", data)

    def update_issue(self, issue_key, fields):
        data = {"fields": fields}
        return self.put(f"/issue/{issue_key}", data)

    def get_issue(self, issue_key):
        return self.get(f"/issue/{issue_key}")

    def delete_issue(self, issue_key):
        return self.delete(f"/issue/{issue_key}")