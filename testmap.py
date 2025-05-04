from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

YANDEX_API_KEY = "a24491d9-0cde-46d5-aa70-07ed380b2649"

@app.route('/')
def index():
    return render_template('map.html')

@app.route('/route', methods=['POST'])
def build_route():
    data = request.json
    points = data.get('points', [])
    
    if len(points) < 2:
        return jsonify({"error": "Необходимо минимум две точки."}), 400

    # Формирование параметров запроса для маршрута
    waypoints = '~'.join([f"{p['lat']},{p['lon']}" for p in points])
    url = f"https://api.routing.yandex.net/v2/route?apikey={YANDEX_API_KEY}&waypoints={waypoints}&mode=driving"

    # Запрос к API Яндекс.Карт
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({"error": "Не удалось получить маршрут от API Яндекс.Карт."}), 500

    return jsonify(response.json())

if (__name__ == '__main__'):
    app.run(debug=True)