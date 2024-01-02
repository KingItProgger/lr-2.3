#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    s=input('enter sentence: ')
    r=s.lower()
    while "c" in r:
        t=r.find('c')
        r=r[:t]+r[t+1:]

    while "с" in r:
        t=r.find('с')
        r=r[:t]+r[t+1:]

    print(r)