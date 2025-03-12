orange modern house with glass walls, 3 stories and sports car  in the garage. 

convert image into url:

   if isinstance(output, list) and len(output) > 0:
            image_url = str(output[0])  # Convert FileOutput to string URL
            return jsonify({"generated_image": image_url})
        else:
            return jsonify({"error": "No image generated"}), 500



            This app is meant to provide inspiration for exterior designs of luxury homes.
             This app can handle features such as glass windows, specific color of houses, and other niche requests. 
             This app will be able to help the Architects, Exterior Designers, and other general people looking to purchase a luxury home. 
            I am able to generate images using Stable Diffusions language model, connecting with it via ReplicateAPI.