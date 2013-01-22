#!/usr/bin/env python

"""
compression_test.py

Tests various HTTP header compression algorithms, to compare them.
"""

# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# pylint: disable=W0311

from collections import defaultdict
from importlib import import_module
import sys
import locale
import optparse

from lib.harfile import read_har_file
from lib.processors import Processors


class CompressionTester(object):
  """
  This is the thing.
  """
  msg_types = ['req', 'res']
  streamifier_dir = "lib.streamifiers"
  default_processor = "http1"
  c = {
    'req':{
      '_TOTAL_HEADER_VALUE_LEN': 0,
      '_TOTAL_MESSAGES': 0,
      '_TOTAL_HEADER_INSTANCES': 0
    },
    'res':{
      '_TOTAL_HEADER_VALUE_LEN': 0,
      '_TOTAL_MESSAGES': 0,
      '_TOTAL_HEADER_INSTANCES': 0
    }
  }

  def __init__(self, output):
    self.options, self.args = self.parse_options()
    self.output = output
    self.tsv_out = defaultdict(list)  # accumulator for TSV output
    self.processors = Processors(self.options, self.msg_types, output)
    self.streamify = self.load_streamifier(self.options.streamifier)
    self.run()

  def run(self):
    "Let's do this thing."
    streams = []
    for filename in self.args:
      har_requests, har_responses = read_har_file(filename)
      messages = zip(har_requests, har_responses)
      streams.extend(self.streamify(messages))
    for stream in streams:
      section = self.c[stream.msg_type]
      for (hdrs, host) in stream.messages:
        section['_TOTAL_MESSAGES'] += 1
        for (key,val) in hdrs.iteritems():
          if not key in section:
            section[key] = {'C':0,'T':0,'A':0.0,'L':sys.maxint,'H':0}
          l = len(val)
          section['_TOTAL_HEADER_VALUE_LEN'] += l
          section['_TOTAL_HEADER_INSTANCES'] += 1
          k = section[key]
          k['C'] += 1
          k['T'] += l
          k['A'] = k['T'] / k['C']
          k['L'] = min(k['L'], l)
          k['H'] = max(k['H'], l)
    for section,data in self.c.iteritems():
      print '%s: ' % section
      print 'TOTAL HEADER VALUE LENGTH: %d' % data['_TOTAL_HEADER_VALUE_LEN']
      print 'NUMBER OF UNIQUE HEADERS:  %d' % (len(data) - 3)
      print 'TOTAL NUMBER OF HEADERS:   %d' % data['_TOTAL_HEADER_INSTANCES']
      print 'TOTAL NUMBER OF MESSAGES:  %d' % data['_TOTAL_MESSAGES']
      for (key,value) in sorted(data.iteritems(), key=lambda(k,v): (v,k), reverse=True):
        if not key[0] == '_':
          print '%s: ' % key
          print ' Instances: %d' % value['C']
          print ' Total:     %d' % value['T']
          print ' Average:   %.2f' % value['A']
          print ' Low:       %d' % value['L']
          print ' High:      %d' % value['H']
          print ' Percent of Total Size: %.6f' % ((float(value['T']) / float(data['_TOTAL_HEADER_VALUE_LEN'])) * 100)
          print ' Percent of Total Count: %.6f' % ((float(value['C']) / float(data['_TOTAL_HEADER_INSTANCES'])) * 100)
          print '\n'

    
  def load_streamifier(self, name):
    "Load the streamifier specified in the options."
    return import_module("%s.%s" % (self.streamifier_dir, name)) \
      .Streamifier([p.name for p in self.processors.processors['req']]) \
      .streamify

  def parse_options(self):
    "Parse command-line options and return (options, args)."
    optp = optparse.OptionParser()
    optp.add_option('-v', '--verbose',
                  type='int',
                  dest='verbose',
                  help='set verbosity, 1-5 (default: %default)',
                  default=0,
                  metavar='VERBOSITY')
    optp.add_option('-c', '--codec',
                  action='append',
                  dest='processor_names',
                  help='compression modules to test, potentially with '
                  'parameters. '
                  'e.g. -c spdy3 -c fork="abc" '
                  '(default: %default)',
                  default=[self.default_processor])
    optp.add_option('-b', '--baseline',
                  dest='baseline',
                  help='baseline codec to base comparisons upon. '
                  '(default: %default)',
                  default=self.default_processor)
    optp.add_option('-t', '--tsv',
                  action="store_true",
                  dest="tsv",
                  help="output TSV.",
                  default=False)
    optp.add_option('-s', '--streamifier',
                  dest="streamifier",
                  help="streamifier module to use (default: %default).",
                  default="public_suffix")
    optp.add_option('--prefix',
                  action="store",
                  dest="prefix",
                  help="Prefix for TSV file output.",
                  default="")
    return optp.parse_args()


if __name__ == "__main__":
  import os
  import sys
  if os.name == "nt":
    locale.setlocale(locale.LC_ALL, 'english-us')
  else:
    locale.setlocale(locale.LC_ALL, 'en_US')
  CompressionTester(sys.stdout.write)
