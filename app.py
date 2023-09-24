from flask import Flask, render_template, request
import httpx

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ssid = request.form['ssid']

        try:
            httpx.get(f'http://192.168.4.1/run?cmd=stop attack', verify=False)
            httpx.get(f'http://192.168.4.1/run?cmd=remove ssids', verify=False)
            httpx.get(f'http://192.168.4.1/run?cmd=attack -b', verify=False)
            httpx.get(f'http://192.168.4.1/attack.json', verify=False)
            httpx.get(f'http://192.168.4.1/run?cmd=add ssid "{ssid}" -f -cl 40 -wpa2', verify=False)
            httpx.get(f'http://192.168.4.1/attack.json', verify=False)
            result = "Broadcasting " + ssid
        except:
            print("Failed to broadcast, please check connection with device")
            result = "Broadcasting failed, please check connection with device!!"

    else:
        ssid = ""
        result = ""

    return render_template('index.html', ssid=ssid, result=result)

if __name__ == '__main__':
    app.run(debug=True)
