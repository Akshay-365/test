from flask import Flask, render_template, request, redirect, url_for
import threading
import gradio as gr

app = Flask(__name__)

# Global variable to store the RTMP key
rtmp_key = ''
rtmp_key_lock = threading.Lock()

# Define the streaming function with RTMP key as a parameter
def stream_to_youtube(input_url):
    global rtmp_key
    with rtmp_key_lock:
        current_rtmp_key = rtmp_key

    # Rest of the streaming code remains the same

# Function to update the RTMP key from the settings tab
@app.route('/update_rtmp_key', methods=['POST'])
def update_rtmp_key():
    global rtmp_key
    with rtmp_key_lock:
        rtmp_key = request.form['rtmp_key']
    return redirect(url_for('settings'))

# Define the Gradio interface
iface = gr.Interface(
    fn=stream_to_youtube,
    inputs=gr.inputs.Textbox(label="Enter the input URL"),
    outputs=gr.outputs.Textbox(label="Status"),
    live=True,
    title="YouTube Streaming App",
    description="Enter the input URL to start streaming to YouTube.",
)

@app.route('/')
def index():
    return iface.launch(share=True)

@app.route('/settings')
def settings():
    return render_template('settings.html', rtmp_key=rtmp_key)

if __name__ == '__main__':
    app.run(debug=True)
