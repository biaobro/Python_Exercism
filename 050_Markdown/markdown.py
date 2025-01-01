# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : markdown.py
@Project            : Python_050_Markdown
@CreateTime         : 2023/2/22 22:40
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/22 22:40
@Version            : 1.0
@Description        : None
"""
import re


def parse(markdown):
    # split the text into list
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for line in lines:
        # match the pattern with six #
        if re.match('###### (.*)', line) is not None:
            line = '<h6>' + line[7:] + '</h6>'
        # match the pattern with five #
        elif re.match('##### (.*)', line) is not None:
            line = '<h5>' + line[6:] + '</h5>'
        # match the pattern with four #
        elif re.match('#### (.*)', line) is not None:
            line = '<h4>' + line[5:] + '</h4>'
        # match the pattern with three #
        elif re.match('### (.*)', line) is not None:
            line = '<h3>' + line[4:] + '</h3>'
        # match the pattern with two #
        elif re.match('## (.*)', line) is not None:
            line = '<h2>' + line[3:] + '</h2>'
        # match the pattern with one #
        elif re.match('# (.*)', line) is not None:
            line = '<h1>' + line[2:] + '</h1>'

        # if line start with *, mean unordered list
        m = re.match(r'\* (.*)', line)
        if m:
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = m.group(1)

                # match the pattern with __ seperated
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                    is_bold = True

                # match the pattern with _ seperated
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                    is_italic = True

                line = '<ul><li>' + curr + '</li>'
            else:
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    is_bold = True

                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    is_italic = True
                if is_bold:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                if is_italic:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                line = '<li>' + curr + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        m = re.match('<h|<ul|<p|<li', line)
        if not m:
            line = '<p>' + line + '</p>'

        m = re.match('(.*)__(.*)__(.*)', line)
        if m:
            line = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)

        m = re.match('(.*)_(.*)_(.*)', line)
        if m:
            line = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)

        if in_list_append:
            line = '</ul>' + line
            in_list_append = False
        res += line
    if in_list:
        res += '</ul>'
    return res
