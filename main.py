from flask import Flask,jsonify,request

app=Flask(__name__)
contact_list = [
    {
        'id': 0,
        'name': 'The Matrix',
        'contact': '0', 
        'done': False
    },
    {
        'id': 1,
        'name': 'Friends at High Places',
        'contact': '999999999999999999', 
        'done': False
    },
    {
        'id': 2,
        'name': 'jablsdfb',
        'contact': '8192758923',
        'done': False
    }
]

@app.route('/')
def hello_world () :
    return 'Mahtab says hello to the world'

@app.route('/add-data',methods=['POST'])
def add_task () :
    if not request.json :
        return jsonify({
            'status':'error',
            'message':'please provide data'
        },400)
    task = {
        'id': contact_list[-1]['id'] + 1,
        'name': request.json['name'],
        'contact': request.json.get('contact', ""),
        'done': False
    }
    contact_list.append(task)
    return jsonify({
        'status':'success',
        'message':'task added successfully'
    })

@app.route('/get-data')
def get_task () :
    return jsonify({
        'data':contact_list
    })

if (__name__=='__main__') :
    app.run(debug=True)

