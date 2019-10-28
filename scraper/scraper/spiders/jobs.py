import scrapy

# running: scrapy crawl jobs -o data.csv

class JobsSpider(scrapy.Spider):
	name = 'jobs'	
	
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
			
			company=job.xpath("normalize-space(.//span[@class='company']/text())") 
			# print("company:", company.extract_first())
			if company.extract_first() == '':
				company=job.xpath("normalize-space(.//a[@class='turnstileLink']/text())")

			yield {
				'TITLE' : job.xpath("normalize-space(.//div[@class='title']/a/text())").extract_first(),
				'COMPANY' : company.extract_first(),
				'LOCATION' : job.xpath("normalize-space(.//div[contains(@class,'location')])").extract_first(),
				'SALARY' : job.xpath("normalize-space(.//span[contains(@class, 'salary')])").extract_first(),
				# 'AGE OF POSTING' : job.xpath("normalize-space(.//span[@class='date '])").extract_first()
			}

		next_page = response.xpath("//div[@class='pagination']/a[position()=last()]/@href").extract_first()
		if next_page is not None:
			next_page_link = response.urljoin(next_page)
			yield scrapy.Request(url=next_page_link, callback=self.parse)

		

		
	