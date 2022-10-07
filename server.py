from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__)

@app.route("/users")
def listUsers():
    users = User.get_all()
    return render_template("users/list.html", users=users)

@app.route("/users/new")
def createUser():
    user = User
    return render_template("users/form.html", action="/users", title="Crear usuario", user=user)

@app.route("/users/edit/<int:user_id>")
def editUser(user_id):
    user = User.get_one(user_id)
    return render_template("users/form.html", action="/users/edit", title="Editar usuario",  user=user)

@app.route("/users", methods = ["POST"])
def processNewUser():
    data = {
        "fname": request.form["first_name"],
        "lname": request.form["last_name"],
        "email": request.form["email"]
    }

    userId = User.save(data)
    return redirect('/users/' + str(userId))

@app.route("/users/<int:user_id>")
def showUser(user_id):
    user = User.get_one(user_id)
    return render_template("users/show.html", user=user)

@app.route("/users/edit", methods=["POST"])
def processUpdateUser():
    userId = request.form["user_id"]
    user = User.get_one(userId)

    user.update({
        "id": user.id,
        "fname": request.form["first_name"],
        "lname": request.form["last_name"],
        "email": request.form["email"],
    })

    return redirect('/users')

@app.route("/users/delete/<int:user_id>")
def deleteUser(user_id):
    User.delete_one(user_id)
    return redirect("/users")


if __name__=="__main__":
    app.run(debug=True)