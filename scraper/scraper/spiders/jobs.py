import scrapy

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
			yield {
				'TITLE' : job.xpath("normalize-space(.//div[@class='title']/a/text())").extract_first(),
				'COMPANY' : job.xpath("normalize-space(.//span[@class='company']/text())").extract_first(),
				'LOCATION' : job.xpath("normalize-space(.//div[contains(@class,'location')])").extract_first(),
				'SALARY' : job.xpath("normalize-space(.//span[contains(@class, 'salary')])").extract_first(),
				'AGE OF POSTING' : job.xpath("normalize-space(.//span[@class='date '])").extract_first()
			}

		next_page = response.xpath("//div[@class='pagination']/a[position()=last()]/@href").extract_first()
		if next_page is not None:
			next_page_link = response.urljoin(next_page)
			yield scrapy.Request(url=next_page_link, callback=self.parse)

		

		
	