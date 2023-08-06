from requests.models import Response
import json

def response_return(response: Response):
  if not response.ok:
    status_message = 'Request failed with status ' + str(response.status_code)
    detail_message = ' with the message "' + str(json.loads(response.text)["detail"]) + '"'
    message = status_message + detail_message
    raise Exception(message)
  return True
