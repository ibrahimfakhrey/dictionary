from flask import Flask, render_template, request, redirect

app=Flask(__name__)


users={
    "ibrahim":"admin",
    "basmallah":"user",
    "torkey":"teacher"
}
oxford={

    "Hi":"a word we say it in the early ",
    "car":"somthing to move us from a place to another "
}
@app.route("/")
def start():
    return render_template("index.html")

@ app .route("/login",methods=["GET","POST"])
def login():
    if request.method =="POST":
        name=request.form.get("name")
        if name in users:
            role=users[name]
            if role =="user":
                return render_template("users.html")
            elif role =="admin":
                return render_template("admin.html",data=users)
            elif role =="teacher":
                return render_template("teacher.html")
        else:
            return "you are not register بره يا كلب "
    return  render_template("login.html")


@ app .route("/register",methods=["GET","POST"])
def register():
    if request.method =="POST":
        name=request.form.get("name")
        if name in users :
            return redirect("/login")
        users[name]="user"
        return redirect("/login")


    return  render_template("register.html")

@app.route("/user",methods=["GET","POST"])
def user():
    if request.method =="POST":
        word=request.form.get("word")
        if word in oxford:
            return oxford[word]
        else:
            return "مش عندي يا عسل "


@app.route("/add_word",methods=["GET","POST"])
def add_word():
    if request.method=="POST":
        word=request.form.get("word")
        defin=request.form.get("def")
        if word in oxford:
            return f"i have this word and it is {oxford[word]}"

        oxford[word]=defin
        return "added sucessfuly"
    return render_template("teacher.html")


@app.route("/change_role/<name>/<role>",methods=["GET","POST"])
def change_role(name,role):
    if request.method=="POST":
        new_role=request.form.get("new_role")
        users[name]=new_role

        return "changed successfully"


    return render_template("change.html",name=name,role=role)

if __name__=="__main__":
    app.run(debug=True)