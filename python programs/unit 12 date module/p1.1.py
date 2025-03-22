import time

# Unix timestamp
timestamp = 1742626200.6440923
print('posix time ',timestamp)
# Convert timestamp to a readable date-time format
readable_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(timestamp))
# readable_time = time.strftime('%Y/%m/%d %H:%M:%S', time.gmtime(timestamp))

print('UTC (the Unix epoch) ',readable_time)
