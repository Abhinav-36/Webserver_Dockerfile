import json
import requests

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNTBkMGIwY2ItZTRiMS00ZjIxLWExNTQtY2I1OTg2MmIwYzBiIiwidHlwZSI6ImFwaV90b2tlbiJ9.39RXuiS-mggEIWWjNemaWxfTp-GtkwxEt7gFXE4-Df8"}

url = "https://api.edenai.run/v2/text/generation"
payload = {
    "providers": "openai",
    "text": "Write a Docker File for httpd server for centos:7 container.dont copy any configurations or files . Only give the output of the Docker File, nothing else",
    "temperature": 0.2,
    "max_tokens": 250,

}

response = requests.post(url, json=payload, headers=headers)

result = json.loads(response.text)
output = result['openai']['generated_text']
def save_content_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
output_file = "Dockerfile"
save_content_to_file(output_file,output)
