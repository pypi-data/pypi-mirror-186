import json
import requests




def whoisxmlapi(ip, apiKey, file_location):
  whoisxmlapi = [
      f"https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey={apiKey}&ipAddress={ip}",
      f"https://ip-netblocks.whoisxmlapi.com/api/v2?apiKey={apiKey}&ip={ip}",
      f"https://dns-history.whoisxmlapi.com/api/v1?apiKey={apiKey}&ip={ip}"
  ]
  results = []
  for api in whoisxmlapi:
    r = requests.get(api)
    k = r.json()
    results.append(k)
  print(results)
  save(file_location, json.dumps(results, indent=2))
  return results


def save(file, data):
    try:
        f = open(file, "a")
        f.write(data)
        return file
    except FileNotFoundError:
        raise Exception("File Not Found")


