# coding=utf8
"""

"""
from selenium import webdriver
import re
import requests
from pymongo import MongoClient

conn = MongoClient('192.168.235.55', 27017) #连接mongodb
db = conn['admin']  #连接数据库名
db.authenticate("admin", "123456")    #密码
db = conn['team_behind_sc'] #use team_behind_sc(数据库)
my_set = db['Film_company'] #连接要导入的表

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
    # res = {}
    company_dict = {}
    # temp = str
    for each in companies:
        name = each[1]
        # print(type(name))
        name = name.replace(',', ' ')
        # print(name)
        company_dict[name] = each[0]
    # print(zc)
    return company_dict

def __insert_company(companyclass, num):
    # __get_company(url_details= __film_data(), number= num)
    try:
        res = __get_company(url_details= __film_data(), number= num)
        print("%s" % companyclass, res)
        return res
    except:
        print("sth wrong while finding %s" % companyclass)
        pass

# def __company(res_p, res_l):
#     try:
#         res_p = __get_company(url_details=__film_data(), number=0)
#         print("p_company", res_p)
#     except:
#         print("wrong in finding p_company")
#     try:
#         res_l = __get_company(url_details=__film_data(), number=1)
#         print("l_company", res_l)
#     except:
#         print("wrong in finding l_company")

def __insert_info():
    # res1 = {}
    # res2 = {}
    res_p = __insert_company(companyclass= "p_company", num= 0)
    res_l = __insert_company(companyclass= "l_company", num= 1)
    # info = [{'_
    # id:': film_id}, {'year:': film_year}, {'movie_name:': film_name}, res_p, res_l]
    # print(info)
    # my_set = db.company_set
    my_set.insert({
        "_id": film_id,
         "year": film_year,
         "movie_name": film_name,
         "p_company": res_p,
         "l_campany": res_l
        })
    # test = my_set.find
    # for i in test:
    #     print(i)


if __name__ == '__main__':
    for film_year in range(2014, 2016):
        # print(type(t))
        with open('%s.txt' % film_year) as file1:
            # 打开文件并按行读取
            for line in file1:
                name_and_number = line.split('')
                film_name = name_and_number[0]
                film_id = name_and_number[1]
                print(film_name)
                # __write_filminfo()      #调用__电影信息写入文件函数
                try:
                    __insert_info()
                    # __write_company(companyclass= 'p_company', num= 0)
                    # __write_company(companyclass= 'l_company', num= 1)
                except:
                    pass
