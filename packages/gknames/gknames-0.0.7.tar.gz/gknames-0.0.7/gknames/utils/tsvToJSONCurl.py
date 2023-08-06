#!/usr/bin/env python
"""Generate all the apfit parameters from the DDC files, or calculate them from scratch.

Usage:
  %s <inputFile> [--survey_database=<survey_database>] [--token=<token>] [--server=<server>] [--serverurl=<serverurl>]
  %s (-h | --help)
  %s --version

Options:
  -h --help                            Show this screen.
  --version                            Show version.
  --survey_database=<survey_database>  Survey database [default: atlas3]
  --token=<token>                      Survey database [default: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa]
  --server=<server>                    Webserver and port hosting the nameserver [default: http://127.0.0.1:8085].
  --serverurl=<serverurl>              Webserver URL of the API [default: /sne/nameserver_atlas/eventapi/].

"""
import sys
__doc__ = __doc__ % (sys.argv[0], sys.argv[0], sys.argv[0])
from docopt import docopt
import os, MySQLdb, shutil, re
from gkutils.commonutils import dbConnect, Struct, cleanOptions, readGenericDataFile

import json

def main(argv = None):
    opts = docopt(__doc__, version='0.1')
    opts = cleanOptions(opts)

    # Use utils.Struct to convert the dict into an object for compatibility with old optparse code.
    options = Struct(**opts)


    data = readGenericDataFile(options.inputFile, delimiter='\t')
    for row in data:
        row["survey_database"] = options.survey_database
        print("echo %s" % json.dumps(row).replace('"', '\\"'))
        print("curl -s -X POST %s%s -d '%s' -H 'Content-Type: application/json' -H 'Authorization: Token %s'" % (options.server, options.serverurl, json.dumps(row), options.token))
        print("echo \"\"")
        print("echo \"\"")


if __name__=='__main__':
    main()

