from flask_restful import Resource, reqparse
from models.site import SiteModel

class Sites(Resource):
    def get(self):
        return {'sites': [site.json() for site in SiteModel.query.all()]}
    
class Site(Resource):
    def get(self, url):
        site = SiteModel.find_site(url)
        if site:
            return site.json()
        return {'Message': 'Site Not Found.'}, 404   
    
    def post(self, url):
        if SiteModel.find_site(url):
            return {'Message': 'Site alread exists.'}, 400
        site = SiteModel(url)
        
        try:
            site.save_site()
        except :
            return {'Message': 'An internal error ocurred trying to create a new site'}, 400
        return site.json(), 201
    
    def delete(self, url):
        site = SiteModel.find_site(url)
        if site:
            site.delete_site()
            return {'Message': 'Site deleted'}, 204
        return {'Message': 'Site not found.'}, 404