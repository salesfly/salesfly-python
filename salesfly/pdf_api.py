class PDFAPI(object):
    """
    PDF API
    """

    def __init__(self, rest_client):
        self.rest_client = rest_client

    def create(self, options):
        return self.rest_client.post("/v1/pdf/create", options)
