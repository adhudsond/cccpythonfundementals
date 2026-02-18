# contact_book.py
# Contact Management System (nested dictionaries + dict methods)

contacts = {
    "Alice": {"phone": "555-1234", "email": "alice@email.com"},
    "Bob": {"phone": "555-5678", "email": "bob@email.com"}
}

print("=" * 60)
print("CONTACT BOOK")
print("=" * 60)

# 2) Add new contact (example)
new_name = "Carol"
contacts[new_name] = {"phone": "555-9999", "email": "carol@email.com"}
print(f"Added new contact: {new_name}")

# 3) Update existing contact phone (example)
name_to_update = "Bob"
if name_to_update in contacts:
    contacts[name_to_update]["phone"] = "555-0000"
    print(f"Updated phone for {name_to_update}")
else:
    print(f"Cannot update: {name_to_update} not found")

# 4) Search for contact (safe access using .get)
search_name = "Alice"
found = contacts.get(search_name)

print("\n--- Search Result ---")
if found:
    print(f"{search_name}: Phone={found.get('phone', 'N/A')}, Email={found.get('email', 'N/A')}")
else:
    print(f"{search_name} was not found.")

# 5) List all contacts (loop through)
print("\n--- All Contacts ---")
for name, info in contacts.items():
    phone = info.get("phone", "N/A")
    email = info.get("email", "N/A")
    print(f"{name:<10} | Phone: {phone:<10} | Email: {email}")

# 6) Count total contacts
print("\n--- Summary ---")
print(f"Total contacts: {len(contacts)}")

# 7) Remove a contact (example)
remove_name = "Alice"
removed = contacts.pop(remove_name, None)

if removed:
    print(f"Removed contact: {remove_name}")
else:
    print(f"Cannot remove: {remove_name} not found")

print("\n--- Contacts After Removal ---")
for name, info in contacts.items():
    print(f"{name}: {info}")

print("=" * 60)
