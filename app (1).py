from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

def htop():
    # Get username (fallback to 'unknown' if not found)
    username = os.getenv('USER', 'unknown')
    
    # Get server time in IST
    tz = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

    # Get top command output (or replace with 'whoami' to test subprocess)
    try:
        top_output = subprocess.getoutput('ps aux')  # Or 'whoami' for testing
    except Exception as e:
        top_output = f"Error fetching system info: {str(e)}"

    # Prepare HTML result
    result = f"""
    <h1>Name: Vividh Salankimatt</h1>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {server_time}</h2>
    <pre>Top Output:\n{top_output}</pre>
    """
    return result

@app.route('/')
def home():
    return htop()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Enable debug mode for detailed errors
