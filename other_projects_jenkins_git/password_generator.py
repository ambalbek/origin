import string

import random



def pw_gen(size = 12, chars=string.ascii_letters + string.digits + string.punctuation):

	return ''.join(random.choice(chars) for _ in range(size))



print(pw_gen())
