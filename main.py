import requests
import re 
import json
import csv
from datetime import datetime

def main():
    response = requests.get("https://portal.rockgympro.com/portal/public/620b59568a6c93407373bda88564f747/occupancy")
    text = re.findall("{\n.*'AAA' :([^;]*),(.*)}", response.text)[0][0]
    thisjson = json.loads(text.replace("'", "\""))

    with open('count.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        data = [datetime.now().strftime("%d/%m/%Y"), datetime.now().strftime("%H:%M:%S"), thisjson["count"], thisjson["capacity"]]
        writer.writerow(data)

    return

if __name__ == "__main__":
    main()