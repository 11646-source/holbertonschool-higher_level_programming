import os

def generate_invitations(template, attendees):
    # --- Input Type Checks ---
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # --- Empty Input Checks ---
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # --- Process Each Attendee ---
    for idx, attendee in enumerate(attendees, start=1):
        # Replace placeholders with attendee data or "N/A"
        processed = template
        for placeholder in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(placeholder, "N/A")
            processed = processed.replace(f"{{{placeholder}}}", value)

        # --- Generate Output File ---
        filename = f"output_{idx}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(processed)
        print(f"Generated {filename}")

# --- Example Usage ---
template = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team
"""

attendees = [
    {"name": "Alice", "event_title": "Tech Conference", "event_date": "April 10, 2026", "event_location": "New York"},
    {"name": "Bob", "event_title": "Tech Conference", "event_date": "April 10, 2026"},  # Missing location
    {"name": "Charlie", "event_title": "Tech Conference", "event_location": "New York"}  # Missing date
]

generate_invitations(template, attendees)
