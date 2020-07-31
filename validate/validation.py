
class Validation:
	users={'admin':'1234','administrator':'1234'}
	def login(self,username,password):
		d='none'
		if(username in self.users.keys()):
			if(password in self.users.get(username)):
				d='success'
		return d






