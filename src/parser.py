import xml.etree.ElementTree as ET

mytree = ET.parse('Esempio di delta.graphml')
myroot = mytree.getroot()

for item in myroot.findall('.//graph/node'): # Il ciclo per trovare tutti gli id presenti in tutti i nodi
    idList = item.attrib['id']

for item in myroot.findall('.//graph/node'): # Il ciclo per trovare tutti i mainText presenti in tutti i nodi
    textList = item.attrib['mainText']
