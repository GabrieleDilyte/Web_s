from flask import Flask
from flask import request
from flask import jsonify

import os

app = Flask(__name__)

visits = [
          {'AK':'49612033268', 'Name' : 'Lina', 'Surname' : 'Kudirkaite', 'Date' : 'Kovo 21 d', 'Time': '11.30'},
          {'AK':'49608052145', 'Name' : 'Kristina', 'Surname' : 'Kateraite', 'Date' : 'Kovo 19 d', 'Time' : '10.15'}
          ]

@app.route('/')
def hello():
    return'Patients visits schedules'

@app.route('/visits/schedules', methods=['GET'])
def get_all_info():
   return jsonify({'visits':visits})
@app.route('/visits/schedules/<patAK>', methods=['DELETE'])
def delete_pat(patAK):
    deleted_pat=[pat for pat in visits if (pat['AK'] == patAK)]
    if len(deleted_pat) == 0:
        abort(404)
    visits.remove(deleted_pat[0])
    return jsonify({'Deleted':deleted_pat[0]})
@app.route('/visits/schedules', methods=['POST'])
def new_appointment():
    new_app={
        'AK' : request.json['AK'],
        'Name' : request.json['Name'],
        'Surname' : request.json['Surname'],
        'Date' : request.json['Date'],
        'Time' : request.json['Time']
        }
    visits.append(new_app)
    return jsonify({'Posted':new_app})
@app.route('/visits/schedules/<switchAK>',methods=['PUT'])
def updateVisits(switchAK):
    up = [ upd for upd in visits if (upd['AK'] == switchAK)]
    if 'Date' in request.json:
        up[0]['Date'] = request.json['Date']
    if 'Time' in request.json:
        up[0]['Time'] = request.json['Time']
    return jsonify({'Switched':up[0]})

@app.route('/visits/schedules/<patieninf>', methods=['GET'])
def getPatient(patieninf):
    pat = [ pak for pak in visits if (pak['AK'] == patieninf
            or pak['Name'] == patieninf or pak['Surname'] == patieninf
            or pak ['Date'] == pateinf or pak['Time'] == patieninf)]
    if len(pat) == 0:
        abort(404)
    return jsonify({'patient':pat})

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0")
    

