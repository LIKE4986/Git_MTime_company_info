
# for year in range(2014, 2016):
#     # print(type(t))
#     with open('%s.txt' % year) as file1:
#         # 打开文件并按行读取
#         for line in file1:
#             name_and_number = line.split('')
#
#             name = name_and_number[0]
#             year = name_and_number[1]
#             # with open('%sinfo.txt' % year, 'a+') as file2:
#             #     info = str(name) + '\n'
#             #     file2.write(info)
#             print(name_and_number)
#             print(year)
#             print(name)



#对重复的公司名修改||尝试
# l_companies = [('a', 123),('a',1234),('b',456), ('c',678), ('b', 999)]
#
# # #判断是否有相同的公司名，如果有，在第二个名称后面加“1”
# # l_company_name_sort = sorted(l_company_name)
# # for i in range(0, len(l_company_name_sort)):
# #     if l_company_name_sort[i] == l_company_name_sort[i - 1]:
# #         l_company_name_sort[i] = str(l_company_name_sort[i]) + '1'
# list = []
# l_company = {}
# for i in range(0, len(l_companies)):
#     # print(i)
#     # print(l_companies[i][0])
#     # print(type(l_companies[i]))
#     # print(type(l_companies[i][0]))
# #
# #     list.append(l_companies[i][0])
# # sorted(list)
# # for i in range(0, len(list)):
# #     if list[i] == list[i-1]:
# #         list[i] = str(list[i]) + '1'
# # print(list)
#     sort_company = sorted(l_companies[i])
#     print(sort_company)
#     # if l_companies[i][0] == l_companies[i-1][0]
#     for company in l_companies:  # 提取发行公司中的公司名和公司网址
#         l_company_name = company[0]  # 发行公司名称
#         print(type(l_company_name))    #type = str
#
#
#         l_company_web = company[0]  # 发行公司网址
#         l_company[l_company_name] = l_company_web

#----------------------JSON----------------------
import json
import re
import requests
html = 'http://movie.mtime.com/91881/details.html'
url = requests.get(html)
url_content = url.text

data = re.findall('<div class="fl wp49">.*?</div>', url_content)[0]
company = re.findall('<a href="(.*?)" target="_blank">(.*?)</a>', data)

# res = {}
company_dict = {}
# temp = str
for each in company:
    name = each[1]
    # print(type(name))
    name = name.replace(',', ' ')
    # print(name)
    company_dict[name] = each[0]
# print(zc)
res = {}
res = json.dumps(company_dict)
s = {}
# assert isinstance(res, object)
s = json.loads(res)
print(s)
with open("abc.txt", "a+") as f:
    info = str(s)
    f.write(info)

# res = {}
# zc = {}
# for each in company:
#     name = each[1]
#     # print(type(name))
#     name = name.replace(',', ' ')
#     # print(name)
#     zc[name] = each[0]
#
# res['发行公司'] = zc
# res = json.dumps(res)
# print('type= ', type(res))
# print('res= ',res)
#
# s = json.loads(res)
# print('type= ', type(s))
# print("s= ", s)
# for i in s.keys():
#     print('i = ', i)
#     val = s[i]
#     print('type= ', type(val))
#     print('val= ', val)
# # print(len(company))
# # print(len(zc))
# print(zc)


#---------------------公司列表为空判断------------------------------
# import re
# import requests
# html = 'http://movie.mtime.com/190485/details.html'
# url = requests.get(html)
# url_content = url.text
#
# try:
#     data = re.findall('<div class="fl wp49">.*?</div>', url_content)[1]
#     company = re.findall('<a href="(.*?)" target="_blank">(.*?)</a>', data)
#
#     # res = {}
#     zc = {}
#     for each in company:
#         name = each[1]
#         # print(type(name))
#         name = name.replace(',', ' ')
#         # print(name)
#         zc[name] = each[0]
#     print(zc)
# except IndexError:
#     print('l_company: {NULL}')


#---------------------temp判断是否有重复公司名----------------------------
# from selenium import webdriver
#
# import re
# browser = webdriver.Chrome()
#
# url_film = 'http://movie.mtime.com/91881/details.html'
# browser.get(url_film)  # 访问查找电影网址
# content = browser.execute_script("return document.documentElement.outerHTML")  # 将网页信息赋值给content
# browser.close()
#
# data = re.findall('<div class="fl wp49">.*?</div>', content)[1]
# company = re.findall('<a href="(.*?)" target="_blank">(.*?)</a>', data)
#
# # res = {}
# zc = {}
# temp = str(company[0][1])
# print(temp)
# for each in company:
#     name = each[1]
#     if temp == str(name):
#         temp = name
#         name = str(temp) + '1'
#     # print(type(name))
#     name = name.replace(',', ' ')
#     print(name)
#     zc[name] = each[0]
# print(zc)
# print(len(company))
# print(len(zc))


#-------------------文件夹内写入文件------------------------
# with open("../幕后团队数据规划/2014info/abctest.txt", "a+") as f:
#     f.write("eeeeeeee")
#
# year = 2014
# name = 'abc'
# path = '../幕后团队数据规划/%sinfo' % year
# print(path)
# path1 = path + "/%s" % name
# print(path1)
# with open("%s" % path1, "a+") as f:
#     f.write("eeeeeeee")

