import ConfigParser

# [/Exception]
# fail on = Fail on
# msg e= MessagingException
# rfof = Reconnect fail on folder
# server fail = Server Fail
# skip msg = Skip one message Exception(E)
# sync = Sync mails failed
#
# [/Exception/fail on]
# getMessageByUID = Fail on getMessageByUID
# getReceivedDate = Fail on getReceivedDate
# list folder = Fail on list folder
# open folder = Fail on open folder
#
# [/Exception/msg e]
# FolderClosedException = javax.mail.FolderClosedException
# MessagingException = javax.mail.MessagingException
# StoredClosedException = javax.mail.StoreClosedException
#
# [/Exception/rfof]
# MessagingException = javax.mail.MessagingException
#
# [/Exception/server fail]
# qq = Server fail: imap.qq.com
# 163 = Server fail: imap.163.com
# sina = Server fail: imap.sina.com
# outlook = Server fail: imap-mail.outlook.com
#
# [/Exception/skip msg]
# FolderClosedException = javax.mail.FolderClosedException
# IndexOutOfBoundsException = java.lang.IndexOutOfBoundsException
# NullPointerException = java.lang.NullPointerException
# Cannot load header = javax.mail.MessagingException: Cannot load header
#
# [/Exception/sync]
# hotmail = @hotmail.com
# qq = @qq.com
# 163 = @163.com
# outlook = @outlook.com
# sina = @sina.com


#config = ConfigParser.ConfigParser()

from LogMiner.functions import MyConfigParser
#config = MyConfigParser()
config = ConfigParser.SafeConfigParser()
config.optionxform = str
config.read('example.cf')

print config.sections()
print config.options('/Exception/msg e')
print config.items('/Exception/msg e')

import json
a = config.get('/Exception','rfof')
print a

import ast
mlist = eval(a)
print type(mlist)
print mlist

b = config.get('/Exception','server fail')
print b
blist = eval(b)
print blist
print type(blist)

print isinstance(ast.literal_eval(a),str)

