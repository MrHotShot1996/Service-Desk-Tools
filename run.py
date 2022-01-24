from servicehub import servicehub_response
from emailres import email_response
from incidents import self_incident
from request import app_inst_request, email_config_request, clarvia_reset_request

def main():
	'''Main Application'''
	choice = input(
		"Choose Service reply type:\n"
		"1 - Service Hub responses\n"
		"2 - Email Responses\n"
		"3 - Incidents\n"
		"4 - Requests\n"
		)

	if choice == '1':
		servicehub_response()
	elif choice == '2':
		email_response()
	elif choice == '3':
		choice = input(
			'Choose an incident service:\n'
			'1 - Create self incident\n'
			)
		if choice == '1':
			self_incident()

	elif choice == '4':
		choice = input(
			'Choose a request service:\n'
			'1 - Application installation\n'
			'2 - Email mobile configuration\n'
			'3 - Clarvia password reset\n'
			)
		# Request services
		if choice == '1':
			app_inst_request()
		elif choice == '2':
			email_config_request()
		elif choice == '3':
			clarvia_reset_request()





if __name__ == '__main__':
	main()