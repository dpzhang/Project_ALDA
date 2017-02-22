### Project Alda
### Course Crawler
### Ningyin Xu Feb. 22nd

###############################################################################
	
	# To run this, you need to install selenium package, and its phantom driver.
	# Reference Webpage:
	# http://stackoverflow.com/questions/13287490/is-there-a-way-to-use-phantomjs-in-python

###############################################################################



# import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import json
import csv
import pandas as pd


def setup_driver(course_url):
	dothething = True
	while dothething:
		try:
			driver = webdriver.PhantomJS()
			driver.implicitly_wait(10)
			driver.set_window_size(1024,768)
			driver.get(course_url)
			quarter_select = Select(driver.find_element_by_id('UC_CLSRCH_WRK2_STRM'))
			if quarter_select.first_selected_option.text != 'Spring 2017':
				quarter_select.select_by_value('2174')
			driver.save_screenshot('screen.png')
			driver.implicitly_wait(20)
			print('driver ready')
			return driver
			break
		except StaleElementReferenceException:
			driver.quit()
			continue
		except NoSuchElementException:
			driver.quit()
			continue


def find_dept_ls(course_url):
	driver = setup_driver(course_url)

	dept_btn_id = 'UC_CLSRCH_WRK2_SUBJECT'
	dept_btn = driver.find_element_by_id(dept_btn_id)
	dept_select = Select(dept_btn)
	depts = dept_select.options
	dept_ls = []
	for i in depts[1:]:
		dept_ls.append(i.get_attribute('value'))
	driver.quit()
	return dept_ls


def one_page_crawler(results_one_page, driver, courses_dict):
	for i in range(results_one_page):
		coursechunk = 'DESCR100$0_row_' + str(i)
		test = driver.find_element_by_id('win0divUC_SR0047_WRK_GROUPBOX18$0')
		driver.find_element_by_id(coursechunk).click()

		wait = WebDriverWait(driver, 10)
		wait.until(EC.visibility_of(test))

		driver.save_screenshot('screen2.png')

		coursekey = driver.find_element_by_id('win0divUC_CLS_DTL_WRK_HTMLAREA$0')
		coursekey = coursekey.text.split()
		coursename = driver.find_element_by_id('UC_CLS_DTL_WRK_UC_CLASS_TITLE$0')
		coursename = coursename.text
		coursedscp = driver.find_element_by_id('UC_CLS_DTL_WRK_DESCRLONG$0')
		coursedscp = coursedscp.text
		instructors = driver.find_element_by_id('MTG$0').text
		daytime = driver.find_element_by_id('MTG_SCHED$0').text
		loc = driver.find_element_by_id('MTG_LOC$0').text
		career = driver.find_element_by_id('PSXLATITEM_XLATLONGNAME$33$$0').text
		
		courseid = coursekey[0] + coursekey[1][:-2]
		section = coursekey[1][-1]
		sectionid = coursekey[2]
		coursetype = coursekey[4]
		courses_dict[courseid] = dict()
		courses_dict[courseid]['name'] = coursename
		courses_dict[courseid]['section'] = section
		courses_dict[courseid]['sectionid'] = sectionid
		courses_dict[courseid]['type'] = coursetype
		courses_dict[courseid]['instructor'] = instructors
		courses_dict[courseid]['location'] = loc
		courses_dict[courseid]['daytime'] = daytime
		courses_dict[courseid]['career'] = career
		courses_dict[courseid]['description'] = coursedscp

		sub = driver.find_element_by_id('win0divUC_CLS_REL_WRK_RELATE_CLASS_NBR_1$373$$0').text
		if len(sub) != 0:
			courses_dict[courseid]['subsections'] = list()
			subcounts = len(driver.find_elements_by_id("win0divSSR_CLS_TBL_R11$grid$0"))
			for i in range(subcounts):
				courses_dict[courseid]['subsections'].append(dict())
				subkey = driver.find_element_by_id('win0divDISC_HTM$' + str(i)).text
				subinstructor = driver.find_element_by_id('win0divDISC_INSTR$' + str(i)).text
				subtime = driver.find_element_by_id('DISC_SCHED$' + str(i)).text
				courses_dict[courseid]['subsections'][i]['sectionname'] = subkey
				courses_dict[courseid]['subsections'][i]['sectionname'] = subkey
				courses_dict[courseid]['subsections'][i]['sectionname'] = subkey
		else:
			courses_dict[courseid]['subsections'] = []

		returnid = 'UC_CLS_DTL_WRK_RETURN_PB$0'
		test = driver.find_element_by_id(returnid)
		driver.find_element_by_id(returnid).click()

		wait = WebDriverWait(driver, 10)
		wait.until(EC.staleness_of(test))

	return courses_dict


