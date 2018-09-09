def flatten(dictionary):
	def helper(d, pref):
		for k in d.keys():
			if type(d.get(k)) == dict:
				neuPref = '{}{}.'.format(pref, k)
				helper(d[k], neuPref)
			else:
				s = '{}{}'.format(pref, k)
				newDict[s] = d[k]

	newDict = {}
	helper(dictionary, '')

	return newDict

def main():
	d = {
		'key': 3,
		'foo': {
			'a': 5,
			'b': 13,
			'bar': {
				'baz': 8,
			},
		},
		'sub': {
			'one': 1,
			'two': -1,
		}
	}

	d_prime = flatten(d)
	print(d_prime)

if __name__ == '__main__':
	main()