import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import pandas as pd
class SerieSpider(CrawlSpider):
    name = 'arania_csv'
    start_urls = [
        'https://danimados.com/'
    ]
    for i  in range(1,27): #27 páginas
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
    #imdb_votes = []
    #tmdb_rating = []
    #tmdb_votes = []
    def parse(self,response):
        info = response.css('div.sbox > div.custom_fields > span.valor::text').extract()
        main_info = response.css('div.content > div.sheader > div.data > div.extra')
        name_serie = info[0]#.split('>')[1].split('<')[0]
        if('&amp;' in name_serie):
            name_serie = name_serie.replace('&amp;','&')
        self.name_serie.append(name_serie)
        if(len(info)<=6):
            runtime = info[5]#.split('>')[6].split('<')[5]
            self.runtime.append(runtime)
        else:
            self.runtime.append("")
            print(len(info))
        if(len(info)<=6):
            end_date = info[2]
            self.end_date.append(end_date)
        else:
            self.end_date.append("")
        # if(len(info)==6):
        #     imdb_rating = info[1].split('<strong>')[1].split('</strong>')[0]
        #     self.imdb_rating.append(imdb_rating)
        #     imdb_votes = info[1].split('</strong>')[1].split('votos')[0].strip()
        #     self.imdb_votes.append(imdb_votes)
        #     tmdb_rating = info[2].split('<strong>')[1].split('</strong>')[0]
        #     self.tmdb_rating.append(tmdb_rating)
        #     tmdb_votes = info[2].split('</strong>')[1].split('votos')[0].strip()
        #     if('</span>' in tmdb_votes):
        #         self.tmdb_votes.append("")
        #     else:
        #         self.tmdb_votes.append(tmdb_votes)
        # elif(len(info)==2):
        #     if("repimdb" in info[1]):
        #         imdb_rating = info[1].split('<strong>')[1].split('</strong>')[0]
        #         self.imdb_rating.append(imdb_rating)
        #         imdb_votes = info[1].split('</strong>')[1].split('votos')[0].strip()
        #         self.imdb_votes.append(imdb_votes)
        #         self.tmdb_rating.append("")
        #         self.tmdb_votes.append("") 
        #     else:
        #         tmdb_rating = info[1].split('<strong>')[1].split('</strong>')[0]
        #         self.tmdb_rating.append(tmdb_rating)
        #         tmdb_votes = info[1].split('</strong>')[1].split('votos')[0].strip()
        #         if('</span>' in tmdb_votes):
        #             self.tmdb_votes.append("")
        #         else:
        #             self.tmdb_votes.append(tmdb_votes)
        #         self.imdb_rating.append("")
        #         self.imdb_votes.append("")
        # else:
        #     self.tmdb_rating.append("")
        #     self.tmdb_votes.append("")
        #     self.imdb_rating.append("")
        #     self.imdb_votes.append("")

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
        #if(main_info.css('span.runtime::text').extract()):
        #    runtime = main_info.css('span.runtime::text').extract()[0]
        #    self.runtime.append(runtime)
        #else:
        #   self.runtime.append("")
        # if(main_info.css('span.rated::text').extract()):
        #     rating = main_info.css('span.rated::text').extract()[0]
        #     self.rating.append(rating)
        # else:
        #     self.rating.append("")
        if(response.css('div.sgeneros > a::text').extract()):
            genre = response.css('div.sgeneros > a::text').extract()[0]
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
                #'imdb_rating': pd.Series(self.imdb_rating),
                #'imdb_votes': pd.Series(self.imdb_votes),
                #'tmdb_rating': pd.Series(self.tmdb_rating),
                #'tmdb_votes': pd.Series(self.tmdb_votes)
            }
        )
        df.to_csv(save_path,index=False)