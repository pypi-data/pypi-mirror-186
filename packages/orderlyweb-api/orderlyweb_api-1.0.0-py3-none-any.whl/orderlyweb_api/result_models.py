class ReportStatusResult:
    def __init__(self, response_data):
        self.status = response_data["status"]
        self.version = response_data["version"]
        self.output = response_data["output"]
        self.success = self.status == "success"
        self.finished = self.status.lower() not in ["running", "queued"]
        self.fail = self.finished and not self.success


class VersionDetails:
    def __init__(self, response_data):
        self.name = response_data['name']
        self.id = response_data['id']
        self.description = response_data['description']
        self.display_name = response_data['display_name']
        self.published = response_data['published']
        self.date = response_data['date']
        self.artefacts = response_data['artefacts']
        self.resources = response_data['resources']
        self.data_info = response_data['data_info']
        self.parameter_values = response_data['parameter_values']
