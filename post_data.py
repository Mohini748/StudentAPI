import requests

url = "http://127.0.0.1:5000/students"

student = {
    'Id': 3,
    'Name': 'Manish',
    'Course': 'C++'
}

response = requests.post(url, json=student)

print("Status Code:", response.status_code)
print("Response:", response.text)
