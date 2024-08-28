import requests
import os

url = "https://example.com/some_file.zip"
download_directory = "/path/to/different_directory"
file_name = "downloaded_file.zip"

response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Create the full path for the file in the new directory
    file_path = os.path.join(download_directory, file_name)

    # Save the file to the new directory
    with open(file_path, 'wb') as file:
        file.write(response.content)

    print(f"File saved to: {file_path}")
else:
    print(f"Failed to download the file. Status code: {response.status_code}")