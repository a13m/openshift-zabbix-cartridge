#!/usr/bin/python

import os
import sys
import urllib2
import hashlib
try:
    import json
except ImportError:
    import simplejson as json

from pprint import pprint

# Adapted from code in https://www.zabbix.com/forum/showthread.php?t=42114

class ZabbixAPI(object):
  def __init__(self, host, port, user="admin", passwd="zabbix"):
    self.user = user
    self.passwd = passwd
    self.url = "http://%s:%s/api_jsonrpc.php" % (host, port)

  def zbxAuth(self):
    login = {
      "jsonrpc" : "2.0",
      "method"  : "user.login",
      "params"  : {
        "user"     : self.user,
        "password" : self.passwd
      },
      "id"     : 1
    }
    res = self.printResult(login)

    if 'error' in res:
      print "Error: Connection Unsuccessful"
      sys.exit(-1)
    self.hash_pass=res["result"]
    print "Successfully Authenticated. Auth ID: " + self.hash_pass

  def zbxImport(self, filename):
    print "Importing " + filename
    file = open(filename, 'rb')

    imprt = {
      "jsonrpc": "2.0",
      "method" : "configuration.import",
      "params" : {
        "format"    :   "xml",
        "rules"     :   {
          "groups" :   {
            "createMissing"  :  True,
            "updateExisting" :  True
          },
          "hosts"     :   {
            "createMissing"   :  True,
            "updateExisting"  :  True
          },
          "templates" :  {
            "createMissing"   :  True,
            "updateExisting"  :  True
          },
          "triggers"  :  {
            "createMissing"   :  True,
            "updateExisting"  :  True
          },
          "items"      : {
            "createMissing"   :   True,
            "updateExisting"  :   True
          }
        },
        "source" :  file.read()
      },
      "auth" : self.hash_pass,
      "id"   : 2
    }

    file.close()

    res = self.printResult(imprt)
    if 'error' in res:
      print "Import unsuccessful for file: " + str(filename)
      print str(pprint(res))
      sys.exit(-1)
    else:
      print "SUCCESS!"
      print str(pprint(res))


  def printResult(self, var):
    data = json.dumps(var)
    request = urllib2.Request(self.url, data, {"Content-Type" : "application/json"})
    response = urllib2.urlopen(request)
    return json.load(response)

if __name__ == "__main__":
  zbx = ZabbixAPI(os.environ['OPENSHIFT_ZABBIX_IP'], os.environ['OPENSHIFT_ZABBIX_PORT'])
  zbx.zbxAuth()
  zbx.zbxImport(sys.argv[1])

