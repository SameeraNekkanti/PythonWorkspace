files = [
" script .py",
" notes .txt",
" data .csv",
" main .py",
" image .png",
" list .txt"
]
def group_by_extension(files):
    grouped={}
    for i in files:
        i=i.replace(" ","")
        name,ext=i.split(".")
        if ext not in grouped:

            grouped[ext]=[]
        grouped[ext].append(i)
    return grouped
print(group_by_extension(files))
