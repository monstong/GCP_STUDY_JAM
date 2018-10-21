# live_streaming.py

from flask import request, Flask, render_template, Response
import face_recog
import youtube_dl

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods=['GET','POST'])
def result():
    youTubeURL = ''
    if request.method == 'POST':
       youTubeURL = request.form['murl'];

    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

    with ydl:
       result = ydl.extract_info( youTubeURL, download=True)

    if 'entries' in result:
       # Can be a playlist or a list of videos
       video = result['entries'][0]
    else:
       # Just a video
       video = result

    return render_template('result.html',mmurl=video['display_id'] + video['ext'])


def gen(fr):
    while True:
        jpg_bytes = fr.get_jpg_bytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpg_bytes + b'\r\n\r\n')

@app.route('/video_feed/<url>')
def video_feed(url):
    return Response(gen(face_recog.FaceRecog(url)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

