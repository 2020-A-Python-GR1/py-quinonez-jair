import scrapy 
class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'
    urls = [
        'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)
    
    def parse(self, response):
        etiqueta_contenedora = response.css('article.product_pod')
        titulos =etiqueta_contenedora.css('h3 > a::text').extract()
        print("Titulos")
        print("{}".format(titulos))
        #valores
        valor_libro = etiqueta_contenedora.css('div.product_price > p.price_color::text').extract()
        valor_list = list()
        for i in valor_libro:
            valor_list.append(float(i.split('£')[1]))
        print("Valores")
        print("{}".format(valor_list))
        #Stock
        stock = etiqueta_contenedora.css('div.product_price > p.instock.availability::text').extract()
        stock_list = list()
        for i in stock:
            aux = i.split('\n')
            if(len(aux) > 2):
                stock_list.append(aux[2])
        print("STOCK")
        print("{}".format(stock_list))
        #Imagenes
        imagenes = etiqueta_contenedora.css('div.image_container > a > img::attr(src)' ).extract()
        print(imagenes)
        estrellas = etiqueta_contenedora.css('p.star-rating::attr(class)').extract()
        print(estrellas)



##el comando es
##scrapy crawl introduccion_spider