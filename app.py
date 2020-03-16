from flask import Flask, jsonify, request, render_template
from attendance2.RECO import pred_images
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('face_recognition.html')
@app.route("/predict", methods=['POST'])
def predict():
    #l = demo()
    if request.method == 'POST':
        file1 = request.files['file1']
        file1.save('a.jpg')
        value = request.form['fname']
        #img_bytes1 = file.read()
        file2 = request.files['file2']
        file2.save('b.jpg')
        #img_bytes2 = file.read()
        result = pred_images('a.jpg','b.jpg', float(value))
    # result = pred_images('ex1.png','ex2.JPG')
    return render_template('results.html', prediction_text='Face Recognition Done: {}'.format(result))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)`
