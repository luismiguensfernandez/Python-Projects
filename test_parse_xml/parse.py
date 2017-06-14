import xml.dom.minidom as xml


if __name__ == '__main__':
    doc = xml.parse("test.xml")
    records = doc.getElementsByTagName('record')
    for record in records:
        metadata = record.getElementsByTagName('metadata')[0]
        print metadata.getElementsByTagName('gml:beginPosition')[0].firstChild.data


