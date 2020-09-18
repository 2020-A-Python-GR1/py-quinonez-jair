import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import pandas as pd
class SerieSpider(CrawlSpider):
    name = 'arania_csv'
    start_urls = [
        'https://danimados.com/'
    ]
    for i  in range(1,27):
        start_urls.append('https://danimados.com/genero/animacion/page/{i}/'.format(i=i))
    segmentos_url_permitidos = (
        'series'
    )
    allowed_domains = [
        'danimados.com'
    ]
    regla_dos = (
        Rule(
            LinkExtractor(
                allow_domains = allowed_domains,
                allow = segmentos_url_permitidos
            ),
            callback = 'parse'
        ),
    )
    regla_uno = (
        Rule(
            LinkExtractor(),
            callback = 'parse_page' #nombre funcion a ejecutar para parsear
        ),
        #segundo parametro vacio 
    )
    rules = regla_dos
    name_serie = []
    release_date = []
    channel = []
    runtime = []
    start_date = []
    genre = []
    end_date = []
    rating_votes = []
    rating = []

    def parse(self,response):
        info = response.css('div.sbox > div.custom_fields > span.valor::text').extract()
        name = response.css('div.content > div.sheader > div.data > h1::text').extract()
        main_info = response.css('div.content > div.sheader > div.data > div.extra')
        name_serie = name[0]
        if('&amp;' in name_serie):
            name_serie = name_serie.replace('&amp;','&')
        self.name_serie.append(name_serie)
        if(len(info)<=6):
            runtime = info[5]
            self.runtime.append(runtime)
        else:
            self.runtime.append("")
            print(len(info))
        if(len(info)<=6):
            end_date = info[2]
            self.end_date.append(end_date)
        else:
            self.end_date.append("")
        if(main_info.css('span.date::text').extract()):
            release_date = main_info.css('span.date::text').extract()[0]
            self.release_date.append(release_date)
        else:
            self.release_date.append("")
        if(main_info.css('span > a::text').extract()):
            channel = main_info.css('span > a::text').extract()[0]
            self.channel.append(channel)
        else:
            self.channel.append("")
        if(response.css('div.starstruck-rating > span.dt_rating_vgs::text').extract()):
            rating = response.css('div.starstruck-rating > span.dt_rating_vgs::text').extract()[0]
            self.rating.append(rating)
        else:
            self.rating.append("")
        if(response.css('div.starstruck-rating > span.rating-count::text').extract()):
            rating_votes = response.css('div.starstruck-rating > span.rating-count::text').extract()[0]
            self.rating_votes.append(rating_votes)
        else:
            self.rating_votes.append(rating_votes)
        if(response.css('div.sgeneros > a::text').extract()):
            genre = response.css('div.sgeneros > a::text').extract()[0]
            #genre2 = genre.replace()
            #self.genre.append(genre)
            if('ó' in genre):
                genre= genre.replace('ó','o')
                self.genre.append(genre)
            else:
                self.genre.append(genre)
        else:
            self.genre.append("")
        

        

    def closed( self, reason ):
        save_path = '../series.csv'
        df = pd.DataFrame(
            {
                'name_serie': pd.Series(self.name_serie),
                'release_date': pd.Series(self.release_date),
                'channel': pd.Series(self.channel),
                'runtime': pd.Series(self.runtime),
                'end_date': pd.Series(self.end_date),
                'genre': pd.Series(self.genre),
                'rating': pd.Series(self.rating),
                'votes': pd.Series(self.rating_votes)
            }
        )
        df.to_csv(save_path,index=False)