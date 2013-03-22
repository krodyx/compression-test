# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

request_freq_table = [
  (   0,      0),(   1,      0),(   2,      0),
  (   3,      0),(   4,      0),(   5,      0),
  (   6,      0),(   7,      0),(   8,      0),
  (   9,      0),(  10,      0),(  11,      0),
  (  12,      0),(  13,      0),(  14,      0),
  (  15,      0),(  16,      0),(  17,      0),
  (  18,      0),(  19,      0),(  20,      0),
  (  21,      0),(  22,      0),(  23,      0),
  (  24,      0),(  25,      0),(  26,      0),
  (  27,      0),(  28,      0),(  29,      0),
  (  30,      0),(  31,      0),( ' ',   1015),
  ( '!',   1070),( '"',    248),( '#',    134),
  ( '$',    133),( '%',  51699),( '&',  35390),
  ( "'",    103),( '(',    897),( ')',    958),
  ( '*',   1090),( '+',   1047),( ',',   4819),
  ( '-',  65428),( '.', 107763),( '/', 198044),
  ( '0',  96411),( '1',  97568),( '2', 100401),
  ( '3',  65167),( '4',  44510),( '5',  48391),
  ( '6',  43457),( '7',  47569),( '8',  43049),
  ( '9',  48704),( ':',  50383),( ';',   6713),
  ( '<',     16),( '=',  55594),( '>',     50),
  ( '?',  10299),( '@',    557),( 'A',  20358),
  ( 'B',  11689),( 'C',  14173),( 'D',  15341),
  ( 'E',   8779),( 'F',  22416),( 'G',   5665),
  ( 'H',   6092),( 'I',   7661),( 'J',   4912),
  ( 'K',   3239),( 'L',   6283),( 'M',   7952),
  ( 'N',   5858),( 'O',   6065),( 'P',   6940),
  ( 'Q',   4768),( 'R',   7305),( 'S',   8037),
  ( 'T',  10439),( 'U',   5850),( 'V',   5839),
  ( 'W',   6682),( 'X',   6246),( 'Y',   5340),
  ( 'Z',   3844),( '[',    286),('\\',      0),
  ( ']',    295),( '^',    144),( '_',  48992),
  ( '`',      9),( 'a', 155039),( 'b',  47481),
  ( 'c', 101510),( 'd',  71484),( 'e', 266868),
  ( 'f',  80484),( 'g',  60734),( 'h',  87393),
  ( 'i', 128602),( 'j',  23163),( 'k',  19215),
  ( 'l',  88869),( 'm',  85724),( 'n',  99945),
  ( 'o', 121614),( 'p', 127713),( 'q',  10028),
  ( 'r', 170852),( 's', 125075),( 't', 192825),
  ( 'u',  52443),( 'v',  21283),( 'w',  72409),
  ( 'x',  16587),( 'y',  19104),( 'z',   9528),
  ( '{',     30),( '|',    986),( '}',     30),
  ( '~',    805),( 127,      0),( 128,      0),
  ( 129,      0),( 130,      0),( 131,      0),
  ( 132,      0),( 133,      0),( 134,      0),
  ( 135,      0),( 136,      0),( 137,      0),
  ( 138,      0),( 139,      0),( 140,      0),
  ( 141,      0),( 142,      0),( 143,      0),
  ( 144,      0),( 145,      0),( 146,      0),
  ( 147,      0),( 148,      0),( 149,      0),
  ( 150,      0),( 151,      0),( 152,      0),
  ( 153,      0),( 154,      0),( 155,      0),
  ( 156,      0),( 157,      0),( 158,      0),
  ( 159,      0),( 160,      0),( 161,      0),
  ( 162,      0),( 163,      0),( 164,      0),
  ( 165,      0),( 166,      0),( 167,      0),
  ( 168,      0),( 169,      0),( 170,      0),
  ( 171,      0),( 172,      0),( 173,      0),
  ( 174,      0),( 175,      0),( 176,      0),
  ( 177,      0),( 178,      0),( 179,      0),
  ( 180,      0),( 181,      0),( 182,      0),
  ( 183,      0),( 184,      0),( 185,      0),
  ( 186,      0),( 187,      0),( 188,      0),
  ( 189,      0),( 190,      0),( 191,      0),
  ( 192,      0),( 193,      0),( 194,      0),
  ( 195,      0),( 196,      0),( 197,      0),
  ( 198,      0),( 199,      0),( 200,      0),
  ( 201,      0),( 202,      0),( 203,      0),
  ( 204,      0),( 205,      0),( 206,      0),
  ( 207,      0),( 208,      0),( 209,      0),
  ( 210,      0),( 211,      0),( 212,      0),
  ( 213,      0),( 214,      0),( 215,      0),
  ( 216,      0),( 217,      0),( 218,      0),
  ( 219,      0),( 220,      0),( 221,      0),
  ( 222,      0),( 223,      0),( 224,      0),
  ( 225,      0),( 226,      0),( 227,      0),
  ( 228,      0),( 229,      0),( 230,      0),
  ( 231,      0),( 232,      0),( 233,      0),
  ( 234,      0),( 235,      0),( 236,      0),
  ( 237,      0),( 238,      0),( 239,      0),
  ( 240,      0),( 241,      0),( 242,      0),
  ( 243,      0),( 244,      0),( 245,      0),
  ( 246,      0),( 247,      0),( 248,      0),
  ( 249,      0),( 250,      0),( 251,      0),
  ( 252,      0),( 253,      0),( 254,      0),
  ( 255,      0),( 256,  98008),
]

