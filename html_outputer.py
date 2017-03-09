#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
#页面输出
class HtmlOutputer(object):
    #构造函数
    def __init__(self):
        self.datas = []

    #收集数据
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    #以页面输出数据
    def output_html(self):
        fout = open('output.html', 'w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()