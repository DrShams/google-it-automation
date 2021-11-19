import random
print(random.randint(1,100))

import datetime
now = datetime.datetime.now()
print(type(now))
print(now)
print(now.month)
print(now+ datetime.timedelta(days=28))
