from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'xxxx'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('broadcast', namespace='/broadcast')
def test_message(message):
    emit('response', {'username': message['username'],'data': message['data']}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)