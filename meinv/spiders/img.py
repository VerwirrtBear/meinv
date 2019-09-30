import scrapy
from meinv.items import MeinvItem

class ImgspiderSpider(scrapy.Spider):
    name = 'meinv'
    allowed_domains = ['meitulu.com']
    start_urls = ['https://www.meitulu.com/item/15723.html']

    def parse(self, response):
        img=[]
        item = MeinvItem()  # 实例化item
        next_p = response.css('a.a1::attr(href)').extract()[1]
        imgurls = response.css('img.content_img::attr(src)').extract() # 注意这里是一个集合也就是多张图片
        
        if next_p is not None:
            next_page =response.urljoin(next_p)
            yield scrapy.Request(next_page, callback=self.parse)
        item['imgurl']= imgurls
        yield item
        with open('a.txt','a') as f:
            f.write('%s' % img)

        pass
