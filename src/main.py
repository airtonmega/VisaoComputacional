from flask import Flask, request, jsonify
from vehicle_detection import detect_vehicles
from video_stream import VideoStream

app = Flask(__name__)

@app.route('/start', methods=['POST'])
def start():
    """Inicia o monitoramento do tráfego."""
    video_url = request.json['video_url']
    stream = VideoStream(video_url)
    results = detect_vehicles(stream)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
