import pandas as pd

class Course():
    def __init__(self, code="", name=""):
        self.code = code
        self.name = name
        self.description = "This is the course description."
        self.syllabus = "Course syllabus here."
        self.prereq = []
        self.coreq = []
        self.exclusion = []


df = pd.read_csv("resources/courses.csv")
def search_course_by_code(s):
    # return all the courses whose course code contains the str s
    course_ids = df[df['Code'].str.contains(s.upper())].index.tolist()
    res = []
    for id in course_ids:
        d = df.iloc[id].to_dict()
        res.append(Course(code=d['Code'], name=d['Name']))
    return res
