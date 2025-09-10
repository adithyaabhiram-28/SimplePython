'''
A 3-day tech workshop collected attendee registrations separately for each day. You are given three lists (day1, day2, day3) of email addresses — lists may contain duplicates (people registering multiple times) and email case may vary (Upper/Lower).
Write a Python program that:
Cleans each day's list (normalizes case, removes duplicates).
Prints the total number of unique attendees across all days.
Prints the list of attendees who attended all three days.
Prints the list of attendees who attended exactly one day.
Prints pairwise overlap counts (day1 & day2, day2 & day3, day1 & day3).
Produces a final report with counts and sorted lists for each of the above outputs.
'''

def report(d1, d2, d3):
    s1 = set(d1)
    s2 = set(d2)
    s3 = set(d3)
    print("Day 1:", s1)
    print("Day 2:", s2)
    print("Day 3:", s3)
    print(f"Total {len(s1|s2|s2)} unique attendees in all days : ",sorted(s1|s2|s3))
    print("Total all attendees in all days : ",s1&s2&s3)
    print("Total unique attendees exactly one day : ",s3-(s2|s1))
    print("Overlap of pairs : ",s1&s2,s2&s3,s1&s3)
    

    

day1 = input("Enter Day 1 attendee emails : ").split(" ")
day2 = input("Enter Day 2 attendee emails : ").split(" ")
day3 = input("Enter Day 3 attendee emails : ").split(" ")

report(day1, day2, day3)
