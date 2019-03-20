class Entry:
    def __init__(self):
        self.entries = [{'id': 1, 'entry_name': 'name of the entry', 'anything': 'something'}, {'id': 2, 'entry_name': 'name of the entry', 'anything': 'something'}]

    def all_entries(self):
        return self.entries

    def single_entry(self, id):
        for entry in self.entries:
            if entry['id'] == id:
                return entry
            return False

    def create_entry(self, entry):
        if entry:
            self.entries.append(entry)
            return self.entries
return 'entry not provided'