import sys
import os
import argparse
import csv
import json

def load_csv(contactsFile):
	"""
	Load contacts from a CSV file as a list of dicts.

	@param contactsFile - the file from which to load.
	@return a list of dicts of contact information.
	"""
	reader = csv.DictReader(contactsFile)
	return [{k: v for k, v in row.iteritems()
		if k and v and not str.isspace(v)}
		for row in reader]

def save_csv(contacts, contactsFile, fieldNames=None):
	"""
	Save contacts as CSV.

	@param contacts - the contacts to save.
	@param contactsFile - the file to which to save.
	@param fieldNames - the names of the fields to use in the header.
	"""
	if not fieldNames:
		fieldNames = {key for contact in contacts for key in contact}
	writer = csv.DictWriter(contactsFile, fieldNames)
	writer.writeheader()
	writer.writerows(contacts)

def save_csv_outlook(contacts, contactsFile):
	"""
	Save contacts as CSV with a header of Outlook field names.

	@param contacts - the contacts to save.
	@param contactsFile - the file to which to save.
	"""
	name = os.path.join(os.path.dirname(__file__), 'outlook_fields.txt')
	with open(name) as fieldNamesFile:
		fieldNames = fieldNamesFile.read().splitlines()
	save_csv(contacts, contactsFile, fieldNames)

def save_json(contacts, contactsFile):
	"""
	Save contacts as JSON.

	@param contacts - the contacts to save.
	@param contactsFile - the file to which to save.
	"""
	json.dump(contacts, contactsFile,
		indent=2, separators=(',',': '), sort_keys=True)

def main():
	parser = argparse.ArgumentParser(
		description='Converts contacts information from CSV to JSON format.')
	parser.add_argument('SOURCE', type=argparse.FileType('rb'),
		help='CSV file to read contacts from')
	parser.add_argument('DEST', type=argparse.FileType('wb'),
		help='JSON file to save contacts to')
	args = parser.parse_args()
	save_json(load_csv(args.SOURCE), args.DEST)

if __name__ == "__main__":
	sys.exit(main())
