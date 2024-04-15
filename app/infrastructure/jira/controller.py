from flask import Blueprint, request, jsonify
from app.infrastructure.jira.services import JiraService

jira = Blueprint('jira', __name__)

jira_service = JiraService(base_url="https://your-domain.atlassian.net/rest/servicedeskapi/", username="your-username", api_token="your-api-token")

@jira.route('/issue', methods=['POST'])
def create_issue():
    data = request.get_json()
    response = jira_service.create_issue(data['project_key'], data['summary'], data['description'], data['issue_type'])
    return jsonify(response), 201

@jira.route('/issue/<issue_key>', methods=['PUT'])
def update_issue(issue_key):
    data = request.get_json()
    response = jira_service.update_issue(issue_key, data['fields'])
    return jsonify(response), 200

@jira.route('/issue/<issue_key>', methods=['GET'])
def get_issue(issue_key):
    response = jira_service.get_issue(issue_key)
    return jsonify(response), 200

@jira.route('/issue/<issue_key>', methods=['DELETE'])
def delete_issue(issue_key):
    jira_service.delete_issue(issue_key)
    return '', 204