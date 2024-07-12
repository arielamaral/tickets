import requests

class BasicUrl:
    def __init__(self, url):
        self.url = url

    def get(self):
        return requests.get(self.url)

    @staticmethod
    def jira_instance():
        jira_url = "https://your-jira-url.com"
        return BasicUrl(jira_url)