#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import numpy
import sys
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
import argparse

def draw_text_at_center(img, text):
  draw = PIL.ImageDraw.Draw(img)
  #draw.font = PIL.ImageFont.load_default()
  draw.font = PIL.ImageFont.truetype("ipamjm.ttf", 40)

  img_size = numpy.array(img.size)
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
  img = PIL.Image.open("emotion.png")
  text = args.text
  draw_text_at_center(img, text)
  img.save(args.output)
