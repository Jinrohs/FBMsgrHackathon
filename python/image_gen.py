#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import sys
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont

def draw_text_at_center(img, text):
  draw = PIL.ImageDraw.Draw(img)
  #draw.font = PIL.ImageFont.load_default() 
  draw.font = PIL.ImageFont.truetype("ipamjm.ttf", 40)

  img_size = numpy.array(img.size)
  txt_size = numpy.array(draw.font.getsize(text))
  pos = (img_size - txt_size) / 2
  pos_set = tuple(pos.tolist()) #numpy nd array is not appropriate. Convert to a tuple
  draw.text(pos_set, text, fill="black")

if __name__ == '__main__':
	argvs = sys.argv
	argc = len(argvs)
	if (argc != 3):   # 引数が足りない場合は、その旨を表示
        	print 'Usage: # python %s inputFile outputFile' % argvs[0]
        	quit()
	img = PIL.Image.open(argvs[1])
   	text = u"さっさとしねよこの豚野郎め！"
   	draw_text_at_center(img, text)
   	img.save(argvs[2])
