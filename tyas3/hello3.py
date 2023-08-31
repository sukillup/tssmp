from flask import Flask,render_template,request,redirect

r1=0
r2=0
r3=0

app=Flask(__name__)


@app.route('/')
def he():
    return render_template('ccca.html',message="Tシャツ③の見積")
@app.route('/sssa',methods=["POST"])
def sssa():
    if request.method=="POST":
        return redirect('./sa')
@app.route('/sa')
def sa():
    return render_template('sssa.html',message="Tシャツ③項目")
@app.route('/ddda',methods=["POST"])
def ddda():
    neme1=request.form.get("サイズ")
    neme2=request.form.get("カラー")
    neme3=request.form.get("デザイン")
    neme4=request.form.get("デザイン位置")
    neme5=request.form.get("q")
    print(neme1)
    print(neme2)
    print(neme3)
    print(neme4)
    print(neme5)
    global r1
    global r2
    if neme1=="S" and neme2 and neme3=="自前" and neme4=="ワンポイント":
     r1=1700
     r2=1000
     total=round(((r1*int(neme5)+r2)/int(neme5))*int(neme5))
     return render_template("ddda.html",message="Tシャツ③{0}サイズ{1}{2}{3}{4}枚".format(neme1,neme2,neme3,neme4,neme5),tist="合計で",tist2="{}円です".format(total))
    elif neme1=="S" and neme2 and neme3=="依頼" and neme4=="ワンポイント":
     r1=1700
     r2=5000
     total=round(((r1*int(neme5)+r2)/int(neme5))*int(neme5))
     return render_template("ddda.html",message="Tシャツ③{0}サイズ{1}{2}{3}{4}枚".format(neme1,neme2,neme3,neme4,neme5),tist="合計で",tist2="{}円です".format(total))
    elif neme1=="S" and neme2 and neme3=="自前" and neme4=="全体":
     r1=2000
     r2=1000
     total=round(((r1*int(neme5)+r2)/int(neme5))*int(neme5))
     return render_template("ddda.html",message="Tシャツ③{0}サイズ{1}{2}{3}{4}枚".format(neme1,neme2,neme3,neme4,neme5),tist="合計で",tist2="{}円です".format(total))
    elif neme1=="S" and neme2 and neme3=="依頼" and neme4=="全体":
     r1=2000
     r2=10000
     total=round(((r1*int(neme5)+r2)/int(neme5))*int(neme5))
     return render_template("ddda.html",message="Tシャツ③{0}サイズ{1}{2}{3}{4}枚".format(neme1,neme2,neme3,neme4,neme5),tist="合計で",tist2="{}円です".format(total))
    elif neme1=="S" and neme2 and neme3=="自前" and neme4=="２か所以上":
     r1=2200
     r2=2000
     total=round(((r1*int(neme5)+r2)/int(neme5))*int(neme5))
     return render_template("ddda.html",message="Tシャツ③{0}サイズ{1}{2}{3}{4}枚".format(neme1,neme2,neme3,neme4,neme5),tist="合計で",tist2="{}円です".format(total))
    elif neme1=="S" and neme2 and neme3=="依頼" and neme4=="２か所以上":
     r1=2200
     r2=15000
     total=round(((r1*int(neme5)+r2)/int(neme5))*int(neme5))
     return render_template("ddda.html",message="Tシャツ③{0}サイズ{1}{2}{3}{4}枚".format(neme1,neme2,neme3,neme4,neme5),tist="合計で",tist2="{}円です".format(total))      
    elif neme1=="M" and neme2 and neme3=="自前" and neme4=="ワンポイント":
     r1=1700
     r2=1000
     total=round(((r1*int(neme5)+r2)/int(neme5))*int(neme5))
     return render_template("ddda.html",message="Tシャツ③{0}サイズ{1}{2}{3}{4}枚".format(neme1,neme2,neme3,neme4,neme5),tist="合計で",tist2="{}円です".format(total))
    elif neme1=="M" and neme2 and neme3=="依頼" and neme4=="ワンポイント":
     r1=1700
     r2=5000
     total=round(((r1*int(neme5)+r2)/int(neme5))*int(neme5))
     return render_template("ddda.html",message="Tシャツ③{0}サイズ{1}{2}{3}{4}枚".format(neme1,neme2,neme3,neme4,neme5),tist="合計で",tist2="{}円です".format(total))
    elif neme1=="M" and neme2 and neme3=="自前" and neme4=="全体":
     r1=2000
     r2=1000
     total=round(((r1*int(neme5)+r2)/int(neme5))*int(neme5))
     return render_template("ddda.html",message="Tシャツ③{0}サイズ{1}{2}{3}{4}枚".format(neme1,neme2,neme3,neme4,neme5),tist="合計で",tist2="{}円です".format(total))
    elif neme1=="M" and neme2 and neme3=="依頼" and neme4=="全体":
     r1=2000
     r2=10000
     total=round(((r1*int(neme5)+r2)/int(neme5))*int(neme5))
     return render_template("ddda.html",message="Tシャツ③{0}サイズ{1}{2}{3}{4}枚".format(neme1,neme2,neme3,neme4,neme5),tist="合計で",tist2="{}円です".format(total))
    elif neme1=="M" and neme2 and neme3=="自前" and neme4=="２か所以上":
     r1=2200
     r2=2000
     total=round(((r1*int(neme5)+r2)/int(neme5))*int(neme5))
     return render_template("ddda.html",message="Tシャツ③{0}サイズ{1}{2}{3}{4}枚".format(neme1,neme2,neme3,neme4,neme5),tist="合計で",tist2="{}円です".format(total))
    elif neme1=="M" and neme2 and neme3=="依頼" and neme4=="２か所以上":
     r1=2200
     r2=15000
     total=round(((r1*int(neme5)+r2)/int(neme5))*int(neme5))
     return render_template("ddda.html",message="Tシャツ③{0}サイズ{1}{2}{3}{4}枚".format(neme1,neme2,neme3,neme4,neme5),tist="合計で",tist2="{}円です".format(total))
    elif neme1=="L" and neme2 and neme3=="自前" and neme4=="ワンポイント":
     r1=1700
     r2=1000
     total=round(((r1*int(neme5)+r2)/int(neme5))*int(neme5))
     return render_template("ddda.html",message="Tシャツ③{0}サイズ{1}{2}{3}{4}枚".format(neme1,neme2,neme3,neme4,neme5),tist="合計で",tist2="{}円です".format(total))
    elif neme1=="L" and neme2 and neme3=="依頼" and neme4=="ワンポイント":
     r1=1700
     r2=5000
     total=round(((r1*int(neme5)+r2)/int(neme5))*int(neme5))
     return render_template("ddda.html",message="Tシャツ③{0}サイズ{1}{2}{3}{4}枚".format(neme1,neme2,neme3,neme4,neme5),tist="合計で",tist2="{}円です".format(total))
    elif neme1=="L" and neme2 and neme3=="自前" and neme4=="全体":
     r1=2000
     r2=1000
     total=round(((r1*int(neme5)+r2)/int(neme5))*int(neme5))
     return render_template("ddda.html",message="Tシャツ③{0}サイズ{1}{2}{3}{4}枚".format(neme1,neme2,neme3,neme4,neme5),tist="合計で",tist2="{}円です".format(total))
    elif neme1=="L" and neme2 and neme3=="依頼" and neme4=="全体":
     r1=2000
     r2=10000
     total=round(((r1*int(neme5)+r2)/int(neme5))*int(neme5))
     return render_template("ddda.html",message="Tシャツ③{0}サイズ{1}{2}{3}{4}枚".format(neme1,neme2,neme3,neme4,neme5),tist="合計で",tist2="{}円です".format(total))
    elif neme1=="L" and neme2 and neme3=="自前" and neme4=="２か所以上":
     r1=2200
     r2=2000
     total=round(((r1*int(neme5)+r2)/int(neme5))*int(neme5))
     return render_template("ddda.html",message="Tシャツ③{0}サイズ{1}{2}{3}{4}枚".format(neme1,neme2,neme3,neme4,neme5),tist="合計で",tist2="{}円です".format(total))
    elif neme1=="L" and neme2 and neme3=="依頼" and neme4=="２か所以上":
     r1=2200
     r2=15000
     total=round(((r1*int(neme5)+r2)/int(neme5))*int(neme5))
     return render_template("ddda.html",message="Tシャツ③{0}サイズ{1}{2}{3}{4}枚".format(neme1,neme2,neme3,neme4,neme5),tist="合計で",tist2="{}円です".format(total))
    elif neme1=="XL" and neme2 and neme3=="自前" and neme4=="ワンポイント":
     r1=1700
     r2=1000
     total=round(((r1*int(neme5)+r2)/int(neme5))*int(neme5))
     return render_template("ddda.html",message="Tシャツ③{0}サイズ{1}{2}{3}{4}枚".format(neme1,neme2,neme3,neme4,neme5),tist="合計で",tist2="{}円です".format(total))
    elif neme1=="XL" and neme2 and neme3=="依頼" and neme4=="ワンポイント":
     r1=1700
     r2=5000
     total=round(((r1*int(neme5)+r2)/int(neme5))*int(neme5))
     return render_template("ddda.html",message="Tシャツ③{0}サイズ{1}{2}{3}{4}枚".format(neme1,neme2,neme3,neme4,neme5),tist="合計で",tist2="{}円です".format(total))
    elif neme1=="XL" and neme2 and neme3=="自前" and neme4=="全体":
     r1=2000
     r2=1000
     total=round(((r1*int(neme5)+r2)/int(neme5))*int(neme5))
     return render_template("ddda.html",message="Tシャツ③{0}サイズ{1}{2}{3}{4}枚".format(neme1,neme2,neme3,neme4,neme5),tist="合計で",tist2="{}円です".format(total))
    elif neme1=="XL" and neme2 and neme3=="依頼" and neme4=="全体":
     r1=2000
     r2=10000
     total=round(((r1*int(neme5)+r2)/int(neme5))*int(neme5))
     return render_template("ddda.html",message="Tシャツ③{0}サイズ{1}{2}{3}{4}枚".format(neme1,neme2,neme3,neme4,neme5),tist="合計で",tist2="{}円です".format(total))
    elif neme1=="XL" and neme2 and neme3=="自前" and neme4=="２か所以上":
     r1=2200
     r2=2000
     total=round(((r1*int(neme5)+r2)/int(neme5))*int(neme5))
     return render_template("ddda.html",message="Tシャツ③{0}サイズ{1}{2}{3}{4}枚".format(neme1,neme2,neme3,neme4,neme5),tist="合計で",tist2="{}円です".format(total))
    elif neme1=="XL" and neme2 and neme3=="依頼" and neme4=="２か所以上":
     r1=2200
     r2=15000
     total=round(((r1*int(neme5)+r2)/int(neme5))*int(neme5))
     return render_template("ddda.html",message="Tシャツ③{0}サイズ{1}{2}{3}{4}枚".format(neme1,neme2,neme3,neme4,neme5),tist="合計で",tist2="{}円です".format(total))
    else:
     return render_template('sssa.html',message="サイズ選んでね")
  
if __name__=="__main__":
    app.run(debug=True)