from flask import Flask, jsonify, render_template, send_from_directory
import json
import utils
import urllib2
from flask import Flask, jsonify

# Logic to get image count from dog api
def get_dog_image_count():
    response = urllib2.urlopen('https://dog.ceo/api/breeds/list')
    html = response.read()

    dog_dict = json.loads(html)
    dog_list = dog_dict.get('message')
    dog_image_count = [['Dog Breed', 'Number of images'], ]

    for dog in dog_list:
        count = 0
        images = urllib2.urlopen('https://dog.ceo/api/breed/'+dog+"/images")
        image_read = images.read()
        for image in image_read:
            count = count+1
        dog_image_count.append([dog,count])
    return(dog_image_count)

# Flask server
app = Flask(__name__, template_folder="./static")

@app.route("/api/dog_info")
def get_dog_info():
    print("getting dog info")
    dog_info = get_dog_image_count()
    return jsonify({
        'dog_info':utils.norm_json(dog_info)
    })

if __name__ == "__main__":
    app.run(debug=True)