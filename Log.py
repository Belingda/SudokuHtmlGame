try:
    f = open('log.txt', 'a')
except Exception as error:
    print str(error)
    f.close()


def WriteToRecordFile(ip, time):
    record = "user's IP:%s time:%s" % (ip, time)
    global f
    f.write(record + '\n')
    f.flush()
    print("record:%s" % record)
