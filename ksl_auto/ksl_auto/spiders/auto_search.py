# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Spider
from scrapy import Selector
from ksl_auto.items import KslAutoItem as Item
from scrapy.http import Request

class AutoSearchSpider(scrapy.Spider):
	name = "auto_search"
	allowed_domains = ["ksl.com"]
	start_urls = ['http://www.ksl.com/auto/search']
	
	page_num = 1
	def parse(self, response):
		hxs = Selector(response)
		listings = hxs.xpath("//div[@class='listing-group']/*")
		items = []
		for listing in listings:
			item = Item()
			link = listing.xpath("./h2[@class='title']/a/@href").extract_first()
			if link is None:
				continue
			item['link'] = 'http://www.ksl.com' + link.strip()
			item['title'] = listing.xpath("./h2[@class='title']/a/text()").extract_first().strip()
			
			price = listing.xpath("./div[@class='listing-detail-line price']/@data-price").extract_first()
			if price is None:
				price = 0
			item['price'] = price
			
			mileage = listing.xpath("./div[@class='listing-detail-line mileage']/text()").extract_first()
			if mileage is None:
				mileage = "0"
			item['mileage'] = int(mileage.strip().replace("Mileage: ","").replace(",",""))
		
			yield Request(item['link'], callback = self.parseCar, meta = {'item': item})

		next_page = hxs.xpath("//a[@title='Go forward 1 page']/@href").extract_first()
		if next_page is not None:
			url = 'http://www.ksl.com/auto/search?page={0}'.format(self.page_num)
			self.page_num += 1
			yield Request(url=url, callback=self.parse)

	def parseCar(self, response):
		hxs = Selector(response)
		item = response.meta['item']
		year = hxs.xpath("(//span[@class='value'])[1]/text()").extract_first()
		if year == '':
			year = "2017"
		item['year'] = int(year.replace("\n","").strip())
		item['make'] = hxs.xpath("(//span[@class='value'])[2]/text()").extract_first().replace("\n","").strip()
		item['model'] = hxs.xpath("(//span[@class='value'])[3]/text()").extract_first().replace("\n","").strip()
		vin = hxs.xpath("(//span[@class='value'])[7]/a/text()").extract_first()
		if vin is None:
			vin = hxs.xpath("(//span[@class='value'])[7]/text()").extract_first()
		item['vin'] = vin.replace("\n","").strip()
		item['title_type'] = hxs.xpath("(//span[@class='value'])[8]/text()").extract_first().replace("\n","").strip()
		return item
