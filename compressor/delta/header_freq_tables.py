# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

request_freq_table = [
  ('\x00', 0),('\x01', 0),('\x02', 0),('\x03', 0),('\x04', 0),('\x05', 0),
  ('\x06', 0),('\x07', 0),('\x08', 0),('\t', 0),('\n', 0),('\x0b', 0),
  ('\x0c', 0),('\r', 0),('\x0e', 0),('\x0f', 0),('\x10', 0),('\x11', 0),
  ('\x12', 0),('\x13', 0),('\x14', 0),('\x15', 0),('\x16', 0),('\x17', 0),
  ('\x18', 0),('\x19', 0),('\x1a', 0),('\x1b', 0),('\x1c', 0),('\x1d', 0),
  ('\x1e', 0),('\x1f', 0),(' ', 61),('!', 9),('"', 0),('#', 0),('$', 2),
  ('%', 1433),('&', 1662),("'", 2),('(', 34),(')', 34),('*', 25),('+', 4),
  (',', 967),('-', 1379),('.', 2886),('/', 4511),('0', 3198),('1', 3331),
  ('2', 3597),('3', 2691),('4', 2251),('5', 1880),('6', 2155),('7', 1639),
  ('8', 1916),('9', 1728),(':', 171),(';', 214),('<', 0),('=', 2120),('>', 0),
  ('?', 251),('@', 0),('A', 931),('B', 481),('C', 566),('D', 696),('E', 362),
  ('F', 545),('G', 513),('H', 328),('I', 524),('J', 210),('K', 260),('L', 373),
  ('M', 287),('N', 311),('O', 288),('P', 381),('Q', 291),('R', 328),('S', 543),
  ('T', 434),('U', 386),('V', 372),('W', 295),('X', 216),('Y', 205),('Z', 199),
  ('[', 2),('\\', 0),(']', 2),('^', 0),('_', 1702),('`', 0),('a', 4237),
  ('b', 1601),('c', 3203),('d', 2392),('e', 4941),('f', 932),('g', 2297),
  ('h', 1352),('i', 3233),('j', 913),('k', 630),('l', 2082),('m', 2429),
  ('n', 3116),('o', 3286),('p', 2510),('q', 314),('r', 2646),('s', 3825),
  ('t', 3486),('u', 1298),('v', 839),('w', 1172),('x', 760),('y', 705),
  ('z', 352),('{', 12),('|', 12),('}', 12),('~', 4),('\x7f', 0),('\x80', 0),
  ('\x81', 0),('\x82', 0),('\x83', 0),('\x84', 0),('\x85', 0),('\x86', 0),
  ('\x87', 0),('\x88', 0),('\x89', 0),('\x8a', 0),('\x8b', 0),('\x8c', 0),
  ('\x8d', 0),('\x8e', 0),('\x8f', 0),('\x90', 0),('\x91', 0),('\x92', 0),
  ('\x93', 0),('\x94', 0),('\x95', 0),('\x96', 0),('\x97', 0),('\x98', 0),
  ('\x99', 0),('\x9a', 0),('\x9b', 0),('\x9c', 0),('\x9d', 0),('\x9e', 0),
  ('\x9f', 0),('\xa0', 0),('\xa1', 0),('\xa2', 0),('\xa3', 0),('\xa4', 0),
  ('\xa5', 0),('\xa6', 0),('\xa7', 0),('\xa8', 0),('\xa9', 0),('\xaa', 0),
  ('\xab', 0),('\xac', 0),('\xad', 0),('\xae', 0),('\xaf', 0),('\xb0', 0),
  ('\xb1', 0),('\xb2', 0),('\xb3', 0),('\xb4', 0),('\xb5', 0),('\xb6', 0),
  ('\xb7', 0),('\xb8', 0),('\xb9', 0),('\xba', 0),('\xbb', 0),('\xbc', 0),
  ('\xbd', 0),('\xbe', 0),('\xbf', 0),('\xc0', 0),('\xc1', 0),('\xc2', 0),
  ('\xc3', 0),('\xc4', 0),('\xc5', 0),('\xc6', 0),('\xc7', 0),('\xc8', 0),
  ('\xc9', 0),('\xca', 0),('\xcb', 0),('\xcc', 0),('\xcd', 0),('\xce', 0),
  ('\xcf', 0),('\xd0', 0),('\xd1', 0),('\xd2', 0),('\xd3', 0),('\xd4', 0),
  ('\xd5', 0),('\xd6', 0),('\xd7', 0),('\xd8', 0),('\xd9', 0),('\xda', 0),
  ('\xdb', 0),('\xdc', 0),('\xdd', 0),('\xde', 0),('\xdf', 0),('\xe0', 0),
  ('\xe1', 0),('\xe2', 0),('\xe3', 0),('\xe4', 0),('\xe5', 0),('\xe6', 0),
  ('\xe7', 0),('\xe8', 0),('\xe9', 0),('\xea', 0),('\xeb', 0),('\xec', 0),
  ('\xed', 0),('\xee', 0),('\xef', 0),('\xf0', 0),('\xf1', 0),('\xf2', 0),
  ('\xf3', 0),('\xf4', 0),('\xf5', 0),('\xf6', 0),('\xf7', 0),('\xf8', 0),
  ('\xf9', 0),('\xfa', 0),('\xfb', 0),('\xfc', 0),('\xfd', 0),('\xfe', 0),
  ('\xff', 0),(256, 1304),
]

