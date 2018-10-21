# live_streaming.py

from flask import Flask, render_template, Response
import face_recog

app = Flask(__name__)

@app.route('/')
def index():
#    return render_template('index.html')
    return render_template('test.html')

#@app.route('/test')
#def test():
#    return render_template('test.html')

#def gen(fr):
#    while True:
#        jpg_bytes = fr.get_jpg_bytes()
#        yield (b'--frame\r\n'
#               b'Content-Type: image/jpeg\r\n\r\n' + jpg_bytes + b'\r\n\r\n')

#@app.route('/video_feed/<url>')
#def video_feed(url):
#    return Response(gen(face_recog.FaceRecog(url)),
#                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
