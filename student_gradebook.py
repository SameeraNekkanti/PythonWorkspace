grade_entries = [
{"name": "Alice", "score": 85},
{"name": "Bob", "score": 90},
{"name": "Alice", "score": 92},
{"name": "Charlie", "score": 78},
{"name": "Bob", "score": 88},
{"name": "Alice", "score": 81}
]
def build_gradebook(grade_entries):
    gradebook={}
    for i in grade_entries:
        name=i["name"]
        score=i["score"]
        if name not in gradebook:
            gradebook[name]=[]
        gradebook[name].append(score)
    return gradebook
print(build_gradebook(grade_entries))
