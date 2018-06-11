import fool
import json
import sys
import re

class NerMap:
    def __init__(self):
        self.type_list=['org', 'person', 'location', 'company']
    def handle_article(self, article, create_time, crawling_time, mongo_id):
        article = ''.join(article)
        words, ner = fool.analysis(article)
        # item_msg 就是代表每一条消息(起始位置, 结束位置, 类型, 内容)
        for item_msg in ner[0]:
            if item_msg[2] in self.type_list:
                type_word = list(item_msg)
                if type_word[2] == 'company':
                    type_word[2] = 'org'
                elif type_word[2] == 'location':
                    type_word[2] = 'place'
                ner_data = str(type_word[3])
                r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
                ner_text = re.sub(r, '', ner_data)
                print(type_word[2]+'NER'+ner_text+'\t'+'create_time'+create_time+'&'+crawling_time+'ID:'+mongo_id)

    def start_analysis(self, row):
        mongo_items = row.split("\n")
        for mongo_item in mongo_items:
           if mongo_item:
                mongo_data = json.loads(mongo_item)
                article = mongo_data.get('article')
                create_time = mongo_data.get('create_time')
                crawling_time = mongo_data.get('crawling_time')
                mongo_id = mongo_data.get('_id')[10:-2]
                self.handle_article(article, create_time, crawling_time, mongo_id)

ner = NerMap()
for i in sys.stdin:
    ner.start_analysis(i)
