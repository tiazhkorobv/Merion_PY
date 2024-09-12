# from Lesson_2.address import Address, Mailing
# from Lesson_2.lesson_2_task_3 import send_to, rcvd_fm
import sys
sys.path.append('D:/.For_QA/My_studies/Merion/merion-AQA-PY/My_studies_MRN/Lesson_2')
from address import Address, Mailing
from classes import Order

# new_coast = 73

# ads1 = Address(123456, 'LED', 'Nevskii street', 234, 1)
# ads2 = Address(147825,'MSQ','Ferk str.', 12, 134)
# ads3 = Address(123456, 'ORG', 'Cherk street', 24, 11)
# ads4 = Address(147825,'MSK','Blue squ.', 12, 14)
# ads5 = Address(123456, 'NSB', 'Bunin street', 4, 41)
# ads6 = Address(147825,'VVO','Svetl str.', 12, 14)        
        
        
# mail1 = Mailing(ads1, ads2, new_coast, 'er4585fd')
# mail2 = Mailing(ads3, ads4, new_coast/2, 'yu585fd')
# mail3 = Mailing(ads5, ads6, new_coast-2, 'er466775fd')

# Mails = [mail1, mail2, mail3]

# for mail in Mails:
#     print(f'Отправление {mail.track} из {mail.address_from.city}, {mail.address_from.street},\
#   {mail.address_from.house}-{mail.address_from.apt} в {mail.address_to.city}, {mail.address_to.street},\
#   {mail.address_to.house}-{mail.address_to.apt}. \
#  Стоимость {mail.cost} рублей.')


# numbers_mult = [1, 2, 3, 25, 88]

# for i in numbers_mult:
#     i *= 2
#     print(i)

numbers_1 = [1, 2, 3, 25, 88]
numbers_2 = [1, 2, 3, 4, 5]

# new_list = []
# for i in numbers_1:
#     new_list.append(i * 2)
# print(new_list)

# Использование спискового включения (list comprehension)
numbers_3 = [1, 2, 3, 4, 5]
# new_list2 = [i * 2 for i in numbers_3]
# print(new_list2)
# print(numbers_1 > numbers_2)
    
# Order1 = Order('Mike', ['soap', 'beer','milk', 'bread', 'sleepers'])

# item_list= ''
# for i in Order1.items:
#     item_list = item_list + i + ', '
    
# corr_txt = item_list.rstrip(', ')     
# print(f'Заказ для {Order1.customer_name}: {corr_txt}.')


# list_to_be_sorted = ['apple', 'pine', 'cucumber', 'tomato', 'onion']
# list_to_be_sorted.sort()
# print(list_to_be_sorted) # только так . сразу в принт не грузить!
# list_to_be_sorted.sort(reverse=True)
# print(list_to_be_sorted)

# for i in list_to_be_sorted:
#     print(f'Item: {i}')

# for i in range(1, 11):
#     print(str(i) +':')
#     for j in range (1, 11):
#         k = i * j
#         print(str(i) + ' x '+ str(j) + ' = ' + str(k)) 
#     print('')
    
# numbers_3.reverse()
# print(numbers_3)
lst = []
for i in range (6):
    lst.append(i * i)
print(lst)
    
    