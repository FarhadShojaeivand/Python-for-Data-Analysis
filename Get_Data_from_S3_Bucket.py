import requests
import hashlib
import hmac
import base64
from datetime import datetime

def calculate_signature(secret_key, string_to_sign):
    hashed = hmac.new(secret_key.encode('utf-8'), msg=string_to_sign.encode('utf-8'), digestmod=hashlib.sha1)
    return base64.b64encode(hashed.digest()).decode('utf-8')

def get_s3(endpoint_url, access_key, secret_key, bucket_name, object_key):
        date = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')

        string_to_sign = f"GET\n\n\n{date}\n/{bucket_name}/{object_key}"

        signature = calculate_signature(secret_key, string_to_sign)

        headers = {
            'Date': date,
            'Authorization': f"AWS {access_key}:{signature}"
            }

        url = f"{endpoint_url}/{bucket_name}/{object_key}"

        response = requests.get(url, headers=headers)

        print(response.text)


endpoint_url = "endpoint_url" #like "http://192.168.91.80:8080"
access_key = "access_key"
secret_key = "secret_key"
bucket_name = "bucket_name"
object_key = "object_key"

# Call the function
get_s3(endpoint_url, access_key, secret_key, bucket_name, object_key)
