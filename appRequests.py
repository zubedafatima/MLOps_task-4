import requests

# Input data
input_data = {
    "merchant": "fraud_Waelchi-Wolf",
    "category": "kids_pets",
    "amt": 1.24,
    "gender": "M",
    "street": "88794 Mandy Lodge Apt. 874",
    "city": "Howells",
    "state": "NE",
    "zip": "68641",
    "lat": 41.6964,
    "long": -96.9858,
    "city_pop": 1063,
    "job": "Research scientist (maths)",
    "unix_time": 1378909042,
    "merch_lat": 42.551265,
    "merch_long": -96.065037
}




# Send POST request to Flask server
response = requests.post("http://localhost:5000/predict", json=input_data)

# Check if request was successful
if response.status_code == 200:
    try:
        # Attempt to decode JSON response
        prediction = response.json()['prediction']
        if (prediction == 0):
            print("It is a Fraud")
        else:
            print("it is not a Fraud")
    except Exception as e:
        print("Error decoding JSON response:", e)
        print("Response content:", response.content)
else:
    print("Error:", response.status_code, response.reason)
    print("Response content:", response.content)
