from flask import Flask, request, jsonify
from app.calculator.pricing import calculate_busCard_price

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        price = calculate_busCard_price(
            num_zones=data['num_zones'],
            num_people=data['num_people'],
            customer_type=data.get('customer_type', 'adult')
        )
        return jsonify({"price": price})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
