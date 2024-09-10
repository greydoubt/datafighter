from werkzeug.utils import secure_filename
import requests
from flask import *
import json
import os
from time import sleep
from parsel import Selector
from flask import jsonify
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)
dropzone = Dropzone(app)
app.config['SECRET_KEY'] = 'supersecretkeygoeshere'

# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
app.config['DROPZONE_REDIRECT_VIEW'] = 'results'

# Uploads settings
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/uploads'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB


@app.route('/', methods =['GET', 'POST'])
def basic():
    return render_template('index.html')


@app.route('/image', methods=['GET', 'POST'])
def index():
    
    # set session for image results
    if "file_urls" not in session:
        session['file_urls'] = []
    # list to hold our uploaded image urls
    file_urls = session['file_urls']

    # handle image upload from Dropszone
    if request.method == 'POST':
        file_obj = request.files
        for f in file_obj:
            file = request.files.get(f)
            
            # save the file with to our photos folder
            filename = photos.save(
                file,
                name=file.filename    
            )

            # append image urls
            file_urls.append(photos.url(filename))
            
        session['file_urls'] = file_urls
        return "uploading..."
    # return dropzone template on GET request    
    return render_template('image.html')


@app.route('/results')
def results():
    
    # redirect to home if no images to display
    if "file_urls" not in session or session['file_urls'] == []:
        return redirect(url_for('index'))
        
    # set the file_urls and remove the session variable
    file_urls = session['file_urls']
    session.pop('file_urls', None)
    
    return render_template('results.html', file_urls=file_urls)

@app.route('/humanresult',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
       result = request.form
       resultdic = result.to_dict()    
       with open('person.json', 'w') as json_file:
            json.dump(resultdic, json_file)
     
            return render_template("humanresult.html",result = result)


# @app.route('/play', methods =['GET', 'POST'])
# def resumescore():
   
#    return render_template('cv.html',t= "hello")




if __name__ == '__main__':
    app.run(debug=True)    



