"""
https://automatetheboringstuff.com/chapter16/

SMTP puedes mandar correos
IMAP puedes revisar tus correos
"""

import smtplib

conn = smtplib.SMTP("smtp.gmail.com", 587)
print(type(conn))

print(conn.ehlo())
conn.starttls()

conn.login(user, password) #por cuestiones de seguridad con gmail, hasta aqui me detengo jaja

conn.sendmail(from_addr, to_addrs, msg)

conn.quit() #desconectado del smtp server

