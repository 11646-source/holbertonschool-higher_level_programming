#!/usr/bin/python3

import requests
import csv

# Function to fetch and print posts
def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print status code
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()  # Parse JSON response
        # Print titles of all posts
        for post in posts:
            print(post['title'])
    else:
        print("Failed to fetch posts.")

# Function to fetch and save posts into CSV
def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Structure data into list of dictionaries
        structured_posts = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        # Write to CSV file
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(structured_posts)

        print("Posts saved to posts.csv successfully.")
    else:
        print("Failed to fetch posts.")

# Run both functions when executed directly
if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
