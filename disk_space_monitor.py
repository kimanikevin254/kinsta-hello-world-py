import psutil
import requests
import json
import os

def check_disk_space():
    disk = psutil.disk_usage('/var/lib/data')
    return {
        "Used": disk.used,
        "Free": disk.free,
        "Total": disk.total
    }

if __name__ == "__main__":
    disk_info = check_disk_space()
    
    endpoint = os.environ.get('SLACK_WEBHOOK_URI')
    
    # Create a Slack message attachment
    attachment = {
        "text": "Disk Space Usage",
        "fields": [
            {
                "title": "Used",
                "value": str(disk_info['Used']),
                "short": True
            },
            {
                "title": "Free",
                "value": str(disk_info['Free']),
                "short": True
            },
            {
                "title": "Total",
                "value": str(disk_info['Total']),
                "short": True
            }
        ]
    }
    
    # Create the main message payload
    payload = {
        "attachments": [attachment]
    }

    # Convert the payload to JSON format
    json_data = json.dumps(payload)

    headers = {
        "Content-type": "application/json"
    }

    resp = requests.post(endpoint, data=json_data, headers=headers)

    print(resp)