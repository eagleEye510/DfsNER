import sys


# print('Please enter your name:')
# name = sys.stdin.readline()[:-1]
# print('Hi, %s!' % name)
# print('Please enter your map ner result:')


class RedNer(object):
    @staticmethod
    def print_key_and_mongodb(key, mongodb):
        if key == '':
            return
        # python print()函数默认换行 print(*objects, sep=' ', end='\n', file=sys.stdout)
        # objects -- 复数，表示可以一次输出多个对象。输出多个对象时，需要用 , 分隔。
        # sep -- 用来间隔多个对象，默认值是一个空格。
        # end -- 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符串。
        # file -- 要写入的文件对象。
        print(key, end='')
        for mongodb_val in mongodb:
            print('\t' + mongodb_val[:-1] + 'end', end='')
        print('LXQ')

    # @staticmethod
    def reduce_map(self):
        sentence = ''
        pre_key = ''
        mongodb = []
        fr = open("./data/ner_out.txt", "r", encoding="utf-8")
        for sentence in fr.readlines():
            array_words = sentence.split('\t')
            if array_words[0] != pre_key:
                RedNer().print_key_and_mongodb(pre_key, mongodb)
                pre_key = array_words[0]
                mongodb.clear()
                mongodb.append(array_words[1])
            else:
                if array_words[1] not in mongodb:
                    mongodb.append(array_words[1])
        # RedNer.print_key_and_mongodb(pre_key, mongodb)
        fr.close()


reduce_text = RedNer()
reduce_text.reduce_map()
# 下面两个写法是一样的
# RedNer.reduce_map(reduce_text)
# reduce_text.reduce_map()

# 不用selfl
# RedNer.reduce_map()
# fr = open("./data/ner_out.txt", "r", encoding="utf-8")
# fw = open('./data/1.txt', 'w', encoding="utf-8")
# pre_sentence = ''
# pre_words = ''
# pre_mongodb = ''
# for sentence in fr.readlines():
#     array_words = sentence.split('\t')
#     if pre_sentence != sentence:
#
#         print(sentence[:-1]+'end')
#         pre_sentence = sentence
#         pre_words = array_words[0]
#         pre_mongodb = array_words[1]


# sentence = ''
# while sentence == sys.stdin.readline():
#     array_words = sentence.split('\t')
#     print(sentence)
# fr = open("./data/ner_out.txt", "r", encoding="utf-8")
# pre_words = ''
# pre_mongodb = ''
# for sentence in fr.readlines():
#     array_words = sentence.split('\t')
#     if array_words[0] != pre_words or array_words[0] == pre_words and array_words[1] == pre_mongodb:
#         print(sentence)
#         pre_words = array_words[0]
#     elif array_words[0] == pre_words and array_words[1] != pre_mongodb:
#         print(sentence+'\t'+array_words[1])
#
#         pre_mongodb = array_words[1]


# ner = RedNer()
