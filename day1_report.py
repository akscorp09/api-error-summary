
errors = [
    {"status": 401, "priority": "High"},
    {"status": 404, "priority": "Medium"},
    {"status": 503, "priority": "Critical"},
    {"status": 500, "priority": "High"},
    {"status": 422, "priority": "Medium"}
]

# terrors = []

terrors = []

high_count = 0
medium_count = 0
critical_count = 0
urgent_count = 0

for error in errors:
    if error["priority"] == "High":
        high_count += 1
        urgent_count += 1

    elif error["priority"] == "Critical":
        critical_count += 1
        urgent_count += 1

    elif error["priority"] == "Medium":
        medium_count += 1

total_errors = len(errors)

print("===== API ERROR REPORT =====")
print("Total errors:", total_errors)
print("High priority:", high_count)
print("Medium priority:", medium_count)
print("Critical priority:", critical_count)
print("Urgent priority:", urgent_count)


if total_errors > 0:
    urgent_percentage = (urgent_count / total_errors) * 100
else:
    urgent_percentage = 0

print("Urgent priority percentage: {:.2f}%".format(urgent_percentage))
