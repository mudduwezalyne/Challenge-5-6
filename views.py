from flask import Flask, jsonify, request
from entry import Entry

app = Flask(__name__)

ENTRYCLASS = Entry()

@app.route('/api/v1/entries', methods=['GET'])
def get_entries():
    entries = ENTRYCLASS.all_entries()
    return jsonify({'entries': entries})

@app.route('/api/v1/entries', methods=['POST'])
def create_entries():
    details = request.get_json()
    entries = ENTRYCLASS.create_entry(details)
    return jsonify({'entries': entries})

@app.route('/api/v1/entry')
def world():
    return 'Hey world'

@app.route('/api/v1/entries/<int:id>', methods=['GET'])
def get_single_entry(id):
    single_entry = ENTRYCLASS.single_entry(id)
    return jsonify({'entry': single_entry})

if __name__ == "__main__":
app.run(host='localhost', port=5001, debug=True)