response_freq_table = [
  (   0,      0),(   1,      0),(   2,      0),
  (   3,      0),(   4,      0),(   5,      0),
  (   6,      0),(   7,      0),(   8,      0),
  (   9,      0),(  10,      0),(  11,      0),
  (  12,      0),(  13,      0),(  14,      0),
  (  15,      0),(  16,      0),(  17,      0),
  (  18,      0),(  19,      0),(  20,      0),
  (  21,      0),(  22,      0),(  23,      0),
  (  24,      0),(  25,      0),(  26,      0),
  (  27,      0),(  28,      0),(  29,      0),
  (  30,      0),(  31,      0),( ' ', 150473),
  ( '!',    473),( '"',  12708),( '#',    168),
  ( '$',     61),( '%',   2656),( '&',   1589),
  ( "'",    192),( '(',   2748),( ')',   2774),
  ( '*',    325),( '+',   1155),( ',',  30356),
  ( '-',  20779),( '.',  17251),( '/',   8906),
  ( '0', 105545),( '1', 120560),( '2', 111092),
  ( '3',  64221),( '4',  54584),( '5',  48154),
  ( '6',  37011),( '7',  38819),( '8',  44232),
  ( '9',  39786),( ':',  54149),( ';',   3944),
  ( '<',     19),( '=',  12726),( '>',     94),
  ( '?',    359),( '@',     15),( 'A',  10140),
  ( 'B',   4587),( 'C',   5837),( 'D',   6379),
  ( 'E',   5480),( 'F',   9230),( 'G',  27558),
  ( 'H',   3224),( 'I',   4515),( 'J',   7053),
  ( 'K',   1828),( 'L',   2904),( 'M',  33752),
  ( 'N',   7420),( 'O',   6581),( 'P',   3845),
  ( 'Q',   2354),( 'R',   3005),( 'S',  18992),
  ( 'T',  41810),( 'U',   3231),( 'V',   2673),
  ( 'W',   6426),( 'X',   2196),( 'Y',   2298),
  ( 'Z',   1946),( '[',    585),('\\',    122),
  ( ']',    596),( '^',     53),( '_',   3692),
  ( '`',     12),( 'a',  40950),( 'b',  14347),
  ( 'c',  32135),( 'd',  20907),( 'e',  53129),
  ( 'f',  16011),( 'g',  12800),( 'h',  12653),
  ( 'i',  21524),( 'j',   3744),( 'k',   3891),
  ( 'l',  13279),( 'm',  14371),( 'n',  22358),
  ( 'o',  26168),( 'p',  22154),( 'q',   3283),
  ( 'r',  19530),( 's',  14292),( 't',  24408),
  ( 'u',  23260),( 'v',   9047),( 'w',   4818),
  ( 'x',   9394),( 'y',   5364),( 'z',   2809),
  ( '{',     16),( '|',     79),( '}',     16),
  ( '~',     24),( 127,      0),( 128,      0),
  ( 129,      0),( 130,      0),( 131,      0),
  ( 132,      0),( 133,      0),( 134,      0),
  ( 135,      0),( 136,      0),( 137,      0),
  ( 138,      0),( 139,      0),( 140,      0),
  ( 141,      0),( 142,      0),( 143,      0),
  ( 144,      0),( 145,      0),( 146,      0),
  ( 147,      0),( 148,      0),( 149,      0),
  ( 150,      0),( 151,      0),( 152,      0),
  ( 153,      0),( 154,      0),( 155,      0),
  ( 156,      0),( 157,      0),( 158,      0),
  ( 159,      0),( 160,      0),( 161,      0),
  ( 162,      0),( 163,      0),( 164,      0),
  ( 165,      0),( 166,      0),( 167,      0),
  ( 168,      0),( 169,      0),( 170,      0),
  ( 171,      0),( 172,      0),( 173,      0),
  ( 174,      0),( 175,      0),( 176,      0),
  ( 177,      0),( 178,      0),( 179,      0),
  ( 180,      0),( 181,      0),( 182,      0),
  ( 183,      0),( 184,      0),( 185,      0),
  ( 186,      0),( 187,      0),( 188,      0),
  ( 189,      0),( 190,      0),( 191,      0),
  ( 192,      0),( 193,      0),( 194,      0),
  ( 195,      0),( 196,      0),( 197,      0),
  ( 198,      0),( 199,      0),( 200,      0),
  ( 201,      0),( 202,      0),( 203,      0),
  ( 204,      0),( 205,      0),( 206,      0),
  ( 207,      0),( 208,      0),( 209,      0),
  ( 210,      0),( 211,      0),( 212,      0),
  ( 213,      0),( 214,      0),( 215,      0),
  ( 216,      0),( 217,      0),( 218,      0),
  ( 219,      0),( 220,      0),( 221,      0),
  ( 222,      0),( 223,      0),( 224,      0),
  ( 225,      0),( 226,      0),( 227,      0),
  ( 228,      0),( 229,      0),( 230,      0),
  ( 231,      0),( 232,      0),( 233,      0),
  ( 234,      0),( 235,      0),( 236,      0),
  ( 237,      0),( 238,      0),( 239,      0),
  ( 240,      0),( 241,      0),( 242,      0),
  ( 243,      0),( 244,      0),( 245,      0),
  ( 246,      0),( 247,      0),( 248,      0),
  ( 249,      0),( 250,      0),( 251,      0),
  ( 252,      0),( 253,      0),( 254,      0),
  ( 255,      0),( 256,  70995),
]
