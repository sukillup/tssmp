from flask import Flask,render_template
r1=0
r2=0
r3=0
app=Flask(__name__)
@app.route('/')
def idff1():
    return render_template('sssa.html',message="ベースアイテム")
if __name__=="__main__":
    app.run(debug=True)