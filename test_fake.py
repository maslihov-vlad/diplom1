import requests

# Registration endpoint test
def test_registration():
    url = 'http://localhost:5000/register'  # Replace with your actual endpoint URL
    data = {'login': 'crypto', 'password': 'expert'}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print('Registration successful')
    else:
        print('Registration failed')

# Login endpoint test
def test_login():
    url = 'http://localhost:5000/login'  # Replace with your actual endpoint URL
    data = {'login': 'crypto', 'password': 'expert'}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print('Login successful')
    else:
        print('Login failed')

# App endpoint test
def test_app():
    url = 'http://localhost:5000/app'  # Replace with your actual endpoint URL
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        signals = data.get('signals')
        print('Signals:')
        for signal in signals:
            print(signal)
    else:
        print('App request failed')

# Run the tests
test_registration()
test_login()
test_app()
