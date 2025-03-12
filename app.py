from flask import Flask, render_template, request, jsonify
import replicate
import time

app = Flask(__name__)

# 🚀 Force Flask to Reload Templates and Disable Caching
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Hardcoded Replicate API key
REPLICATE_API_TOKEN = "r8_X1gcU2tWEbjYVNo7LVElyYls7bvXVFx2Bw1Ki"

@app.route('/')
def index():
    return render_template('index.html', time=time.time())

@app.route('/generate', methods=['POST'])
def generate_home():
    """Generates an AI dream home based on the description"""
    data = request.get_json()
    
    if not data or 'description' not in data:
        return jsonify({'error': 'Missing description'}), 400  

    prompt = data['description']
    
    try:
        # 🚀 Run Stable Diffusion on Replicate
        output = replicate.run(
            "stability-ai/stable-diffusion:ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4",
            input={
                "width": 768,
                "height": 768,
                "prompt": prompt,
                "scheduler": "K_EULER",
                "num_outputs": 1,
                "guidance_scale": 7.5,
                "num_inference_steps": 50
            }
        )

        # 🚀 Extract the image URL correctly
        if isinstance(output, list) and len(output) > 0:
            image_url = str(output[0])  # Convert FileOutput to string URL
            return jsonify({"generated_image": image_url})
        else:
            return jsonify({"error": "No image generated"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
