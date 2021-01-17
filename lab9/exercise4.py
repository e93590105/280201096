import time
def rec_timer(n):
  if n==0:
    print("done")
    return None
  print(f"time remaining: {n}")
  time.sleep(1)
  return rec_timer(n-1)
rec_timer(3)