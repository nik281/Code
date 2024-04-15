import xml.dom.minidom as md
s = [{'name':'s1','mk':'100'},{'name':'s2','mk':'90'}]
doc = md.Document()
print(doc)
root = doc.createElement('students')
doc.appendChild(root)
for st in s:
    ch = doc.createElement('std')
    for k in st:
        ele = doc.createElement(k)
        t = doc.createTextNode(st[k])
        ele.appendChild(t)
        ch.appendChild(ele)
    root.appendChild(ch)
with open('a.xml','w') as f:
    f.write(doc.toprettyxml(indent='    '))
with open('a.xml','r') as f:
    print(f.read())