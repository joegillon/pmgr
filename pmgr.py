from flask import Flask, render_template
from models.project import Project

app = Flask(__name__)

excel_file = 'c:/bench/pmgr/data/projects.xls'

@app.route('/')
def homepage():
    return render_template(
        'index.html',
        title='Prj Mgr',
        projects = Project.get(excel_file)
    )

@app.route('/tst')
def tst():
    return render_template('test.html')

if __name__ == '__main__':
    app.run()
