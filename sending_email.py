import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
conn.login('baldeaguirre@gmail.com', '*****')

conn.sendmail('baldeaguirre@gmail.com', 'baldeaguirre@gmail.com', 'Subject: Test.\n\n '
                                                                  'To myself:\n'
                                                                  'This a simple test.\n\n'
                                                                  '-Balde')
conn.quit()