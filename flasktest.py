from flask import Flask, render_template, request

app = Flask(__name__)

post=[
    {
        'Author': 'Ryan Wu',
        'Date': 'July 25th',
        'Title' : 'First Post',
        'Post' : 'Fill content'
    },
    {
        'Author': 'Wu',
        'Date': 'July ',
        'Title' : 'second Post',
        'Post' : ' content'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', post = post)

@app.route('/about')
def about():
    return render_template('about.html')

#app.config [‘UPLOAD_FOLDER’]='storage'


@app.route('/upload/',methods = ['GET','POST'])
def upload():
    if request.method =='POST' and 'file' in request.files:
             filename = files.save(request.files['file'])
             return filename
    return render_template('file_upload.html')

if __name__ == "__main__":
    app.run(debug=True)