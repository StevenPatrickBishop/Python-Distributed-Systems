import xml.etree.ElementTree as ET
import sys

tree = ET.parse('plant_catalog.xml')
root = tree.getroot()
element = "COMMON"
plantName = "Anemone"
percentChange = -0.2

def updatePlantPrice(element,plantName,percentChange):
    condition = "*/[" + element + " = '" + plantName + "']/PRICE"
    for x in root.findall(condition):
        originalValue = float(x.text)
        changeBy = originalValue * percentChange
        newValue = round(originalValue + changeBy,2)
        x.text = str(newValue)
    tree.write('new.xml')

# updatePlantPrice(element,plantName,percentChange)


print(root[0][1].text)

# for i in range(len(root)):
#     for j in range(len(root[i])):
#         print(root[i][j].tag, ": ", root[i][j].text)
#     print("\n")

# for x in root.findall('PLANT'):
#     price = x.find('PRICE').text
#     print(f"Price: {price}")


# for x in root.iter('PRICE'):
#     a = "$ " + str(x.text)
#     x.text = str(a)

# tree.write('new.xml')




    