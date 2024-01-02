#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    word1=input('enter 1st word: ')
    word2 = input('enter 2nd word: ')
    for i in word1:
        if i in word2:
            print('yes')
        else:
            print('no')
