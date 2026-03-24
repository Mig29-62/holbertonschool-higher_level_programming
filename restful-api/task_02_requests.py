"""Fetch and print or save JSONPlaceholder posts."""
import requests
import csv

def fetch_and_print_posts():
    """Fetch all posts and print their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        for post in response.json():
            print(post.get("title"))

def fetch_and_save_posts():
    """Fetch all posts and save to posts.csv."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            for post in posts:
                writer.writerow({k: post.get(k) for k in ["id", "title", "body"]})

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
