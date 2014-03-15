#!/usr/bin/env python
"""Command-line Gmail message reader."""
import argparse
import email
import getpass
import imaplib

parser = argparse.ArgumentParser(
    description='Command-line Gmail message reader.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument(
    '-u', '--username',  default='your_username', help='Gmail username.')
parser.add_argument('-p', '--password', help='Gmail password.')
parser.add_argument(
    '-n', '--number', default=1, type=int,
    help='Number of emails to show.')
parser.add_argument(
    '-t', '--to',
    help='Only emails with this in "To:".')
parser.add_argument(
    '-f', '--from_text',
    help='Only emails with this in "From:".')
parser.add_argument(
    '-c', '-cc', '--cc',
    help='Only emails with this in "CC:".')
parser.add_argument(
    '-B', '-bcc', '--bcc',
    help='Only emails with this in "BCC:".')
parser.add_argument(
    '-s', '--subject',
    help='Only emails with this in "Subject:".')
parser.add_argument(
    '-b', '--body',
    help='Only emails with this in "Body:".')
parser.add_argument(
    'text', nargs='?',
    help='Only emails with this in any field.')
parser.add_argument(
    '--summary', '--nobody', action='store_true',
    help="Show summary (don't show body).")

args = parser.parse_args()

# SEARCH Command:
# http://www.travelingfrontiers.com/projects/doku.php?id=imapv4_protocol
search_string = "(ALL"

if args.to:
    search_string += ' TO "%s"' % args.to
if args.from_text:
    search_string += ' FROM "%s"' % args.from_text
if args.cc:
    search_string += ' CC "%s"' % args.cc
if args.bcc:
    search_string += ' BCC "%s"' % args.bcc
if args.subject:
    search_string += ' SUBJECT "%s"' % args.subject
if args.body:
    search_string += ' BODY "%s"' % args.body
if args.text:
    search_string += ' TEXT "%s"' % args.text

search_string += ")"
print "search_string:", search_string

if not args.username:
    args.username = raw_input("Enter your Gmail username: ")
if not args.password:
    args.password = getpass.getpass("Enter your password: ")

m = imaplib.IMAP4_SSL("imap.gmail.com")
m.login(args.username, args.password)
args.password = None

m.select("[Gmail]/All Mail", readonly=True)
result, data = m.search(None, search_string)

ids = data[0]  # data is a list
id_list = ids.split()  # ids is a space separated string

print len(id_list), "emails found"

for email_id in reversed(id_list):
    # Fetch the email body (RFC822) for the given ID
    result, data = m.fetch(email_id, "(RFC822)")
    # Here's the body, which is raw text of the whole email
    # including headers and alternate payloads
    raw_email = data[0][1]
    email_message = email.message_from_string(raw_email)
    print "From:\t\t", email_message['From']
    print "To:\t\t", email_message['To']
    if email_message['Cc']:
        print "CC:\t\t", email_message['Cc']
    print "Date:\t\t", email_message['Date']
    print "Subject:\t", email_message['Subject']
    for part in email_message.walk():
         # Ignore attachments/html
        if (not args.summary) and (part.get_content_type() == "text/plain"):
            body = part.get_payload(decode=True)
            print body
    print "-------------------------------------"
    args.number -= 1
    if args.number == 0:
        break

m.logout()

# End of file
