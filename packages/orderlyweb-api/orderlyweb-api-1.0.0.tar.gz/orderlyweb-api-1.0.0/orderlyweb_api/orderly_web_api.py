from orderlyweb_api.result_models import ReportStatusResult, VersionDetails

from orderlyweb_api.orderly_web_response_error import OrderlyWebResponseError
import requests
import json


class OrderlyWebAPI:
    def __init__(self, base_url, auth_provider_token):
        self.base_url = base_url
        auth_url = self.build_url('login/')
        headers = {'Authorization': 'token {}'.format(auth_provider_token)}
        response = requests.post(auth_url, headers=headers)
        if response.status_code != 200:
            raise OrderlyWebResponseError(response)
        self.access_token = response.json()['access_token']

    def run_report(self, report, params, timeout=600):
        url = 'reports/{}/run/?timeout={}'.format(report, timeout)
        result = self.post(url, json.dumps({'params': params}))
        return result['key']

    def publish_report(self, name, version):
        url = 'reports/{}/versions/{}/publish/'.format(name, version)
        return self.post(url, None)

    def report_status(self, key):
        data = self.get('reports/{}/status/'.format(key))
        return ReportStatusResult(data)

    def kill_report(self, key):
        self.delete('reports/{}/kill/'.format(key))

    def report_versions(self, name):
        return self.get('reports/{}'.format(name))

    def version_details(self, name, version):
        data = self.get('reports/{}/versions/{}/'.format(name, version))
        return VersionDetails(data)

    def post(self, route, data):
        headers = self.headers()
        url = self.build_url(route)
        response = requests.post(url, data=data, headers=headers)
        return self.handle_response(response)

    def get(self, route):
        headers = self.headers()
        url = self.build_url(route)
        response = requests.get(url, headers=headers)
        return self.handle_response(response)

    def delete(self, route):
        headers = self.headers()
        url = self.build_url(route)
        response = requests.delete(url, headers=headers)
        if response.status_code != 200 and response.status_code != 400:
            raise OrderlyWebResponseError(response)
        # TODO: we should handle_response to raise error if result is not 200 -
        # but do that after issue in orderly-server which returns 400 from a
        # successful kill

    def headers(self):
        return {'Authorization': 'Bearer {}'.format(self.access_token)}

    def build_url(self, route):
        return '{}/api/v2/{}'.format(self.base_url, route)

    @staticmethod
    def handle_response(response):
        if response.status_code != 200:
            raise OrderlyWebResponseError(response)
        return response.json()['data']
