# xml
#  <menu id="file" value="File">
#    <popup>
#      <menuitem value="New" onclick="CreateNewDoc()" />
#      <menuitem value="Open" onclick="OpenDoc()" />
#      <menuitem value="Close" onclick="CloseDoc()" />
#    </popup>
#  </menu>

from xml.dom import minidom

root = minidom.Document()
xml = root.createElement('root')
root.appendChild(xml)

product_child = root.createElement('product')
product_child.setAttribute('name', 'Geek')
xml.appendChild(product_child)

xml_str = root.toprettyxml(indent="\t")
print(xml_str)
# <?xml version="1.0" ?>
# <root>
# 	<product name="Geek"/>
# </root>

with open('gfg.xml', 'w') as f:
    f.write(xml_str)
