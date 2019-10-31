# -*- coding:utf-8 -*-

from selenium import webdriver
import csv

driver = webdriver.Chrome()
driver.get("https://feebee.com.tw/")

element = driver.find_element_by_name("q")
element.send_keys("電風扇")
element.submit()

for i in range(50):
	fobj = open('output.csv','a+')
	writer = csv.writer(fobj)
	elem = driver.find_elements_by_xpath('//*[@id="list_view"]/li')
	for i in elem:
		rawList = i.text.split('\n')
		if len(rawList) <= 8:
			writer.writerow([rawList[0],rawList[1],rawList[3]])
		else:
			locationList = []
			priceList = []
			for i in range(4,len(rawList),2):
				locationList.append(rawList[i])
			for j in range(5,len(rawList),2):
				priceList.append(rawList[j])
			nameList = [rawList[0]]*len(locationList)
			for i,j,k in zip(nameList,priceList,locationList):
				writer.writerow([i,j,k])
		print(rawList)
	driver.find_element_by_xpath('//*[@id="search_result_container"]/div[3]/div/ol/li/a[@title="下一頁"]').click()

driver.quit()
