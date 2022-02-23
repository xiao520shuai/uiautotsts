from flask import Flask, request, redirect, url_for
from flask import render_template
app = Flask(__name__,template_folder=r"D:\project\flask1")
@app.route('/')
def hello():
   return render_template('login.html')
@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))
if __name__ == '__main__':
    app.run(debug=True)