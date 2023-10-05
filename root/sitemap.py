from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from service.models import Services


class StaticSitemap(Sitemap):

    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [
            'root:home',
            'root:about',
            'root:contact',
            'root:pricing',
            'root:request',
            'service:service'
        ]
    
    def location(self,item):
        return reverse(item)


class DynamicSitemap(Sitemap):

    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Services.objects.filter(status=True)
    
    def location(self,obj):
        return '/service/service_detail/%s' % obj.id