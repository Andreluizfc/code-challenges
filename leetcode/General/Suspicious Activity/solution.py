suspicious_activities = [
    ("Brad", "San Francisco", "withdraw"),
]

new_activities = [
    ("Joe", "Miami", "withdraw"),
    ("John", "San Francisco", "deposit"),
    ("Albert", "London", "withdraw"),
    ("Diana", "London", "withdraw"),
    ("Diana", "San Francisco", "withdraw"),
    ("Joe", "New York", "updateaddress"),
]

def find_suspicious_activities(suspicious_activities, new_activities, k=2):
    final_activities = []
    
    while True:
        new_suspicious = []
        for new_activity in new_activities:
            if is_suspicious(new_activity, suspicious_activities, k) and new_activity not in final_activities:
                new_suspicious.append(new_activity)

        if not new_suspicious:
            break

        for activity in new_suspicious:
            final_activities.append(activity)
            suspicious_activities.append(activity)

    return final_activities


def is_suspicious(new_activity, suspicious_activities, k):
    for suspicious_activity in suspicious_activities:
        if count_matching_values(new_activity, suspicious_activity) >= k:
            return True
    return False

def count_matching_values(activity1, activity2):
    count = 0
    for a, b in zip(activity1, activity2):
        if a == b:
            count += 1
    return count

suspicious_results = find_suspicious_activities(suspicious_activities, new_activities, 2)

for activity in suspicious_results:
    print(activity)
