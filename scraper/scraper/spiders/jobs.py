import scrapy
import re
import unidecode

# running: scrapy crawl indeed -o indeed_data.json

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

			##### DESCRIPTION
			desc_data=job.xpath(".//div[contains(@class,'summary')]/ul/li")
			# print("----------------------")
			# print(desc_data)
			# print(len(desc_data))
			desc=""
			for point in desc_data:
				desc+=(" "+point.xpath("normalize-space(.//text())").extract_first())
			# print(desc)


			##### LINK
			link_data=job.xpath("//a[contains(@class,'jobtitle') and contains(@class,'turnstileLink')]/@href").extract_first()
			link=re.sub(r'(https:\/\/www\.indeed\.co\.in)','',link_data)
			link='https://www.indeed.co.in'+link
			


			yield {
				'TITLE' : job.xpath("normalize-space(.//div[@class='title']/a/text())").extract_first(),
				'COMPANY' : company.extract_first(),
				'LOCATION' : job.xpath("normalize-space(.//div[contains(@class,'location')])").extract_first(),
				'SALARY' : salary,
				'DESCRIPTION' : unidecode.unidecode('u'+desc),
				'LINK' : link,

			}

		next_page = response.xpath("//div[@class='pagination']/a[position()=last()]/@href").extract_first()
		if next_page is not None:
			next_page_link = response.urljoin(next_page)
			yield scrapy.Request(url=next_page_link, callback=self.parse)

# running: scrapy crawl tj -o tj_data.json

class TJSpider(scrapy.Spider):
	name = 'tj'	
	
	start_urls = [
		'https://www.timesjobs.com/candidate/job-search.html?from=submit&searchType=personalizedSearch&txtLocation=Bengaluru/%20Bangalore&luceneResultSize=25&postWeek=60&pDate=Y&sequence=1&startPage=1'
	]				




	def parse(self, response):
		if response.xpath("//div[contains(@class,'no-jobs-found')]"):
			print('End of pagination!')
		else:
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

				##### DESCRIPTION
				desc=re.sub('(Job Description:)|(More Details)', '', job.xpath("normalize-space(.//ul[contains(@class,'list-job-dtl')]/li)").extract_first())
				
				yield {
					'TITLE' : job.xpath("normalize-space(.//header[contains(@class,'clearfix')]/h2/a/text())").extract_first(),
					'COMPANY' : job.xpath("normalize-space(.//header[contains(@class,'clearfix')]/h3/text())").extract_first(),
					'LOCATION' : job.xpath("normalize-space(.//ul[contains(@class,'top-jd-dtl')]/li[position()=last()]/span/text())").extract_first(),
					'SALARY' : salary,
					'DESCRIPTION': unidecode.unidecode('u'+desc),
					'LINK': job.xpath(".//header[contains(@class,'clearfix')]/h2/a/@href").extract_first()
					# 'AGE OF POSTING' : job.xpath("normalize-space(.//span[@class='date '])").extract_first()
				}
				

				# extracting the page number from url, incrementing it and injecting it back into the next url
			current_url=response.request.url
			matches = re.finditer(r"(?<=sequence=).[0-9]*", current_url)
			matches=list(enumerate(matches))
			pgno=int(matches[0][1].group())
			pgno+=1
			next_url=re.sub('(?<=sequence=).[0-9]*',str(pgno),current_url)
			print("---------------------------------------------------------ENTERING PAGE", pgno)
			next_page_link = response.urljoin(next_url)
			yield scrapy.Request(url=next_page_link, callback=self.parse)






	

		
	