import httpx

ssid = input("Enter SSID: ")

httpx.get(f'http://192.168.4.1/run?cmd=stop attack', verify=False)
httpx.get(f'http://192.168.4.1/run?cmd=remove ssids', verify=False)
httpx.get(f'http://192.168.4.1/run?cmd=attack -b', verify=False)
httpx.get(f'http://192.168.4.1/attack.json', verify=False)
httpx.get(f'http://192.168.4.1/run?cmd=add ssid "{ssid}" -f -cl 40 -wpa2', verify=False)
httpx.get(f'http://192.168.4.1/attack.json', verify=False)

print("Done!!")





