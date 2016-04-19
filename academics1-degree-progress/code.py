from bs4 import BeautifulSoup
import urllib2 

url = raw_input()
url = urllib2.urlopen(url)

content = url.read()

soup = BeautifulSoup(content)

tables = soup.findAll('table')
semester_count = 0
courses_done = {}
invalid_grades = set([u'W', u'F'])
for table in tables:
	rows = table.find_all('tr')
	rows = [row.find_all('td') for row in rows]
	rows = [[e.text.strip() for e in row if e] for row in rows]
	if len(rows) >= 1:
		top_row = rows[0]
		if len(top_row) >= 2 and top_row[1] == u'Course Code':
			semester_count += 1
			for row in rows[1:]:
				course_code = row[1]
				course_type = row[3]
				course_credits = float(row[4])
				course_grade = row[5]
				if course_type not in courses_done:
					courses_done[course_type] = set([])
				if course_grade not in invalid_grades:
					courses_done[course_type].add((course_code, course_credits))

for course_type in courses_done:
	print 'Course Type: ', course_type
	total_credits = 0
	for (course_code, course_credits) in courses_done[course_type]:
		print course_code, course_credits
		total_credits += course_credits
	print 'Total Credits: ', total_credits