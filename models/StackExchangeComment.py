

# < row
# Id = "1"
# PostTypeId = "1"
# AcceptedAnswerId = "2"
# CreationDate = "2010-07-19T19:36:53.637"
# Score = "28"
# ViewCount = "860"
# Body = "&lt;p&gt;It's inevitable that we will get lots of R questions in this forum. Should we:&lt;/p&gt;&#xA;&#xA;&lt;ol&gt;&#xA;&lt;li&gt;Bounce them all to SO&lt;/li&gt;&#xA;&lt;li&gt;Answer all questions, even when it's clearly programming and not statistics.&lt;/li&gt;&#xA;&lt;li&gt;Answer the question unless it clearly has no statistical content.&lt;/li&gt;&#xA;&lt;/ol&gt;&#xA;&#xA;&lt;p&gt;I would vote for 3.&lt;/p&gt;&#xA;"
# OwnerUserId = "8"
# LastEditorUserId = "22047"
# LastEditDate = "2014-10-08T17:53:57.573"
# LastActivityDate = "2014-10-08T17:53:57.573"
# Title = "How to answer R questions"
# Tags = "&lt;discussion&gt;&lt;faq&gt;&lt;r&gt;"
# AnswerCount = "6"
# CommentCount = "6"
# FavoriteCount = "1" / >

class StackExchangeComment:
    # XML ATTRIBUTE names
    ATTRIBUTE_ID = "Id"
    ATTRIBUTE_CREATION_DATE = "CreationDate"
    ATTRIBUTE_SCORE = "Score"
    ATTRIBUTE_VIEWCOUNT = "ViewCount"
    ATTRIBUTE_BODY = "Body"
    ATTRIBUTE_ANSWER_COUNT = "AnswerCount"
    ATTRIBUTE_COMMENT_COUNT = "CommentCount"
    ATTRIBUTE_FAVORITE_COUNT = "FavoriteCount"


    def __init__(self):
        self.id = None
        self.creationDate = None
        self.score = None
        self.viewCount = None
        self.body = None
        self.answerCount = None
        self.commentCount = None
        self.favoriteCount = None


