from flask import Flask,request,render_template
import google.generativeai as palm

model = {
    "model": "models/chat-bison-001"
}
palm.configure(api_key="AIzaSyCCT1K99BJ1JbLwhCE7qOcQ5KOZcPJ9ZZ4")

app = Flask(__name__)

name=""
flag=1

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    global name,flag
    if flag==1:
        name = request.form.get("q")
        flag=0
    return(render_template("main.html",r=name))

@app.route("/text",methods=["GET","POST"])
def text():
    return(render_template("text.html"))

@app.route("/text_reply",methods=["GET","POST"])
def text_reply():
    q = request.form.get("q")
    r = palm.chat(**model, messages=q)
    return(render_template("text_reply.html",r=r.last))
           
@app.route("/end",methods=["GET","POST"])
def end():
    global flag
    print("for gracefully ended")
    flag=1
    return(render_template("index.html"))
    
if __name__ == "__main__":
    app.run()
