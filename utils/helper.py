import json

import allure
from allure_commons.types import AttachmentType


class Helper:

    def attach_response(self, response):
        allure.attach(
            body=json.dumps(response, indent=4),
            name="API Response",
            attachment_type=AttachmentType.JSON
        )
