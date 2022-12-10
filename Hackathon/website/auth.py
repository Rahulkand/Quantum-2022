from flask import Blueprint,render_template,request
auth = Blueprint("auth",__name__)

@auth.route('/system',methods=['GET','POST'])
def system():
    ln=request.form.get("Licence_number")
    return render_template("system.html")
    