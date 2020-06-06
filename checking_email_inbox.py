import imapclient
import pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('baldeaguirre@gmail.com', '*****')
conn.list_folders()
conn.select_folder('INBOX', readonly=True)
UIDs = conn.search(['SINCE', '01-Jan-2020'])
# conn.search(['TEXT', "data science"])

rawMessage = conn.fetch([36727], ['BODY[]', 'FLAGS'])
message = pyzmail.PyzMessage.factory(rawMessage[36727][b'BODY[]'])
print(message.get_subject(), '\n')
print(message.get_addresses('from'), '\n')
print(message.get_addresses('to'), '\n')
print(message.text_part, '\n')
print(message.html_part, '\n')
print(message.text_part.charset, '\n')
# print(message.html_part.charset, '\n')
print(message.text_part.get_payload().decode('UTF-8'), '\n')
# print(message.html_part.get_payload().decode('UTF-8'), '\n')

# Deleting emails
conn.select_folder('INBOX', readonly=False)
UIDs = conn.search(['SINCE', '01-Jan-2020'])
# conn.delete_messages([36727])

conn.logout()