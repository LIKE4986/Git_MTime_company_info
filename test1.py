# print('-------------version1.0 || 20180602--------------')
# from selenium import webdriver
# import re
# import requests
#
#
# def __film_data():
#     # 获取每个电影专门的编号，并进入网站
#     browser = webdriver.Chrome()
#     get_name = film_name  # 从文件夹获取电影名赋值给get_name
#     url_film = 'http://search.mtime.com/search/?q=%s' % get_name
#     browser.get(url_film)  # 访问查找电影网址
#     content = browser.execute_script("return document.documentElement.outerHTML")  # 将网页信息赋值给content
#     browser.close()
#
#     # 根据固定编号进入more details界面
#     get_number = '.*target="_blank" href="(.*?)"><img alt="%s.' % get_name  # 通过电影名获取电影编号
#     film_numberweb = re.findall(get_number, content)  # 通过正则匹配获取含电影编号的网址
#     url_details = str(film_numberweb[0]) + 'details.html'  # 电影更多资料网址
#     return url_details
#
#
# def __film_companies(url_details, get_year):
#     # 获取制作/发行公司信息
#     url_moredetails = requests.get(url_details)
#     url_moredetails = url_moredetails.text
#
#     # 获取制作公司信息（p_company)
#     p_companies_html = re.findall('<div class="fl wp49">.*?</div>', url_moredetails)[0]  # 正则匹配获取制作公司的部分html
#     p_companies = re.findall('<a href="(.*?)" target="_blank">(.*?)</a>', p_companies_html)  # 正则匹配获取所有制作公司
#
#     p_company = {}  # 定义制作公司字典
#     for company in p_companies:  # 提取制作公司中的公司名和公司网址
#         p_company_name = company[1]  # 制作公司名称
#         p_company_web = company[0]  # 制作公司网址
#         # 判断是否有相同的公司名，如果有，在第二个名称后面加“1”
#         p_company[p_company_name] = p_company_web
#
#     print('制作公司：', p_company)
#
#     # 判断制作公司信息是否为空并写入文件
#     if len(p_companies) == 0:
#         with open('%sinfo.txt' % film_year, 'a+') as file:
#             p_companise_txt = '制作公司：{NULL}\n'  # 制作公司信息的文本信息
#             file.write(p_companise_txt)
#     else:
#         with open('%sinfo.txt' % film_year, 'a+') as file:
#             p_companise_txt = '制作公司：' + str(p_company) + '\n'  # 制作公司信息的文本信息
#             file.write(p_companise_txt)
#
#     # 获取发行公司信息（l_company)
#     l_companies_html = re.findall('<div class="fl wp49">.*?</div>', url_moredetails)[0]  # 正则匹配获取发行公司的部分html
#     l_companies = re.findall('<a href="(.*?)" target="_blank">(.*?)</a>', l_companies_html)  # 正则匹配获取所有发行公司
#
#     l_company = {}
#     for company in l_companies:  # 提取发行公司中的公司名和公司网址
#         l_company_name = company[1]  # 发行公司名称
#         l_company_web = company[0]  # 发行公司网址
#
#         # 判断是否有相同的公司名，如果有，在第二个名称后面加“1”
#
#         # 判断发行公司信息是否为空并写入文件
#         if len(l_companies) == 0:
#             with open('%sinfo.txt' % film_year, 'a+') as file:
#                 l_companise_txt = '发行公司：{NULL}\n'  # 发行公司信息的文本信息
#                 file.write(l_companise_txt)
#         else:
#             with open('%sinfo.txt' % film_year, 'a+') as file:
#                 l_companise_txt = '发行公司：' + str(l_company) + '\n'  # 发行公司信息的文本信息
#                 file.write(l_companise_txt)
#
#
# if __name__ == '__main__':
#     for film_year in range(2014, 2016):
#         # print(type(t))
#         with open('%s.txt' % film_year) as file1:
#             # 打开文件并按行读取
#             for line in file1:
#                 name_and_number = line.split('')
#                 film_name = name_and_number[0]
#                 film_id = name_and_number[1]
#                 with open('%sinfo.txt' % film_year, 'a+') as file2:
#                     _id = '_id：' + str(film_id)
#                     year = 'year：' + str(film_year) + '\n'
#                     movie_name = 'movie_name：' + str(film_name)
#                     info = _id + year + movie_name
#                     file2.write(info)
#                 print(_id, year, movie_name)
#                 try:
#                     __film_companies(url_details = __film_data(), get_year = film_year)
#                 except:
#                     pass
#



