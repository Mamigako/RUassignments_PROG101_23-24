# ask for input, convert to int.
temp_now = int(input())
temp_prev = int(input())
# Assign instructions to variables.
RAISE = "raise"
KEEP = "keep"
LOWER = "lower"
SHUTDOWN = "shutdown"

# If temperature is below 300 not rising, raise temp.
if temp_now < 300 and (temp_prev == temp_now or temp_prev > temp_now):
    print(RAISE)
# If temperature is between 300 and 350 and rising, lower temp.
elif 350 > temp_now > 300 and (temp_prev == temp_now or temp_prev < temp_now):
    print(LOWER)
# If temperature is at or above 350, emergency shutdown.
elif temp_now >= 350:
    print(SHUTDOWN)
# In all other cases, keep temp the same.
else: 
    print(KEEP)
    