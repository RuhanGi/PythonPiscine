import time
import datetime

n = time.time()
print(f"Seconds since January 1, 1970: {n:,.4f}", end=" ")
print(f"or {n:.2e} in scientific notation")
print(datetime.datetime.now().strftime("%b %d %Y"))
