# This is the model

from config import app, db

class Course(db.Document):
    code = db.StringField(required=True, unique=True)
    name = db.StringField(required=True)
    description = db.StringField(required=True)
    syllabus = db.URLField()
    prereq = db.ListField()
    coreq = db.ListField()
    exclusion = db.ListField()
    keyword = db.StringField(required=True)
    graph = db.StringField(required=True)

    meta = {'indexes': [
        '$keyword'
    ]}

    @classmethod
    def get(cls, code_):
        return cls.objects(code=code_).get()
    
    @classmethod
    def get_requisite_graph(cls, code_):
        return cls.objects(code=code_).get().graph
