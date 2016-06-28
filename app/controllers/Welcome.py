from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        self.load_model('User')

    def index(self):
        return self.load_view('index.html')
    def login(self):
        user = {
            'email' : request.form['email'],
            'password' : request.form['password']
        }
        login_user = self.models['User'].login(user)

        if login_user['status'] == True:
            session['id'] = login_user['user']['id']
            session['username'] = login_user['user']['username']
            return self.load_view('home.html')
        else:
            for message in login_user['errors']:
                flash(message, 'regis_errors')
            return redirect('/')

    def register(self):
        user_details = {
            'name' : request.form['name'],
            'username' : request.form['username'],
            'email' : request.form['email'],
            'password' : request.form['password'],
            'confirm_password' : request.form['confirm_password']
        }
        # print dir(self.models['User'])
        user_status = self.models['User'].register(user_details)

        if (user_status['status']==True):
            session['id']=user_status['user']['id']
            session['name']=user_status['user']['name']
            session['username']=user_status['user']['username']
            session['email']=user_status['user']['email']
            return self.load_view('home.html')
        else:
            for message in user_status['errors']:
                flash(message, 'regis_errors')
            return redirect('/')

