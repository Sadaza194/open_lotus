from lotus.user import User
from lotus.user import CustomUserManager
from lotus.entry import Entry
from lotus.entryChilds import Memory
from lotus.entryChilds import Journal
from lotus.question import Question
from lotus.answer import Answer
from lotus.textAnswer import TextAnswer
from lotus.likertAnswer import LikertAnswer
from lotus.questionTracker import QuestionTracker





Objects:
User		
UserID	Integer	NOT NULL, Primary Key, Auto Increment, Unique
Name	Varchar(60)	NOT NULL, encrypted
Email	Varchar(60)	NOT NULL, contains('@'), encrypted
Password	Varchar(255)	NOT NULL, Min 8, Hash
Colourscheme	Integer	NOT NULL, Default('white')
Admin	bool	NOT NULL, Default('false')

    User
        UserID
        Name
        Email
        Password
        ColourScheme
    Client(User)
    Admin(User)

Entry
    JournID
    UserID
    Text
    Title
    Date

Entry		
EntryID	Integer	NOT NULL, Primary Key, Auto Increment, Unique
UserID	Integer	NOT NULL, Foreign Key(User)
Date	DateTime	NOT NULL, Auto Increment
Journal	Bool	NOT NULL, Default('true')

Journal(Entry)

Memory		
MemoryID	Integer	NOT NULL, Primary Key, Auto Increment, Unique
EntryID	Integer	NOT NULL, Foreign Key(Entry)
Emotion	Varchar(40)	NOT NULL
Text	Varchar(60)	


Memory(Entry)
		
Journal		
JournalID	Integer	NOT NULL, Primary Key, Auto Increment, Unique
EntryID	Integer	NOT NULL, Foreign Key(Entry)
Text	Mediumtext	encrypted


    Emotion
Question
    QuestID
    QuestText
    QuestionType
    Active
    Frequency

Question		
QuestionID	Integer	NOT NULL, Primary Key, Auto Increment, Unique
QuestionText	Varchar(255)	NOT NULL
QuestionType	Integer	NOT NULL
Active	bool	NOT NULL, Default('true')
Frequency	Varchar(20)	NOT NULL, Default('daily')


Answer
    AnsID
    UserID
    QuestID
    Answer
    Date

Answer		
AnswerID	Integer	NOT NULL, Primary Key, Auto Increment, Unique
QuestionID	Integer	NOT NULL, Foreign Key(Question)
UserID	Integer	NOT NULL, Foreign Key(User)
Date	DateTime	NOT NULL, Auto Increment

TextAnswer		
TextID	Integer	NOT NULL, Primary Key, Auto Increment, Unique
AnswerID	Integer	NOT NULL, Foreign Key(Answer)
text	Varchar(30)	encrypted

LikertAnswer		
LikertID	Integer	NOT NULL, Primary Key,  Auto Increment, Unique
AnswerID	Integer	NOT NULL, Foreign Key(Answer)
Value	Integer	


Questiontracker		
UserID	Integer	NOT NULL, Foreign Key(User), Primary Key
QuestionID	Integer	NOT NULL, Foreign Key(Question), Primary Key
Date	DateTime	NOT NULL