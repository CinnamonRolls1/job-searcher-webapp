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
		for job in response.xpath("//div[@class='title']/a/text()"):
			yield {
				'TITLE' : job.extract()  
			}

		next_page = response.xpath("//div[@class='pagination']/a[position()=last()]/@href").extract_first()
		if next_page is not None:
			next_page_link = response.urljoin(next_page)
			yield scrapy.Request(url=next_page_link, callback=self.parse)

		

		
	