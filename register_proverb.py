import json
import requests

def register_proverbs_from_json(file_path, api_url):
    """
    Register proverbs from a JSON file using the API.

    Args:
    - file_path (str): The path to the JSON file containing the proverbs.
    - api_url (str): The URL of the API endpoint for registering a single proverb.

    Returns:
    - list: A list of dictionaries representing the registered proverbs.
    """
    registered_proverbs = []

    with open(file_path, 'r') as file:
        data = json.load(file)
        proverbs = data.get('proverbs', [])

        for proverb_text in proverbs:
            # Create a dictionary representing the proverb
            proverb_data = {
                'proverb': proverb_text
            }

            # Make a POST request to the API endpoint to register the proverb
            response = requests.post(api_url, json=proverb_data)

            if response.status_code == 200:
                # Proverb successfully registered
                registered_proverbs.append(response.json())
            else:
                # Error registering proverb
                print(f"Error registering proverb '{proverb_text}': {response.text}")

    return registered_proverbs

if __name__ == "__main__":
    # Specify the path to your JSON file and the URL of the API endpoint
    file_path = 'proverbs.json'
    api_url = 'https://api.umuco.tech/api/v1/insert_proverbs'

    # Register proverbs from the JSON file using the API
    registered_proverbs = register_proverbs_from_json(file_path, api_url)

    # Print the registered proverbs
    print(registered_proverbs)

