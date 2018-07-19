from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route('/')
def main():
    return 'Hej!! Min flaskapplikation i en Docker container 2.'

if __name__ == '__main__':
	app.run(host='0.0.0.0')

