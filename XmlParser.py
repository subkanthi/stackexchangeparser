import xml.dom.minidom;

#
#< row
#Id = "5"
#PostId = "17"
#Score = "3"
#Text = "Any professor who is asked a homework question explicitly in office hours would tell the student to do a little work and rephrase the question, which is essentially what I mean."
#CreationDate = "2010-07-19T20:48:41.983"
#UserId = "5" / >


class XmlParser:
    def __init__(self, file):
        self.file = file


    def parseXml(self):
        xmldoc = xml.dom.minidom.parse(self.file)
        itemlist = xmldoc.getElementsByTagName('item')
        print(len(itemlist))
        print(itemlist[0].attributes['name'].value)
        for s in itemlist:
            print(s.attributes['name'].value)

