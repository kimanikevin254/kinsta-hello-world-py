import psutil
import requests
import json

def check_disk_space():
    disk = psutil.disk_usage('/var/lib/data')
    return {
        "Used": disk.percent,
        "Free": disk.free,
        "Total": disk.total
    }

if __name__ == "__main__":
    disk_info = check_disk_space()
    # print(disk_info)
    endpoint = "https://hooks.slack.com/services/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"
    json_data = json.dumps(disk_info)
    headers = {
        "Content-type": "application/json"
    }

    resp = requests.post(endpoint, data=json_data, headers=headers)