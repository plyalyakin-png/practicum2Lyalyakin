second = int(input())
print(second // 3600,'часов', (second % 59), 'минут', (second - (second // 3600)*60-(second % 59)*60) % 60, 'секунд' )
