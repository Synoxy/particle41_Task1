from datetime import datetime
import socket
from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def SimpletimeService(): 
    current_timestamp = datetime.now()
    formatted_timestamp = current_timestamp.strftime("%Y-%m-%d %H:%M:%S")
    host_ip = socket.gethostbyname(socket.gethostname())
    return jsonify({
        'timestamp': formatted_timestamp,
        'ip': host_ip
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)