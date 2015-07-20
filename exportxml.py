
from xml.dom import minidom
'''dom = minidom.parse('C:/Users/wangxun/Downloads/testcases.xml')
root = dom.documentElement
print root.nodeName
print root.nodeValue
print root.nodeType
print root.ELEMENT_NODE
bb = root.getElementsByTagName('testcase')
b = bb[0]
print b.nodeName
print b.getAttribute("name")
cc = root.getElementsByTagName('actions')
c = cc[0]
print c.firstChild.data
'''
impl = minidom.getDOMImplementation()
dom = impl.createDocument(None, None, None)#namespaceURI, qualifiedName, doctype
#write to dom

testsuite =  dom.createElement("testsuite")
testcases = dom.createElement("testcases")
testcase = dom.createElement("testcase")
steps = dom.createElement("steps")
step = dom.createElement("step")
step_number = dom.createElement("step_number")
actions = dom.createElement("actions")
expectedresults = dom.createElement("expectedresults")
sexecution_type = dom.createElement("execution_type")

testcases.setAttribute("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
i=0

    
testcase.setAttribute("name", "checkUI")
testsuite.setAttribute("name", "caidan")
testsuite.appendChild(testcase)


summary = dom.createElement("summary")
preconditions = dom.createElement("preconditions")
execution_type = dom.createElement("execution_type")
importance = dom.createElement("importance")

summary_text = dom.createTextNode("summary")
summary.appendChild(summary_text)
preconditions_text = dom.createTextNode("preconditions")
preconditions.appendChild(preconditions_text)
execution_type_text = dom.createTextNode("execution")
execution_type.appendChild(execution_type_text)
importance_text = dom.createTextNode("importance")
importance.appendChild(importance_text)




step_number_text = dom.createTextNode("1")
actions_text = dom.createTextNode("step")
expectedresults_text = dom.createTextNode("step")
sexecution_type_text = dom.createTextNode("1")
step_number.appendChild(step_number_text)
actions.appendChild(actions_text)
expectedresults.appendChild(expectedresults_text)
sexecution_type.appendChild(sexecution_type_text)


step.appendChild(step_number)
step.appendChild(actions)
step.appendChild(expectedresults)
step.appendChild(sexecution_type)


testcase.appendChild(summary)
testcase.appendChild(preconditions)
testcase.appendChild(execution_type)
testcase.appendChild(importance)
testcase.appendChild(steps)
steps.appendChild(step)



dom.appendChild( testsuite )

f=file('C:/Users/wangxun/Downloads/skills.xml','w')
dom.writexml(f,'',' ','\n','utf-8')
f.close()