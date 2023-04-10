from website import create_app
from flask import render_template

app = create_app()

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)