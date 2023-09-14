import psutil

def check_disk_space():
    disk = psutil.disk_usage('/var/lib/data')
    return disk.percent

if __name__ == "__main__":
    disk_percent = check_disk_space()
    print(f'Used disk space: {disk_percent}%')