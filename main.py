from xml.dom import minidom

doc = minidom.parse("main.xml")

# doc.getElementsByTagName returns NodeList
name = doc.getElementsByClassName(".company")
print((name))
#py main.py
