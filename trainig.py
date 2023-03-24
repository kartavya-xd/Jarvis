import requests

def is_username_available(username):
    # Send a GET request to Instagram's search endpoint
    response = requests.get(f'https://www.instagram.com/web/search/topsearch/?query={username}')
    response_json = response.json()

    # Check if the username is available
    if len(response_json['users']) == 0:
        return True
    else:
        return False

# Test the function with some example usernames
usernames = ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yz12', '3456']
for username in usernames:
    if is_username_available(username):
        print(f'{username} is available')
    else:
        print(f'{username} is not available')
