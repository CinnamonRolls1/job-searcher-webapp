import scrapy
import re

# running: scrapy crawl indeed -o indeed_data.csv

class IndeedSpider(scrapy.Spider):
	name = 'indeed'	
	
	start_urls = [
		'https://www.indeed.co.in/jobs-in-Bangalore,-Karnataka'
	]
	
	# def start_requests(self):
		
		# for url in start_urls:

		# 	next_page = response.xpath("//span[@class='np']/../../@href").extract_first()
		# 	if next_page is not None:
		# 		next_page_link = response.urljoin(next_page)
		# 		yield scrapy.Request(url=next_page_link, callback=self.parse)
				

	def parse(self, response):
		for job in response.xpath("//div[contains(@class,'jobsearch-SerpJobCard') and contains(@class,'unifiedRow')]"):
			
			##### COMPANY NAME
			company=job.xpath("normalize-space(.//span[@class='company']/text())") 
			# print("company:", company.extract_first())
			if company.extract_first() == '':
				company=job.xpath("normalize-space(.//a[@class='turnstileLink']/text())")

			##### SALARY
			salary_data=job.xpath("normalize-space(.//span[contains(@class, 'salary')])")
			salary=salary_data.re(r'[₹][A-Za-z0-9,]+')
			if salary:
				if len(salary)==2:
					low_sal=float(re.sub('[,₹]','',salary[0]))
					high_sal=float(re.sub('[,₹]','',salary[1]))
					salary=(low_sal+high_sal)/2
					# print("Salary averaged!")
				else:
					salary=salary[0]
					salary=int(re.sub('[,₹]','',salary))
				# print(salary)
				if salary_data.re(r'[mM][oO][nN][tT][hH]'):
					# print("\nMonthly salary detected!")
					salary=12*salary


			yield {
				'TITLE' : job.xpath("normalize-space(.//div[@class='title']/a/text())").extract_first(),
				'COMPANY' : company.extract_first(),
				'LOCATION' : job.xpath("normalize-space(.//div[contains(@class,'location')])").extract_first(),
				'SALARY' : salary,
				# 'AGE OF POSTING' : job.xpath("normalize-space(.//span[@class='date '])").extract_first()
			}

		next_page = response.xpath("//div[@class='pagination']/a[position()=last()]/@href").extract_first()
		if next_page is not None:
			next_page_link = response.urljoin(next_page)
			yield scrapy.Request(url=next_page_link, callback=self.parse)

# running: scrapy crawl tj -o tj_data.csv

class TJSpider(scrapy.Spider):
	name = 'tj'	
	
	start_urls = [
		'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=&txtLocation=Bengaluru%2F+Bangalore'
	]				




	def parse(self, response):
		for job in response.xpath("//ul/li[contains(@class,'clearfix')]"):
			
			##### SALARY
			salary_data=job.xpath("normalize-space(.//i[contains(@class,'rupee')]/../text())")
			salary=salary_data.re(r'[0-9]*[.]*[0-9]+')
			if salary:
				if len(salary)==2:
					#low_sal=float(re.sub('[,₹]','',salary[0]))
					#high_sal=float(re.sub('[,₹]','',salary[1]))
					low_sal=float(salary[0])*100000
					high_sal=float(salary[1])*100000
					salary=(low_sal+high_sal)/2
					# print("Salary averaged!")
				else:
					salary=salary[0]
					salary=float(salary)*100000
				# print(salary)

			yield {
				'TITLE' : job.xpath("normalize-space(.//header[contains(@class,'clearfix')]/h2/a/text())").extract_first(),
				'COMPANY' : job.xpath("normalize-space(.//header[contains(@class,'clearfix')]/h3/text())").extract_first(),
				'LOCATION' : job.xpath("normalize-space(.//ul[contains(@class,'top-jd-dtl')]/li[position()=last()]/span/text())").extract_first(),
				'SALARY' : salary,
				# 'AGE OF POSTING' : job.xpath("normalize-space(.//span[@class='date '])").extract_first()
			}

		# next_page = response.xpath("//a[@rel='next']/@href").extract_first()
		# if next_page is not None:
		# 	next_page_link = response.urljoin(next_page)
		# 	yield scrapy.Request(url=next_page_link, callback=self.parse)
	

		
	