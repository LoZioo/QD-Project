import xml.etree.ElementTree as ET

mytree = ET.parse('Esempio di delta.graphml')
myroot = mytree.getroot()

for i in myroot:
    posX = myroot.find('./graph').find('./node').attrib['positionX']
    posY = myroot.find('./graph').find('./node').attrib['positionY']
