import xml.etree.ElementTree as ET
# xml.etree.ElementTree module implements an API for parsing and creating XML data

mytree = ET.parse('Esempio di delta.graphml')
myroot = mytree.getroot()

nodes = [] 

for item in myroot.findall('.//graph/node'):
    # Dictionaries
    node = {
        'posX' : item.attrib['positionX'],
        'posY' : item.attrib['positionY'],
        'node_id' : item.attrib['id'],
        'label' : item.attrib['mainText']
    }
    
    nodes.append(node)
    # So I have an array of dictionaries
