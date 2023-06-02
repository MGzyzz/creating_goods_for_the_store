
from controllers.pages import PagesController
from src.router import Router
from src.server import runserver

config = {
    'host': 'localhost',
    'port': 1025,
    'static': 'static'
}

router = Router()
router.get('/', PagesController, 'get_list')
router.get('/page_create', PagesController, 'new')
router.get('/graphics', PagesController, 'graphics')
router.post('/', PagesController, 'create')


runserver(router, config)