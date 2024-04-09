# open_lotus

Lotus Three project

## How to deploy the app

1. Download the .zip file from the git repository
2. Unzip it and from the terminal `cd` to get into the OPEN_LOTUS folder. 
3. Create a python virtual enviroment. You can call it open-lotus-venv. TO do so you can type `python3 -m venv open-lotus-env`
4. Then type `source open-lotus-venv/bin/activate`
5. Then get into the OPEN_LOTUS folder.
6. Once there type `python -m pip install -r requirementes`. This will install the libraries required to run the app.
7. Type then `cd lotus_django` 
8. Once in there type `python manage.py runserver`
9. In the command prompt that follows that command you will find an url; it will look something like this: "http://127.0.0.1:8000/" although it may be diferent. Copy and paste in your browser. Now the app will be deployed and you will be able to interact with it. 


## File Structure

The file structure (displayed in the tree diagram) portrais the basic structure of the app. 

It is compose by a main folder: lotus_django and several subfolder with each functionality of the app (journal, memories, questions, report).

The **lotus_django** folder contains the main structure that allows the app to join all its parts. the url.py contains all the paths to each app functionality. The templates contains a **base.html** file that contains the tamplate for every page within the app and the **static** folder contains the css styles used.

Each app has a **templates** folder that contains the html pages that display the apps. It also contains a **forms.py** and a **views.py** both of them contain the main functionality of each app. 

lotus_django
├── db.sqlite3
├── journal
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_delete_memory.py
│   │   ├── 0003_alter_entry_user.py
│   │   ├── 0004_auto_20240407_0606.py
│   │   ├── 0005_auto_20240407_0627.py
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   ├── createJournal.html
│   │   ├── journalBase.html
│   │   └── viewJournals.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── lotus
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   ├── admin.cpython-39.pyc
│   │   ├── answer.cpython-39.pyc
│   │   ├── apps.cpython-39.pyc
│   │   ├── entry.cpython-39.pyc
│   │   ├── entryChilds.cpython-39.pyc
│   │   ├── likertAnswer.cpython-39.pyc
│   │   ├── models.cpython-39.pyc
│   │   ├── question.cpython-39.pyc
│   │   ├── questionTracker.cpython-39.pyc
│   │   ├── textAnswer.cpython-39.pyc
│   │   ├── urls.cpython-39.pyc
│   │   ├── user.cpython-39.pyc
│   │   └── views.cpython-39.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20240319_0552.py
│   │   ├── 0003_auto_20240319_0631.py
│   │   ├── 0004_auto_20240319_0634.py
│   │   ├── 0005_remove_answer_question_remove_answer_user_and_more.py
│   │   ├── 0006_alter_entry_user_delete_user.py
│   │   ├── 0007_user_remove_entry_user_remove_journal_entry_and_more.py
│   │   ├── 0008_delete_user.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-39.pyc
│   │       ├── 0002_auto_20240319_0552.cpython-39.pyc
│   │       ├── 0003_auto_20240319_0631.cpython-39.pyc
│   │       ├── 0004_auto_20240319_0634.cpython-39.pyc
│   │       └── __init__.cpython-39.pyc
│   ├── models.py
│   ├── static
│   │   ├── 0.jpg
│   │   ├── 1.jpg
│   │   ├── 10.jpg
│   │   ├── 11.jpg
│   │   ├── 2.jpg
│   │   ├── 3.jpg
│   │   ├── 4.jpg
│   │   ├── 5.jpg
│   │   ├── 6.jpg
│   │   ├── 7.jpg
│   │   ├── 8.jpg
│   │   ├── 9.jpg
│   │   ├── scroll.jpg
│   │   └── styles.css
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── lotus_django
│   ├── __init__.py
│   ├── __pycache__
│   │   └── __init__.cpython-39.pyc
│   ├── context_processors.py
│   ├── forms.py
│   ├── settings.py
│   ├── static
│   │   ├── 0.jpg
│   │   ├── 1.jpg
│   │   ├── 10.jpg
│   │   ├── 11.jpg
│   │   ├── 2.jpg
│   │   ├── 3.jpg
│   │   ├── 4.jpg
│   │   ├── 5.jpg
│   │   ├── 6.jpg
│   │   ├── 7.jpg
│   │   ├── 8.jpg
│   │   ├── 9.jpg
│   │   ├── scroll.jpg
│   │   └── styles.css
│   ├── templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── settings.html
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── manage.py
├── memories
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_remove_memory_entryid_remove_memory_memoryid_and_more.py
│   │   ├── 0003_alter_memory_user.py
│   │   ├── 0004_auto_20240408_2046.py
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   ├── createMemory.html
│   │   ├── memoriesBase.html
│   │   └── viewMemories.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── mydatabase
├── questions
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_question_text_answer_likertanswer_and_more.py
│   │   ├── 0003_alter_answer_user_alter_questiontracker_user.py
│   │   ├── 0004_rename_answer_id_likertanswer_answer.py
│   │   ├── 0005_auto_20240408_1725.py
│   │   ├── 0006_auto_20240408_1752.py
│   │   ├── 0007_auto_20240408_1831.py
│   │   ├── 0008_auto_20240408_2046.py
│   │   ├── 0009_auto_20240408_2052.py
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   ├── answerLikertQuestion.html
│   │   ├── answerTextQuestion.html
│   │   ├── createQuestion.html
│   │   ├── questionsBase.html
│   │   └── viewAnswers.html
│   ├── templatetags
│   │   ├── __init__.py
│   │   └── dict_filter.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── report
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── context_processors.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── templates
    │   └── report.html
    ├── tests.py
    ├── urls.py
    └── views.py
