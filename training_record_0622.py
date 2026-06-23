date = input("Date: ")
table_size = input("Table size: ")
training_item = input("Training item: ")
total_shot = int(input("total shot: "))
made_shot = int(input("made shot: "))
mental_score = int(input("mental score(1-5): "))

hit_percent = made_shot / total_shot * 100

print("\n========== Today's snooker training report ==========")
print(f"training date: {date}")
print(f"table size: {table_size}")
print(f"training item: {training_item}")
print(f"total shot: {total_shot}, made shot: {made_shot}")
print(f"hit percent: {hit_percent:.1f} %")
print(f"mental score: {mental_score}")

if hit_percent >= 85:
    print("Training evaluation: Excellent")
elif hit_percent >= 60:
    print("Training evaluation: Normal")
else:
    print("Training evaluation: Need more practice")