from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        ip_address = request.remote_addr
        # Do something with the data, e.g. store it in a database
        return f'Thank you for submitting your information, {first_name} {last_name}. Your IP address is {ip_address}.'
    else:
        return '''
        <form method="POST">
            <label>First Name:</label><br>
            <input type="text" name="first_name"><br>
            <label>Last Name:</label><br>
            <input type="text" name="last_name"><br>
            <input type="submit" value="Submit">
        </form>
        '''

if __name__ == '__main__':
    app.run(debug=True)

    
