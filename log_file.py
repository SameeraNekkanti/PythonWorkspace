def find_first_error(log_data):
    a=tuple()
    for timestamp,log_level,message in log_data:
        if log_level=='ERROR':
            return timestamp
# Sample Input
log_data = [
    ('08:30:01', 'INFO', 'Server started'),
    ('08:30:05', 'WARN', 'Low disk space'),
    ('08:31:10', 'INFO', 'User login'),
    ('08:32:00', 'ERROR', 'Database connection failed'),
    ('08:32:01', 'INFO', 'Retrying connection...'),
    ('08:33:00', 'ERROR', 'Authentication service timeout')
]

# Function call
result = find_first_error(log_data)
print(result)
