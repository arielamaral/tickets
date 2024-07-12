import app.infrastructure.jira.basic_url as BasicUrl

class Authentication:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get(self):
        return BasicUrl.BasicUrl.jira_instance().get()