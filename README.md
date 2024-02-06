# Order Status Dialogflow Bot and REST API

## Overview
This project involves creating a conversational Dialogflow bot to check order status and a REST API written in Flask to fetch shipment details. The bot interacts with the API to provide users with shipment information based on the order ID.

## Objectives

### Dialogflow Bot Setup:

Setup a Dialogflow ES bot using Dialogflow Console.
Build the conversational flow as depicted in the sequence diagram Fig. 1 provided.


### REST API Development:

Create a Flask REST API to receive webhook requests from the Dialogflow bot.
Process the WebhookRequest to extract the user-provided order ID.
Make a POST request to the provided API endpoint to fetch shipment date.
Return the WebhookResponse with the appropriate details as per the sequence diagram.


## Sequence Diagram



## Getting Started

### Prerequisites

Dialogflow ES account: Dialogflow Console.
Python and Flask installed for the API development.


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/saadsaleem10/OrderStatusBot-DialogFlow-REST-API.git
   cd OrderStatusBot-DialogFlow-REST-API
   ```

2. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```

3. Run the Flask API
   ```sh
    python app.py
    ```
    The API should be accessible at http://localhost:5000.


4. Expose localhost using ngrok for testing
   ```sh
   ngrok http 5000
   ```
   Copy the ngrok URL to set up Dialogflow webhook.



## Dialogflow Configuration

1. Set up Dialogflow intent with webhook fulfillment using the ngrok URL.

2. Test the bot in the Dialogflow console or any supported platform.


## Demo Video

[![Demo Video](https://img.youtube.com/vi/VIDEO-ID/0.jpg)](https://www.youtube.com/watch?v=VIDEO-ID)


## Optional Tasks

1. Convert shipment date to a human-readable format.

2. Deploy the Flask API to a cloud platform like AWS and Azure.


## API Details

### API URL: https://orderstatusapi-dot-organization-project-311520.uc.r.appspot.com/api/getOrderStatus

### Method: POST

### Request Body:
```json
{
    "orderid": "12345"
}
```

### Response bODY:
```json
{
    "shipmentDate": "2021-08-01T00:00:00Z",
}