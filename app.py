from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'xxxx'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('broadcast', namespace='/broadcast')
def test_message(message):
    emit('response', {'username': message['username'], 'coords': message['coords'], 'acc': message['acc']}, broadcast=True)
    print str({'username': message['username'], 'coords': message['coords'], 'acc': message['acc']})
if __name__ == '__main__':
    socketio.run(app, port=5005)
