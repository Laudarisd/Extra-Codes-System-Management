import os
from shutil import copyfile
import sys
import xml.etree.ElementTree

imgpath = sys.argv[1]
xmlpath = sys.argv[2]
testpath = sys.argv[3]
testxmlpath = sys.argv[4]

imglist = sorted(os.listdir(imgpath))
testlist = sorted(os.listdir(testpath))

xml_filename, ext = imglist[-1].split('.')

for imgfile in imglist:
    filename, ext = imgfile.split('.')
    with open('trainval.txt', 'a') as f:
        f.write('%s %s.xml\n' % (imgpath + imgfile, xmlpath + filename))

#copyfile('trainval.txt', 'test.txt')

for testfile in testlist:
    filename, ext = testfile.split('.')
    with open('test.txt', 'a') as f:
        f.write('%s %s.xml\n' % (testpath + testfile, testxmlpath + filename))

e = xml.etree.ElementTree.parse(xmlpath + xml_filename + '.xml').getroot()
w = e[4][0].text
h = e[4][1].text

for testfile in testlist:
    filename, ext = testfile.split('.')
    with open('test_name_size.txt', 'a') as f:
        f.write('%s %s %s\n' % (filename, w, h))
