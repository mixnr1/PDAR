import time
from selenium import webdriver
browser=webdriver.Chrome()
browser.get('http://www.dvi.gov.lv/pub/pub.php?f=pd#')
with open('Personas_datu_apstrades_registrs.txt', mode='w', encoding='utf-8') as teksts:
    for i in range(1, 153):
        browser.get('http://www.dvi.gov.lv/pub/pub.php?f=pd#')
        time.sleep(2)
        if i != 1:
            browser.find_element_by_link_text(str(i)).click()
        time.sleep(2)
        rows=browser.find_element_by_id('rectable').find_elements_by_tag_name('tr')
        registrs=[]
        for row in range(0, len(rows)):
            merk=rows[row].find_elements_by_tag_name('td')[0].get_attribute('title')
            parzin= rows[row].find_elements_by_tag_name('td')[0].text
            kopa=f'Pārzinis:{parzin}|'+merk.replace('\n', '')
            registrs.append(kopa)
            print(kopa)
        for m in range(0, len(registrs)):
            teksts.write(f'{registrs[m]}\n')
browser.close()