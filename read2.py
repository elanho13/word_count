data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)


#文字計數
wc = {} # word_count
for d in data:
    words = d.split() # split預設值是空字串
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 # 新增新的key進wc字典

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])


while True:
    word = input('請問你想查什麼字:')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為:', wc[word])
    else:
        print('這個字沒出現過!')

print('感謝使用本查詢功能!')

