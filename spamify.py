import argparse
import email
import getpass
import imaplib

parser = argparse.ArgumentParser(description='Find spam message sent to a labelled Gmail address.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-u', '--username',  default='your_username',
        help='Gmail username.')
parser.add_argument('-p', '--password',  
        help='Gmail password.')
args = parser.parse_args()

if not args.username:
    args.username = raw_input("Enter your Gmail username: ")
if not args.password:
    args.password = getpass.getpass("Enter your password: ")

m = imaplib.IMAP4_SSL("imap.gmail.com")
m.login(args.username, args.password)
args.password = None

m.select("[Gmail]/Spam", readonly=True)

result, data = m.search(None, "ALL")
ids = data[0] # data is a list
id_list = ids.split() # ids is a space separated string

print len(id_list), "spam emails found"

count = 0
for email_id in id_list:
    result, data = m.fetch(email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
    raw_email = data[0][1] # here's the body, which is raw text of the whole email including headers and alternate payloads
    email_message = email.message_from_string(raw_email)
    if email_message['To'] and args.username+"+" in email_message['To']:
        print "From:\t\t", email_message['From']
        print "To:\t\t", email_message['To']
        print "CC:\t\t", email_message['Cc']
        print "Subject:\t", email_message['Subject']
        print "************ CONTAINS " + args.username + "+  ************"
        count += 1
        print "-------------------------------------"

m.logout()

print count, "emails containing", args.username+"+"
