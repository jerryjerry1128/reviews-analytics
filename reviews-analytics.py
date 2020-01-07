# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:10:53 2020

@author: Admin
"""


data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000000 == 0:
            print(len(data))
print('檔案讀取完畢，共有', len(data), '筆資料')

sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
print('留言平均長度為',sum_len/len(data))

wc = {}
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] +=1
        else:
            wc[word] =1
            
for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

while True:
    word = input('請問你想查什麼字: ')
    if word == 'q':
        break
    if word not in wc:
        print(word, '沒有出現過')
    else:
        print(word, '出現過', wc[word])
print('謝謝使用本查詢功能')