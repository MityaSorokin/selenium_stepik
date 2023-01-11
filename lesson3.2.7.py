import selenium
from selenium.webdriver.common.by import By
'''
link = 'https://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)

Sample Input 1:

8 11
Sample Output 1:

expected 8, got 11
Sample Input 2:

11 11
Sample Output 2:

Sample Input 3:

11 15
Sample Output 3:

expected 11, got 15
'''
def test_input_text(expected_result, actual_result):
    assert actual_result == expected_result, f"Wrong result, got {actual_result} instead of {expected_result}"
    # ваша реализация, напишите assert и сообщение об ошибке

s = 'as Name'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')
