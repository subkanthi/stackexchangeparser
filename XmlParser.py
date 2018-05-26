import xml.dom.minidom;
from typing import List

from StackExchangeComment import StackExchangeComment;

class XmlParser:



    def __init__(self, file):
        self.file = file


    # Function to parse XML file based on stackoverflow
    # Structure
    def parseXml(self):
        xmldoc = xml.dom.minidom.parse(self.file)
        itemlist = xmldoc.getElementsByTagName('row')
        print(len(itemlist))
        commentList: List[StackExchangeComment] = []
        for s in itemlist:
            comment = StackExchangeComment()
            comment.id = self.getAttributeValue(StackExchangeComment.ATTRIBUTE_ID, s)
            comment.answerCount = self.getAttributeValue(StackExchangeComment.ATTRIBUTE_ANSWER_COUNT, s)
            comment.body = self.getAttributeValue(StackExchangeComment.ATTRIBUTE_BODY, s)
            comment.creationDate = self.getAttributeValue(StackExchangeComment.ATTRIBUTE_CREATION_DATE, s)
            comment.commentCount = self.getAttributeValue(StackExchangeComment.ATTRIBUTE_COMMENT_COUNT, s)
            comment.favoriteCount = self.getAttributeValue(StackExchangeComment.ATTRIBUTE_FAVORITE_COUNT, s)
            comment.viewCount = self.getAttributeValue(StackExchangeComment.ATTRIBUTE_VIEWCOUNT, s)
            commentList.append(comment)

        return commentList

    # Wrapper function to check if attribute
    # exists before trying to retrieve the
    # value of attribute
    def getAttributeValue(self, attributeName, element):
        if element.hasAttribute(attributeName):
            return element.attributes[attributeName].value;



