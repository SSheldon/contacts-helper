import csv

def load_csv(contactsFile):
	"""
	Load contacts from a CSV file as a list of dicts.

	@param contactsFile - the file from which to load,
	or the path to a file that will be opened.
	@return a list of dicts of contact information.
	"""
	if isinstance(contactsFile, basestring):
		contactsFile = open(contactsFile)
	reader = csv.DictReader(contactsFile)
	contacts = []
	for row in reader:
		contact = {}
		for key, value in row.iteritems():
			if value and not str.isspace(value):
				contact[key] = value
		contacts.append(contact)
	return contacts
