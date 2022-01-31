import xml.etree.ElementTree as ET
import re
import sys

tree = ET.parse('odoo-pycharm-templates/Odoo.xml')
root = tree.getroot()
for template in root:
    # # import ipdb; ipdb.set_trace()
    value = template.attrib.get('value')
    name = template.attrib.get('name')
    print(name)
    name = "%s - %s" % (name, name)
    res = re.findall(r"(\$(.*?)\$)+", value)
    for i in range(0, len(res)):
        rr = res[i]
        value = value.replace(rr[0], '${%s:%s}' % (i, rr[1]))

    try:
        language = template.find("context").find("option").attrib.get('name')
        language = language.lower()
    except:
        e = sys.exc_info()[0]
        print(e)
        pass

    if language not in ['xml', 'python']:
        language = 'other'

    f = open("snippets/%s/%s" % (language, name), "w")
    f.write(value)
    f.close()
