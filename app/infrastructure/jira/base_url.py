import os
from app.infrastructure.jira.services import JiraService

base_url = "https://your-domain.atlassian.net/rest/servicedeskapi/"
username = os.getenv('JIRA_USERNAME')
api_token = os.getenv('JIRA_API_TOKEN')

jira_service = JiraService(base_url=base_url, username=username, api_token=api_token)