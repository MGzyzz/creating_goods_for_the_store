from controllers.base import BaseController
import requests
import utils
from controllers.base import BaseController
from db.database import Database
from template_engine.jinja import env


class PagesController(BaseController):

    def get_list(self):
        tmp = env.get_template('pages/home.html')
        body = tmp.render(information=Database.all(), total=Database.total_sum())

        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(body)


    def new(self):
        tmp = env.get_template('pages/create_page.html')
        body = tmp.render()
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(body)

    def create(self):
        Database.add(self.request.body)
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_status(301)
        self.response.add_header('Location', '/')
        self.response.set_body('<a href="/">Back to posts list</a>')

    def graphics(self):
        tmp = env.get_template('pages/graphic.html')
        data = list(zip(Database.sum_category(), Database.colors))
        print(data)
        body = tmp.render(information=data, total=Database.total_sum())
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(body)


