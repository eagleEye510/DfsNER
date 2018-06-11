import fool
import os

if os.path.exists('./data/') == True:
    fw = open("./data/ner_out.txt", "w", encoding="utf-8")
else:
    os.mkdir(r"./data/")
    fw = open("./data/ner_out.txt", "w", encoding="utf-8")

fr = open("./data/ner_test.txt", "r", encoding="utf-8")
# lines = [line.strip() for line in fr.readlines() if line.strip()]

lines = []
for line in fr.readlines():

    if line.strip():
        lines.append(line.strip())
# print(lines)

for words in lines:

    if len(words) != 0:
        words, ner = fool.analysis(words)

        for i in ner:

            try:
                if i[2] == 'org'or i[2] == 'company'or i[2] == 'person'or i[2] == 'location':
                    fw.write(str(i[2:4]) + '\n')
            except:
                print(i)


    else:
        break
fr.close()




