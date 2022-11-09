import json
import requests

## Harness Manger Variables
account_id = 'REDACTED'
headers = {"x-api-key": "REDACTED"}
organization_id = 'default'
project_id = 'sandbox'  

## Harness service accounts examples

# create a service account
body = {
  "identifier": "service_account_1",
  "name": "service_account_1",
  "email": "francisco.piva+sa1@harness.io",
  "description": "this service account was created via API",
  "accountIdentifier": account_id,
  "orgIdentifier": organization_id,
  "projectIdentifier": project_id
}
url = f"https://app.harness.io/gateway/ng/api/serviceaccount?accountIdentifier={account_id}&orgIdentifier={organization_id}&projectIdentifier={project_id}"
request = requests.post(url, json=body, headers=headers)
print(json.dumps(json.loads(request.text), indent=2))

# delate a service account
url = f"https://app.harness.io/gateway/ng/api/serviceaccount/service_account_1?accountIdentifier={account_id}&orgIdentifier={organization_id}&projectIdentifier={project_id}"
request = requests.delete(url, headers=headers)
print(json.dumps(json.loads(request.text), indent=2))
