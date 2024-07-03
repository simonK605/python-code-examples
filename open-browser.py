import webbrowser

# Specify the URL you want to open
url = "https://www.example.com"

# Use the Windows-style path
windows_url = url.replace("/", "\\")

# Open the web browser
webbrowser.open(windows_url)