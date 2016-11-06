from flask import *
from Model.dbModel import *

app = Flask(__name__)


@app.route('/')
def index():
    Documents_data = Document.query.order_by(Document.Sequence).all()
    document_dic = {}
    document_list = []
    for document_data in Documents_data:
        document_dic['document'] = []
        document_dic['ID'] = document_data.ID
        document_dic['Title'] = document_data.Title
        document_dic['Content'] = document_data.Content
        # document_dic['Parent'] = document_data.Parent
        document_dic['Sequence'] = document_data.Sequence
        # for item in child_Documents:
        #     if (item.Parent == document_data.ID):
        #         document_dic['document'].append(item)
        document_list.append(document_dic)
        document_dic = {}
    return render_template('index.html', **locals())

@app.route('/preview')
def preview():
    Documents_data = Document.query.order_by(Document.Sequence).all()
    document_dic = {}
    document_list = []
    for document_data in Documents_data:
        document_dic['document'] = []
        document_dic['ID'] = document_data.ID
        document_dic['Title'] = document_data.Title
        document_dic['Content'] = document_data.Content
        document_list.append(document_dic)
        document_dic = {}
    return render_template('preview.html', **locals())


@app.route('/API_update_Sequence', methods=['POST'])
def api_update_Sequence():
    document_data = request.json.get('document_data')
    sequence_count = 0
    for data in document_data:
        target = Document.query.filter_by(ID=data['id']).scalar()
        target.Sequence = sequence_count
        sequence_count = sequence_count + 1
    db.session.commit()

    return json.dumps("ok")


@app.route('/API_new_document', methods=['POST'])
def API_new_document():
    document_title = request.json.get('document_title')
    document_sequence = request.json.get('document_sequence')
    document_content = request.json.get('document_content')
    if document_sequence == "":
        document_sequence = 0
    data_DocumentDatas = Document(
        Title=document_title,
        Content=document_content,
        Parent=0,
        Sequence=document_sequence
    )

    db.session.add(data_DocumentDatas)
    db.session.commit()
    return json.dumps("ok")


@app.route('/API_edit_document', methods=['POST'])
def API_edit_document():
    document_id = request.json.get('document_id')
    document_title = request.json.get('document_title')
    document_sequence = request.json.get('document_sequence')
    document_content = request.json.get('document_content')
    if document_sequence == "":
        document_sequence = 0
    _DocumentDatas = Document.query.filter_by(ID=document_id).scalar()
    _DocumentDatas.Title = document_title
    _DocumentDatas.Sequence = document_sequence
    _DocumentDatas.Content = document_content
    db.session.commit()
    return json.dumps("ok")


@app.route('/API_delete_documentTitle', methods=['POST'])
def API_delete_documentTitle():
    id = request.json.get('id')
    delete_DocumentDatas = Document.query.filter_by(ID=id).scalar()
    db.session.delete(delete_DocumentDatas)
    db.session.commit()
    return json.dumps("ok")

@app.route('/API_update_document_title', methods=['POST'])
def API_change_document_title():
    document_title_id = request.json.get('title_id')
    # document_content = request.json.get('document_content')
    _DocumentDatas = Document.query.filter_by(ID=document_title_id).scalar()
    document_content = _DocumentDatas.Content
    return json.dumps(document_content)


if __name__ == '__main__':
    app.run(debug=True)
