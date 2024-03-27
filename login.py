from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Base de données des utilisateurs (à titre d'exemple)
users = {
    "malika": {"username": "malika", "password": "123"},
    "gareh": {"username": "gareh", "password": "789"}
}

@app.route('/')
def home():
    print("La route '/' a été appelée avec succès.")
    return render_template('mentore.html')

@app.route('/login', methods=['POST'])
def login():
    print("La route '/login' a été appelée avec succès.")
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username]['password'] == password:
        # Authentification réussie, rediriger vers la page de formulaire
        return redirect(url_for('formulaire'))
    else:
        # Authentification échouée, rediriger vers la page d'échec
        return redirect(url_for('mentore'))

@app.route('/register', methods=['POST'])
def register():
    print("La route '/register' a été appelée avec succès.")
    username = request.form['username']
    password = request.form['password']
    if username not in users:
        # Ajouter l'utilisateur à la base de données (à titre d'exemple)
        users[username] = {'username': username, 'password': password}
        # Rediriger vers la page de formulaire après l'inscription
        return redirect(url_for('formulaire'))
    else:
        # L'utilisateur existe déjà, rediriger vers la page d'échec
        return redirect(url_for('mentore'))

@app.route('/formulaire')
def formulaire():
    print("La route '/formulaire' a été appelée avec succès.")
    return render_template('formulaire.html')

@app.route('/mentore')
def mentore():
    print("La route '/mentore' a été appelée avec succès.")
    return render_template('mentore.html')
@app.route('/form_signup', methods=['POST'])
def form_signup():
    print("La route '/form_signup' a été appelée avec succès.")
    username = request.form['username']
    password = request.form['password']
    if username not in users:
        # Ajouter l'utilisateur à la base de données (à titre d'exemple)
        users[username] = {'username': username, 'password': password}
        # Rediriger vers la page de formulaire après l'inscription
        return redirect(url_for('formulaire'))
    else:
        # L'utilisateur existe déjà, rediriger vers la page d'échec
        return redirect(url_for('mentore'))


if __name__ == '__main__':
    app.run(debug=True)