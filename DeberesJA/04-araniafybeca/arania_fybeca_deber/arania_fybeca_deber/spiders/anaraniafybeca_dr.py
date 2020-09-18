import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlFybeca(CrawlSpider):
    name = 'crawl_fybeca' #heredado

    allowed_domain = [
        'fybeca.com'
    ]

    start_urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=446&s=0&pp=3000',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=537&s=0&pp=3000',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=446&s=0&pp=3000',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=627&s=0&pp=3000',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=558&s=0&pp=3000',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=489&s=0&pp=3000',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=562&s=0&pp=3000',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=457&s=0&pp=3000&q='
    ]

    regla_uno = {
        Rule( LinkExtractor(), callback='parse_page' )
        ,
    }

    

    segmentos_url_permitidos = {
        'cat=446&s',
        'cat=537&s',
        'cat=446&s',
        'cat=627&s',
        'cat=558&s',
        'cat=489&s',
        'cat=562&s',
        'cat=457&s'
    }

    regla_dos = {
         Rule( LinkExtractor(
             allow_domains=allowed_domain,
             allow = segmentos_url_permitidos

         ), callback='parse_page' )
        ,
    }

    url_segmento_restringido = (
        'ar/sections',
        'zh/sections',
        'ru/sections'
    )

    regla_tres = (
        Rule(
            LinkExtractor(
                allow_domains=allowed_domain,
                allow=segmentos_url_permitidos,
                deny=url_segmento_restringido
            ),callback='parse_page'
        ),
    )

    rules = regla_dos

    def parse_page(self, response):
        etiqueta_contenedora = response.css(
            'div.product-tile-inner'
        )

        nombres = etiqueta_contenedora.css(
            'a.name::text'
        ).extract()
                
        precios = etiqueta_contenedora.css(
            'div.detail>div.side > div.price'
        ).xpath("@data-bind").extract()

        precios_final = [b.replace("text:'$' + (", '').replace(").formatMoney(2, '.', ',')", '') for b in precios] 

        lista_precios=[]
        for p in precios_final:
            lista_precios.append(p)
        [float(i) for i in lista_precios]

       
        precios_miembro = etiqueta_contenedora.css(
            'div.detail>div.side > div.price-member >div'
        ).xpath("@data-bind").extract()
        
        precios_miembro_final = [b.replace("text:'$' + (", '').replace(").formatMoney(2, '.', ',')", '') for b in precios_miembro] 

        lista_precios_miembros=[]
        for p in precios_miembro_final:
            lista_precios_miembros.append(p)
        [float(i) for i in lista_precios_miembros]

        


        for (nombre, precio,precio_afiliado) in zip(nombres, precios_final,precios_miembro_final): 
            with open('fybeca_items.txt', 'a+', encoding='utf-8') as archivo:
                archivo.write(nombre + '\t'+'Para no afiliados: $'+ precio+ '\t'+' Para Afiliado: $'+precio_afiliado+ '\t' +'Ahorro: $'+str(round((float(precio) - float(precio_afiliado)),2))+'\n')
