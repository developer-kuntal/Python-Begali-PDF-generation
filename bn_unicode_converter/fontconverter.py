"# -*- coding: utf-8 -*-"
#
#  License: MIT 
#  
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# 
#  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# 
#  THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import stm as engine

def main():
#~ txt="xy!› öœ" 
#   for storynum in range(1,21):
    # with open(r'D:\PythonProject\dictionary_project\bn_unicode_converter\story1.txt', 'r') as content_file: 
    txt = "বেষ্টিত" #content_file.read()
    optxt = txt.encode('utf-8')
    print(optxt)
    # try:
    txt=b'\xe0\xa6\xac\xe0\xa7\x87\xe0\xa6\xb7\xe0\xa7\x8d\xe0\xa6\x9f\xe0\xa6\xbf\xe0\xa6\xa4'.decode('utf-8')
    print(txt)
    optxt = engine.convert(txt)
    # except UnicodeDecodeError:
    #     pass
    # except AttributeError:
    #     pass
    print(optxt)
    # print(storynum)
    # optxt = optxt.encode('utf-8')
    # fo = open('unicode/story{0}.txt'.format(storynum), "w")
    # fo.write(optxt)
    # fo.close()

    return 0

if __name__ == '__main__':
	main()
