import nfc
#from nfc.clf import RemoteTarget

clf=nfc.ContactlessFrontend()
assert clf.open('ttyS0') is True
tag = clf.connect(rdwr={'on-connect': lambda tag: False})
print(tag)
assert tag.ndef is not None
for record in tag.ndef.records:
    print(record)