class OrderlyWebResponseError(Exception):
    def __init__(self, response):
        self.response = response
        json = response.json()
        msg = "An OrderlyWeb error occurred"
        if "errors" in json and len(json["errors"]) > 0:
            error = json["errors"][0]
            if "detail" in error:
                msg = error["detail"]
            elif "error" in error:
                msg = error["error"]

        super(Exception, self).__init__(msg)