# print('-------------version2.1 || 20180603--------------')
# #新增获取公司函数（__get_company）,写入文件函数（__write_company和__write_filminfo）将重复的内容模块化
# from selenium import webdriver
# import re
# import requests
#
#
# def __film_data():
#     # 获取每个电影专门的编号，并进入网站
#     browser = webdriver.Chrome()
#     get_name = film_name  # 从文件夹获取电影名赋值给get_name
#     url_film = 'http://search.mtime.com/search/?q=%s' % get_name
#     browser.get(url_film)  # 访问查找电影网址
#     content = browser.execute_script("return document.documentElement.outerHTML")  # 将网页信息赋值给content
#     browser.close()
#
#     # 根据固定编号进入more details界面
#     get_number = '.*target="_blank" href="(.*?)"><img alt="%s.' % get_name  # 通过电影名获取电影编号
#     film_numberweb = re.findall(get_number, content)  # 通过正则匹配获取含电影编号的网址
#     url_details = str(film_numberweb[0]) + 'details.html'  # 电影更多资料网址
#     return url_details
#
#
# def __get_company(url_details, number):
#     # 获公司信息
#     url_moredetails = requests.get(url_details)
#     url_moredetails = url_moredetails.text
#
#
#     html = re.findall('<div class="fl wp49">.*?</div>', url_moredetails)[number]  # 正则匹配获取制作公司的部分html
#     companies = re.findall('<a href="(.*?)" target="_blank">(.*?)</a>', html)  # 正则匹配获取所有制作/发行公司
#     res = {}
#     company_dict = {}
#     for each in companies:
#         name = each[1]
#         # print(type(name))
#         name = name.replace(',', ' ')
#         # print(name)
#         company_dict[name] = each[0]
#     # print(zc)
#     return company_dict
#
#
# def __write_company(companyclass, num):
#     #将公司信息写入文件
#     try:
#         company = __get_company(url_details=__film_data(), number = num)
#         with open('%sinfo.txt' % film_year, 'a+') as file2:
#             info = '%s：' % companyclass + str(company) + '\n'
#             file2.write(info)
#     except IndexError:
#         with open('%sinfo.txt' % film_year, 'a+') as file2:
#             info = '%s：{NULL}\n' % companyclass
#             file2.write(info)
#
# def __write_filminfo():
#     #将电影id、年份、名字写入文件
#     with open('%sinfo.txt' % film_year, 'a+') as file2:
#         _id = '_id：' + str(film_id)
#         year = 'year：' + str(film_year) + '\n'
#         movie_name = 'movie_name：' + str(film_name) + '\n'
#         info = _id + year + movie_name
#         file2.write(info)
#     print(_id, year, movie_name)
#
# if __name__ == '__main__':
#     for film_year in range(2014, 2016):
#         # print(type(t))
#         with open('%s.txt' % film_year) as file1:
#             # 打开文件并按行读取
#             for line in file1:
#                 name_and_number = line.split('')
#                 film_name = name_and_number[0]
#                 film_id = name_and_number[1]
#                 __write_filminfo()      #调用__电影信息写入文件函数
#                 try:
#                     __write_company(companyclass= 'p_company', num= 0)
#                     __write_company(companyclass= 'l_company', num= 1)
#                 except:
#                     pass

print('-------------version2.2 || 20180604--------------')
#修改写入文件部分，将按年份写入文件改为按电影名写入文件
from selenium import webdriver
import re
import requests


def __film_data():
    # 获取每个电影专门的编号，并进入网站
    browser = webdriver.Chrome()
    get_name = film_name  # 从文件夹获取电影名赋值给get_name
    url_film = 'http://search.mtime.com/search/?q=%s' % get_name
    browser.get(url_film)  # 访问查找电影网址
    content = browser.execute_script("return document.documentElement.outerHTML")  # 将网页信息赋值给content
    browser.close()

    # 根据固定编号进入more details界面
    get_number = '.*target="_blank" href="(.*?)"><img alt="%s.' % get_name  # 通过电影名获取电影编号
    film_numberweb = re.findall(get_number, content)  # 通过正则匹配获取含电影编号的网址
    url_details = str(film_numberweb[0]) + 'details.html'  # 电影更多资料网址
    return url_details


def __get_company(url_details, number):
    # 获公司信息
    url_moredetails = requests.get(url_details)
    url_moredetails = url_moredetails.text


    html = re.findall('<div class="fl wp49">.*?</div>', url_moredetails)[number]  # 正则匹配获取制作公司的部分html
    companies = re.findall('<a href="(.*?)" target="_blank">(.*?)</a>', html)  # 正则匹配获取所有制作/发行公司
    res = {}
    company_dict = {}
    temp = str
    for each in companies:
        name = each[1]
        # print(type(name))
        name = name.replace(',', ' ')
        # print(name)
        company_dict[name] = each[0]
    # print(zc)
    return company_dict


def __write_company(companyclass, num):
    #将公司信息写入文件
    path = '../幕后团队数据规划/%sinfo' % film_year
    path1 = path + "/%s" % film_name
    try:
        company = __get_company(url_details=__film_data(), number = num)
        with open("%s" % path1, "a+") as file2:
            info = '%s：' % companyclass + str(company) + '\n'
            file2.write(info)
    except IndexError:
        with open("%s" % path1, "a+") as file2:
            info = '%s：{NULL}\n' % companyclass
            file2.write(info)

def __write_filminfo():
    #将电影id、年份、名字写入文件
    path = '../幕后团队数据规划/%sinfo' % film_year
    path1 = path + "/%s" % film_name
    with open("%s" % path1, "a+") as file2:
        _id = '_id：' + str(film_id)
        year = 'year：' + str(film_year) + '\n'
        movie_name = 'movie_name：' + str(film_name) + '\n'
        info = _id + year + movie_name
        file2.write(info)
    print(_id, year, movie_name)

if __name__ == '__main__':
    for film_year in range(2014, 2016):
        # print(type(t))
        with open('%s.txt' % film_year) as file1:
            # 打开文件并按行读取
            for line in file1:
                name_and_number = line.split('')
                film_name = name_and_number[0]
                film_id = name_and_number[1]
                __write_filminfo()      #调用__电影信息写入文件函数
                try:
                    __write_company(companyclass= 'p_company', num= 0)
                    __write_company(companyclass= 'l_company', num= 1)
                except:
                    pass
