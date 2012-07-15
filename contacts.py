import sys
import argparse
import csv
import json

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

def save_json(contacts, contactsFile):
	"""
	Save contacts as JSON.

	@param contacts - the contacts to save.
	@param contactsFile - the file to which to save,
	or the path to a file that will be opened.
	"""
	if isinstance(contactsFile, basestring):
		contactsFile = open(contactsFile, 'w')
	json.dump(contacts, contactsFile,
		indent=2, separators=(',',': '), sort_keys=True)

def main():
	parser = argparse.ArgumentParser(
		description='Converts contacts information from CSV to JSON format.')
	parser.add_argument('SOURCE', type=argparse.FileType('r'),
		help='CSV file to read contacts from')
	parser.add_argument('DEST', type=argparse.FileType('w'),
		help='JSON file to save contacts to')
	args = parser.parse_args();
	save_json(load_csv(args.SOURCE), args.DEST)

if __name__ == "__main__":
	sys.exit(main())
