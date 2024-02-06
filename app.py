from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def hello():
    return 'Hello, Ngrok is working!'

@app.route('/get_shipment', methods=['POST'])
def get_shipment():
    try:
        # Get the order ID from the incoming request
        order_id = request.json['queryResult']['parameters']['number']
        order_id = int(order_id)

        if not order_id:
            return jsonify({
                'fulfillmentText': 'Order ID is required'
            }), 400

        # Make a request to the external API to get shipment date
        api_url = 'https://orderstatusapi-dot-organization-project-311520.uc.r.appspot.com/api/getOrderStatus'
        payload = {'orderId': order_id}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(api_url, json=payload, headers=headers)

        # Check if the request to the external API was successful (status code 200)
        if response.status_code == 200:
            shipment_date = response.json().get('shipmentDate')

            # Convert date from ISO format to human-readable format
            from datetime import datetime
            shipment_date = datetime.fromisoformat(shipment_date[:-1])   # Remove 'Z' from the end
            shipment_date = shipment_date.strftime('%A, %d %b %Y')
            
            # Create a Dialogflow webhook response
            fulfillment_response = {
                'fulfillmentMessages': [
                    {
                        'text': {
                            'text': [
                                f'Your order {order_id} will be shipped on {shipment_date}.'
                            ]
                        }
                    }
                ]
            }

            return jsonify(fulfillment_response)

        # If the request was not successful, handle the error
        return jsonify({
            'fulfillmentText': f'Failed to get shipment date. API response: {response.text}'
        }), response.status_code

    except Exception as e:
        # Handle exceptions appropriately (logging, error response, etc.)
        print(f"Error processing request: {str(e)}")
        return jsonify({
            'fulfillmentText': 'An error occurred while processing the request.'
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