def one_dept_crawler(dept, courses_dict, course_url):

	driver = setup_driver(course_url)

	dept_btn = driver.find_element_by_id('UC_CLSRCH_WRK2_SUBJECT')
	Select(dept_btn).select_by_value(dept)
	driver.implicitly_wait(10)

	searchbutton = driver.find_element_by_id('UC_CLSRCH_WRK2_SEARCH_BTN')
	searchbutton.click()

	# test = driver.find_element_by_id('UC_CLSRCH_WRK2_SEARCH_BTN')
	wait = WebDriverWait(driver, 10)
	# wait.until(EC.staleness_of(test))
	wait.until(EC.staleness_of(searchbutton))
	driver.save_screenshot('screen1.png')

	resultsize = driver.find_element_by_id('UC_RSLT_NAV_WRK_PTPG_ROWS_GRID').text.split()[0]
	resultsize = int(resultsize)
	pages = 1

	if resultsize == 250:
		print("something's wrong, crawl this dept from beginning")
		driver.quit()
		courses_dict = one_dept_crawler(dept, courses_dict, course_url)
		return courses_dict

	if resultsize > 25:
		pages = resultsize // 25 + 1

	while pages > 1:
		print('this is dept: ' + dept + ' page (reversely) ' + str(pages))
		results_one_page = 25
		pagedown = driver.find_element_by_id('UC_RSLT_NAV_WRK_SEARCH_CONDITION2$46$')
		courses_dict = one_page_crawler(results_one_page, driver, courses_dict)
		pagedown.click()

		wait = WebDriverWait(driver, 10)
		wait.until(EC.staleness_of(pagedown))
		driver.save_screenshot('screen3.png')
		print('page ' + str(pages) + ' (reversely) finished')
		pages = pages - 1


	if pages == 1:
		print('this is dept: ' + dept + ', it only has one page or this is its last page')
		results_one_page = resultsize % 25
		courses_dict = one_page_crawler(results_one_page, driver, courses_dict)
		driver.save_screenshot('screen3.png')
		print('this page finished')
	
	driver.quit()
	return courses_dict


def course_crawler(dept_ls, courses_dict, course_url):
	for dept in dept_ls:
		print('this is dept: ' + dept)
		dothething = True
		while dothething:
			try:
				courses_dict = one_dept_crawler(dept, courses_dict, course_url)
				break
			except StaleElementReferenceException:
				return (courses_dict, dept)
			except NoSuchElementException:
				return (courses_dict, dept)

		print(dept + 'finished')

	return (courses_dict, '')


if __name__ == "__main__":
	course_url = 'https://coursesearch.uchicago.edu/psc/prdguest/EMPLOYEE/HRMS/c/UC_STUDENT_RECORDS_FL.UC_CLASS_SEARCH_FL.GBL'
	courses_dict = dict()

	dept_ls = find_dept_ls(course_url)
	print('There are {:} departments in total.'.format(len(dept_ls)))
	
	# dept_ls = dept_ls[:1]
	dept_ls = dept_ls[:5]

	courses_dict, dept = course_crawler(dept_ls, courses_dict, course_url)	
	# print(courses_dict)
	print(dept)

	with open('course_output.json', 'w') as f:
		json.dump(courses_dict, f, ensure_ascii = False)

	coursedf = pd.DataFrame.from_dict(courses_dict, orient = 'index')

	coursedf.to_csv('course_output.csv', sep = '|')

	


	
	



	
