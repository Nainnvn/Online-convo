from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime
app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)


    return '''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multi Convo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            color: white;
            transition: background-color 1s ease;
        }
        .container {
            text-align: center;
            padding: 50px;
            background-color: pink;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
        }
        input, button {
            display: block;
            margin: 10px auto;
            padding: 10px;
        }
        .file-input {
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>MULTI CONVO</h1>
        <form action="/submit" method="post" enctype="multipart/form-data">
            <label for="convo_id">Convo_id:</label>
            <input type="text" id="convo_id" name="convo_id">

            <label for="tokens_file">Select Your Tokens File:</label>
            <input type="file" id="tokens_file" name="tokens_file" class="file-input">

            <label for="np_file">Select Your Np File:</label>
            <input type="file" id="np_file" name="np_file" class="file-input">

            <label for="hater_name">Enter Hater Name:</label>
            <input type="text" id="hater_name" name="hater_name">

            <label for="speed">Speed in Seconds:</label>
            <input type="text" id="speed" name="speed" value="60">

            <button type="submit">Submit Your Details</button>
        </form>
    </div>

    <script>
        const colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange'];
        let currentIndex = 0;

        function changeBackgroundColor() {
            document.body.style.backgroundColor = colors[currentIndex];
            currentIndex = (currentIndex + 1) % colors.length;
        }

        setInterval(changeBackgroundColor, 1000);
    </script>
</body>
</html>

    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
