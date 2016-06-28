
from system.core.router import routes


routes['default_controller'] = 'Welcome'
routes['POST']['/register'] = 'Welcome#register'
routes['POST']['/login'] = 'Welcome#login'
routes['POST']['/create_book'] = 'Books#create_book'
routes['/add'] = 'Books#add'
routes['/home'] = 'Books#home'



