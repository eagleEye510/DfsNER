from pymongo import MongoClient
import fool
import os
import json
import re


class MapNer(object):
    # def __init__(self):
    #     port = 27017
    #     username = 'zhfr_mongodb_root'
    #     password = 'zkfr_DUBA@0406mgdb#com'
    #     self.conn = MongoClient(host='192.168.1.178', port=port, username=username, password=password)
    @staticmethod
    def fool_ner():
        # data_all = self.conn.portal.web_data.find_one()
        fr = open("E:/untitled1/工具/article.txt", "r", encoding="utf-8")
        # fw = open("./data/ner_out.txt", "a", encoding="utf-8")
        # lines = [line.strip() for line in fr.readlines() if line.strip()]
        for each_data in fr.readlines():
            each_data_json = json.loads(each_data)
            for item in [each_data_json]:
                a = [str(item.get('article'))]
                mongo_id = item.get('_id')[10:-2]
                create_time = item.get('create_time')
                crawling_time = item.get('crawling_time')

                # 字符串分片截取操作

                MapNer.analysis(a, create_time, crawling_time, mongo_id)

    @staticmethod
    def analysis(article,create_time,crawling_time ,mongo_id ):
        '''
        :param article:  文章 ["本报讯.. ', ""],
        :return:
        '''
        # a append追加文件 w:写入文件 r:读文件
        fw = open("./data/ner_out.txt", "a", encoding="utf-8")
        for a in article:
            each_article = a.replace("\n", "")
            if len(article) != 0:
                words, ner = fool.analysis(each_article)
                for i in ner:
                    if i[2] == 'org' or i[2] == 'company' or i[2] == 'person' or i[2] == 'location':
                        i = list(i)
                        if i[2] == 'company':
                            i[2] = 'org'
                        elif i[2] == 'location':
                            i[2] = 'place'
                       # str(i[2])
                        ner_text=str(i[3])
                        r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
                        ner_text = re.sub(r, '', ner_text)
                        fw.write(str(i[2])+'NER'+ner_text+'\t'+'create_time'+create_time+'&'+crawling_time+'ID:'+mongo_id+'\n')
        fw.close()


if __name__ == '__main__':
    map_ner = MapNer()
    map_ner.fool_ner()
