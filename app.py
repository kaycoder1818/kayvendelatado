from flask import Flask, send_from_directory, request, abort
import os


app = Flask(__name__)

# Serve index.htm at the root path
@app.route('/')
def serve_index():
    return send_from_directory(os.getcwd(), 'index.htm')

# Serve static files from the _next directory
@app.route('/_next/static/<path:filename>')
def serve_next_static(filename):
    # Define the path to the _next folder in the static directory
    static_dir = os.path.join(os.getcwd(), 'static', '_next', 'static')
    
    # Serve the requested file from the _next/static directory
    return send_from_directory(static_dir, filename)


@app.route('/_next/profile.png')
def serve_profile_image():
    image_dir = os.path.join(os.getcwd(), 'static', '_next')
    return send_from_directory(image_dir, 'profile.png')
    
if __name__ == '__main__':
    app.run(debug=True)
