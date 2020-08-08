from flask import *
from flask_socketio import *

# Init the server
app = Flask(__name__)
app.config['SECRET_KEY'] = 'some super secret key!'
socketio = SocketIO(app, logger=True)

# Send HTML!
@app.route('/')
def root():    
    return "Hello world!"

# Returns a random number
@app.route('/random')
def random():  
    from random import randint  
    html = str(randint(1, 100))
    return html

# Prints the user id
@app.route('/user/<id>')
def user_id(id):
    return str(id)

# Display the HTML Page & pass in a username parameter
@app.route('/html/<username>')
def html(username):
    return render_template('index.html', username=username)

# Receive a message from the front end HTML
@socketio.on('send_message')   
def message_recieved(data):
    client_cmd = data['text']
    print(client_cmd)
    if client_cmd == "/login":
        emit('message_from_server', {'text': "Executing selenium Module with python" })
    else:
        emit('message_from_server', {'text': "type /help to know More !" })

# Actually Start the App
if __name__ == '__main__':
    """ Run the app. """    
    socketio.run(app, host="0.0.0.0", port=8000, debug=True)
