import xml.etree.ElementTree as ET


# set IVR variables default value
def main():
    rootpath = "./CF_MenuID_setting/"
    tree = ET.parse(rootpath + 'project.variables')
    root = tree.getroot()
    f = open(rootpath + "setMenuIDvarible8.java")
    lines = f.readlines()
    f.close()
    for line in lines:
        line = line.split('Assign(')[1].split(', true)')[0]
        name = line.split(',')[0].replace('"', '').strip()
        ID = line.split(',')[1].replace('"', '').strip()
        print(name, ID)
        root.find(f".//variable[@name='{name}']").set("value", ID)
        if root.find(f".//variable[@name='{name}']") is None:
            raise Exception(f"Sorry, Not find Key: {name}")

    tree.write(rootpath + 'project.variables')
    fin = open(rootpath + 'project.variables', "rt")
    data = fin.read()
    data = data.replace(' />', '/>')
    fin.close()
    fin = open(rootpath + 'project.variables', "wt")
    fin.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
    fin.write(data)
    fin.close()


if __name__ == '__main__':
    main()