response_freq_table = [
  ('\x00', 87),('\x01', 0),('\x02', 0),('\x03', 0),('\x04', 0),('\x05', 0),
  ('\x06', 0),('\x07', 0),('\x08', 0),('\t', 0),('\n', 0),('\x0b', 0),
  ('\x0c', 0),('\r', 0),('\x0e', 0),('\x0f', 0),('\x10', 0),('\x11', 0),
  ('\x12', 0),('\x13', 0),('\x14', 0),('\x15', 0),('\x16', 0),('\x17', 0),
  ('\x18', 0),('\x19', 0),('\x1a', 0),('\x1b', 0),('\x1c', 0),('\x1d', 0),
  ('\x1e', 0),('\x1f', 0),(' ', 8277),('!', 0),('"', 948),('#', 9),('$', 0),
  ('%', 191),('&', 203),("'", 2),('(', 191),(')', 191),('*', 6),('+', 300),
  (',', 2522),('-', 2374),('.', 1325),('/', 3266),('0', 7630),('1', 7965),
  ('2', 7636),('3', 4415),('4', 4337),('5', 3594),('6', 3253),('7', 3223),
  ('8', 3920),('9', 3306),(':', 3545),(';', 421),('<', 0),('=', 1626),('>', 0),
  ('?', 24),('@', 0),('A', 1644),('B', 820),('C', 1187),('D', 1116),('E', 954),
  ('F', 1260),('G', 1955),('H', 493),('I', 674),('J', 875),('K', 560),
  ('L', 544),('M', 2305),('N', 844),('O', 781),('P', 640),('Q', 537),('R', 555),
  ('S', 965),('T', 2550),('U', 691),('V', 504),('W', 776),('X', 459),('Y', 507),
  ('Z', 476),('[', 11),('\\', 0),(']', 11),('^', 0),('_', 436),('`', 0),
  ('a', 5171),('b', 3355),('c', 4201),('d', 3265),('e', 5511),('f', 2185),
  ('g', 2455),('h', 1166),('i', 3075),('j', 768),('k', 768),('l', 1980),
  ('m', 1582),('n', 3613),('o', 3418),('p', 1864),('q', 532),('r', 2488),
  ('s', 2906),('t', 3324),('u', 2433),('v', 1097),('w', 927),('x', 1169),
  ('y', 749),('z', 506),('{', 9),('|', 13),('}', 9),('~', 0),('\x7f', 0),
  ('\x80', 0),('\x81', 0),('\x82', 0),('\x83', 0),('\x84', 0),('\x85', 0),
  ('\x86', 0),('\x87', 0),('\x88', 0),('\x89', 0),('\x8a', 0),('\x8b', 0),
  ('\x8c', 0),('\x8d', 0),('\x8e', 0),('\x8f', 0),('\x90', 0),('\x91', 0),
  ('\x92', 0),('\x93', 0),('\x94', 0),('\x95', 0),('\x96', 0),('\x97', 0),
  ('\x98', 0),('\x99', 0),('\x9a', 0),('\x9b', 0),('\x9c', 0),('\x9d', 0),
  ('\x9e', 0),('\x9f', 0),('\xa0', 0),('\xa1', 0),('\xa2', 0),('\xa3', 0),
  ('\xa4', 0),('\xa5', 0),('\xa6', 0),('\xa7', 0),('\xa8', 0),('\xa9', 0),
  ('\xaa', 0),('\xab', 0),('\xac', 0),('\xad', 0),('\xae', 0),('\xaf', 0),
  ('\xb0', 0),('\xb1', 0),('\xb2', 0),('\xb3', 0),('\xb4', 0),('\xb5', 0),
  ('\xb6', 0),('\xb7', 0),('\xb8', 0),('\xb9', 0),('\xba', 0),('\xbb', 0),
  ('\xbc', 0),('\xbd', 0),('\xbe', 0),('\xbf', 0),('\xc0', 0),('\xc1', 0),
  ('\xc2', 0),('\xc3', 0),('\xc4', 0),('\xc5', 0),('\xc6', 0),('\xc7', 0),
  ('\xc8', 0),('\xc9', 0),('\xca', 0),('\xcb', 0),('\xcc', 0),('\xcd', 0),
  ('\xce', 0),('\xcf', 0),('\xd0', 0),('\xd1', 0),('\xd2', 0),('\xd3', 0),
  ('\xd4', 0),('\xd5', 0),('\xd6', 0),('\xd7', 0),('\xd8', 0),('\xd9', 0),
  ('\xda', 0),('\xdb', 0),('\xdc', 0),('\xdd', 0),('\xde', 0),('\xdf', 0),
  ('\xe0', 0),('\xe1', 0),('\xe2', 0),('\xe3', 0),('\xe4', 0),('\xe5', 0),
  ('\xe6', 0),('\xe7', 0),('\xe8', 0),('\xe9', 0),('\xea', 0),('\xeb', 0),
  ('\xec', 0),('\xed', 0),('\xee', 0),('\xef', 0),('\xf0', 0),('\xf1', 0),
  ('\xf2', 0),('\xf3', 0),('\xf4', 0),('\xf5', 0),('\xf6', 0),('\xf7', 0),
  ('\xf8', 0),('\xf9', 0),('\xfa', 0),('\xfb', 0),('\xfc', 0),('\xfd', 0),
  ('\xfe', 0),('\xff', 0),(256, 5072),
]

