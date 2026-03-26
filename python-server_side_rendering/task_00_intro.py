"""Function to generate personalized event invitations from a template and attendee data."""

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Invalid input type for template.")
        return
    if not isinstance(attendees, list):
        print("Error: Invalid input type for attendees.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    keys = ["name", "event_title", "event_date", "event_location"]

    for i, person in enumerate(attendees, start=1):
        content = template
        for key in keys:
            value = person.get(key)
            if value is None:
                value = "N/A"
            content = content.replace(f"{{{key}}}", str(value))
        with open(f"output_{i}.txt", "w") as f:
            f.write(content)

if __name__ == "__main__":
    with open("template.txt", "r") as f:
        raw_template = f.read()

    attendees_list = [
        {"name": "Alice", "event_title": "Tech Gala", "event_date": "2026-05-15", "event_location": "Grand Hall"},
        {"name": "Bob", "event_title": "Workshop", "event_location": "Room 101"},
        {"name": "Charlie", "event_date": "2026-06-01"}
    ]

    generate_invitations(raw_template, attendees_list)
