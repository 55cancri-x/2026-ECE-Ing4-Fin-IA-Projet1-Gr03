from src.strategies.twap import twap_schedule

print("Running TWAP test...")
print(twap_schedule(Q=100, N=10))
