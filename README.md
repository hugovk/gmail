Some Python scripts for using Gmail.

gmail.py
========
````
usage: gmail.py [-h] [-u USERNAME] [-p PASSWORD] [-n NUMBER] [-t TO]
                [-f FROM_TEXT] [-c CC] [-B BCC] [-s SUBJECT] [-b BODY]
                [--summary]
                [text]

Gmail message reader.

positional arguments:
  text                  Only emails with this in any field. (default: None)

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Gmail username. (default: your_username)
  -p PASSWORD, --password PASSWORD
                        Gmail password. (default: None)
  -n NUMBER, --number NUMBER
                        Number of emails to show. (default: 1)
  -t TO, --to TO        Only emails with this in "To:". (default: None)
  -f FROM_TEXT, --from_text FROM_TEXT
                        Only emails with this in "From:". (default: None)
  -c CC, -cc CC, --cc CC
                        Only emails with this in "CC:". (default: None)
  -B BCC, -bcc BCC, --bcc BCC
                        Only emails with this in "BCC:". (default: None)
  -s SUBJECT, --subject SUBJECT
                        Only emails with this in "Subject:". (default: None)
  -b BODY, --body BODY  Only emails with this in "Body:". (default: None)
  --summary, --nobody   Show summary (don't show body). (default: False)
  ````
  
spamify.py
==========
  
  ````
  usage: spamify.py [-h] [-u USERNAME] [-p PASSWORD]

Find spam message sent to a labelled Gmail address.

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Gmail username. (default: your_username)
  -p PASSWORD, --password PASSWORD
                        Gmail password. (default: None)
