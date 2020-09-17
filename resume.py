from flask import Flask, render_template, request
import os

app = Flask(__name__)
target = os.path.join('static')

@app.route('/')

def index():
    return render_template('details.html')

@app.route('/RESUME', methods=['GET', 'POST'])
def RESUME():
    
    full_filename = os.path.join(target, 'image.jpg')
    print(full_filename)
    return render_template('builded_resume.html', name=request.form['name'], role=request.form['role'],obj=request.form['obj'],col=request.form['col'],branch=request.form['branch'],
    year1=request.form['year1'],per1=request.form['per1'],col2=request.form['col2'],stream=request.form['stream'],per2=request.form['per2'],year2=request.form['year2'],
    sch=request.form['sch'],year3=request.form['year3'],per3=request.form['per3'],comp=request.form['comp'],exp=request.form['exp'],cer1=request.form['cer1'],
    dur1=request.form['dur1'],cer2=request.form['cer2'],dur2=request.form['dur2'],prof1=request.form['prof1'],prof2=request.form['prof2'],prof3=request.form['prof3'],
    pers1=request.form['pers1'],pers2=request.form['pers2'],pers3=request.form['pers3'],hob1=request.form['hob1'],hob2=request.form['hob2'],hob3=request.form['hob3'],
    proj_dur1=request.form['proj_dur1'],proj_dur2=request.form['proj_dur2'],proj_name1=request.form['proj_name1'],proj_name2=request.form['proj_name2'],lang1=request.form['lang1'],
    lang2=request.form['lang2'],work_dur1=request.form['work_dur1'],desc_work1=request.form['desc_work1'],exp_dur1=request.form['exp_dur1'],address=request.form['address'],
    gmail=request.form['gmail'],git_link=request.form['git_link'],linked_in=request.form['linked_in'],num=request.form['num'],user_image = full_filename)                                                                          

if __name__ == "__main__":
    app.run(debug=True)