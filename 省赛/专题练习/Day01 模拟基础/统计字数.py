
def main():
    sentenceChar()
    sentenceWord()
    printWord()
"""
输出句子里的字符和
"""
def sentenceChar():
    s = input()
    total = len(s.replace(" ", ""))
    print(total)

"""
输出句子里的单词数
"""
def sentenceWord():
    s=input()
    word=s.split()
    print(len(word))

"""
逐个输出每个单词和它的字符长度
"""
def printWord():
    word=input().split()
    for i in word:
        print(i,len(i))

if __name__ =='__main__':
    main()