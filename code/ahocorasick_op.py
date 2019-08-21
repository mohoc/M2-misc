import ahocorasick

def build_auto(F):
	auto = ahocorasick.Automaton()
	for f in F:
		auto.add_word(f, f)
	auto.make_automaton()
	return auto

def is_substring(auto, w):
	for _, _ in auto.iter(w):
		return True
	return False

def find_occurrences(auto, w):
	occurrences = []
	for end_idx, found in auto.iter(w):
		occurrences += (end_idx, found)
	return occurrences