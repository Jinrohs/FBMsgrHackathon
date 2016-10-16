#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import numpy
import sys
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
import argparse
import textwrap

def draw_text_multilines(img, text):
  draw = PIL.ImageDraw.Draw(img)
  draw.font = PIL.ImageFont.truetype("ipamjm.ttf", 40)
  img_size = numpy.array(img.size)
  max_width = 16
  max_lines = 3
  ratio_margin = 0.2
  if len(text) <= max_width:
    treat_text_singleline(img_size, draw, text)
    return
  
  lines = textwrap.wrap(text, width=max_width)
  for i in range(len(lines)):
    if (i == max_lines):
      break
    txt_size = numpy.array(draw.font.getsize(lines[i]))
    pos = (img_size - txt_size) / 2
    pos[1] = img_size[1] * ratio_margin  + img_size[1] * (1- ratio_margin * 2)/max_lines * i 
    pos_set = tuple(pos.tolist()) #numpy nd array is not appropriate. Convert to a tuple 
    draw.text(pos_set, lines[i], fill="black")

def treat_text_singleline(img_size, draw, text):
  txt_size = numpy.array(draw.font.getsize(text))
  pos = (img_size - txt_size) / 2
  pos_set = tuple(pos.tolist()) #numpy nd array is not appropriate. Convert to a tuple
  draw.text(pos_set, text, fill="black")

def parse_args():
  parser = argparse.ArgumentParser(description='')
  parser.add_argument(
    'text',
    help=u"本文",
    type=lambda s: unicode(s, 'utf8')
  )
  parser.add_argument(
    'type',
    help=u"S or M"
  )
  parser.add_argument(
    'output',
    help=u"画像の保存先"
  )
  return parser.parse_args()

if __name__ == '__main__':
  args = parse_args()
  img = PIL.Image.open("./emotion_m_2x/emotion_m1_2x.png")
  text = args.text
  draw_text_multilines(img, text)
  img.save(args.output)
