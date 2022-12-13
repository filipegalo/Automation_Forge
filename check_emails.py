import email
from email.parser import BytesParser
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Connect to the email account and retrieve a list of unread emails
server = email.server('imap.gmail.com', 'username', 'password')
unread_emails = server.search(['UNSEEN'])

# Parse the emails and extract the relevant information
parser = BytesParser()
for email_id in unread_emails:
    email = parser.parsebytes(server.fetch(email_id, ['BODY[]'])[b'BODY[]'])

    sender = email['from']
    subject = email['subject']
    body = email.get_payload()

    # Use NLP to identify important keywords or phrases in the email
    keywords = ['urgent', 'important', 'deadline', 'meeting']
    words = word_tokenize(body)
    important_words = [word for word in words if word.lower() in keywords]

    # Highlight the identified keywords in the email
    highlighted_body = body
    for word in important_words:
        highlighted_body = highlighted_body.replace(word, '<b>' + word + '</b>')

    # Display the highlighted email to the user
    print('From:', sender)
    print('Subject:', subject)
    print('Body:', highlighted_body)
