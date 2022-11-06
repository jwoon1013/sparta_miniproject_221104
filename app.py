from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient

import certifi

#성준 db
junclient = MongoClient('mongodb+srv://sparta:test@cluster0.u8xq40k.mongodb.net/Cluster0?retryWrites=true&w=majority')
jun_db = junclient.dbsparta

#조운 db
jw_client = MongoClient('mongodb+srv://test:sparta@Cluster0.xtye7kw.mongodb.net/?retryWrites=true&w=majority')
jw_db = jw_client.dbsparta

#용연 db
eli_client = MongoClient('mongodb+srv://test:sparta@cluster0.iytbmso.mongodb.net/Cluster0?retryWrites=true&w=majority')
eli_db = eli_client.dbsparta

#성윤 db
syjclient = MongoClient('mongodb+srv://test:sparta@cluster0.lot5yin.mongodb.net/Cluster0?retryWrites=true&w=majority')
syj_db = syjclient.dbsparta

#남훈 db
ca = certifi.where()
nhk_client = MongoClient('mongodb+srv://test:sparta@cluster0.j4reysf.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
nhk_db = nhk_client.miniteam

@app.route('/')  #팀페이지
def home():
    return render_template('index.html')

@app.route('/jun-page')   #성준페이지
def jun_page():
    return render_template('jun-page.html')

@app.route('/jw-page')   #조운페이지
def jw_page():
    return render_template('jw-page.html')

@app.route('/elicho-page')   #용연페이지
def elicho_page():
    return render_template('elicho-page.html')

@app.route('/SYJ')   #성윤페이지
def SYJ():
    return render_template('SYJ.html')

@app.route('/nhk')    #남훈페이지
def nhk_page():
    return render_template('nhk.html')



#post
@app.route("/coosepost", methods=["POST"])
def coose_post():
    user = request.form['user']
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {'name': name_receive,
           'comment': comment_receive}

    if user == 'main' :
        nhk_db.coosemain.insert_one(doc)
    elif user == 'jun' :
        jun_db.coosejun.insert_one(doc)
    elif user == 'jw' :
        jw_db.tpro1.insert_one(doc)
    elif user == 'eli' :
        eli_db.cooseproject.insert_one(doc)
    elif user == 'syj' :
        syj_db.syjcomment.insert_one(doc)
    elif user == 'nhk' :
        nhk_db.nhk.insert_one(doc)

    return jsonify({'msg':'방명록 저장 완료!'})


#get
@app.route("/cooseget", methods=["GET"])
def coose_get():
    user = request.args.get('user')
    search_name = request.args.get('search_name')
    comment_list = list()

    if user == 'main':
        comment_list = list(nhk_db.coosemain.find({}, {'_id': False}))
    elif user == 'jun':
        comment_list = list(jun_db.coosejun.find({}, {'_id': False}))
    elif user == 'jw':
        comment_list = list(jw_db.tpro1.find({}, {'_id': False}))
    elif user == 'eli':
        comment_list = list(eli_db.cooseproject.find({}, {'_id': False}))
    elif user == 'syj':
        comment_list = list(syj_db.syjcomment.find({}, {'_id': False}))
    elif user == 'nhk':
        comment_list = list(nhk_db.nhk.find({}, {'_id': False}))

#검색기능
    if search_name is not None and search_name is not '':
        temp_list = list()
        search_name = search_name.strip()
        for rows in comment_list:
            if search_name == rows['name']:
                temp_list.append(rows)
        comment_list = temp_list


    return jsonify({'comment_list':comment_list})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)