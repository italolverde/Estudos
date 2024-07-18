from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def home():
    if 'color' in request.cookies:
        cor = request.cookies['color']
    return render_template('index.html', cor='white')

@app.route('/cores')
def color():
    cor = request.args.get('color')
    
    # verificar se tem cookie
    if 'color' in request.cookies:
        if cor != request.cookies['color']:
            # definir novo cookie
            template = render_template('cor.html', cor = request.cookies['color'])
            response = make_response(template)
            response.delete_cookie('color')
            response.set_cookie('color', value = cor)
            return response
        else:
            return render_template('cor.html', cor = request.cookies['color'])
    else:
        template = render_template('cor.html', cor = request.cookies['color'])
        response = make_response(template)
        response.delete_cookie('color')
        response.set_cookie('color', cor)
        return response

#return render_template('cor.html', request.cookie[])

