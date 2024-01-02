#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    word1=(input('enter word1: '))
    word2 = (input('enter word2: '))
    if word1==word2:
        print('The same words!')
    else:
        if len(word1)<len(word2):
            minimal=len(word1)
        else:
            minimal=len(word2)
        count=0
        for i in range(minimal):
            if word1[i]==word2[i]:
                count+=1
            else: break
        if count==0:
            print('no same start symbols')
        else:
            print(f"{count} same start symbols")

