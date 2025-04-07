import json

try:
    with open('chat_history.json', 'r', encoding='utf-8') as f:
        chat_data = json.load(f)
    print(f"تعداد کل پیامها: {len(chat_data)}")
    roles_count = {}
    for entry in chat_data:
        role = entry.get("role", "unknown")
        roles_count[role] = roles_count.get(role, 0) + 1

    print("تعداد پیامها بر اساس نقش:")
    for role, count in roles_count.items():
        print(f"- {role}: {count}")

except FileNotFoundError:
    print("خطا: فایل chat_history.json پیدا نشد!")
except json.JSONDecodeError:
    print("خطا: فایل JSON نامعتبر است!")