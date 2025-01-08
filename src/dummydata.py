# Extend the dataset with an engagement parameter and generate more data
rows_extended = []
for _ in range(5000):  # Generate 5000 rows of data
    user = random.choice(users)
    action = random.choice(actions)
    source = random.choice(sources)
    post_type = random.choice(post_types)
    topic = random.choice(topics)
    engagement = random.randint(1, 100)  # Random engagement score between 1 and 100
    rows_extended.append({
        "User": user,
        "Action": action,
        "Source": source,
        "Post Type": post_type,
        "Topic": topic,
        "Engagement": engagement
    })

# Define the updated CSV file path
file_path_extended = "/mnt/data/extended_social_media_engagement.csv"

# Save to CSV
with open(file_path_extended, mode="w", newline="") as file:
    writer = csv.DictWriter(
        file, fieldnames=["User", "Action", "Source", "Post Type", "Topic", "Engagement"]
    )
    writer.writeheader()
    writer.writerows(rows_extended)

file_path_extended

