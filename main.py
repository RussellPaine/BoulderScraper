import requests
import re 
import json 

def main():
    response = requests.get("https://portal.rockgympro.com/portal/public/620b59568a6c93407373bda88564f747/occupancy")
    text = re.findall("{\n.*'AAA' :([^;]*),(.*)}", response.text)[0][0]
    thisjson = json.loads(text.replace("'", "\""))

    print(thisjson["count"])
    return

if __name__ == "__main__":
    main()