import sys
from pathlib import Path

PROJECT_ROOT = Path.cwd().parent

sys.path.insert(0, str(PROJECT_ROOT))


from app.gmail import Gmail, get_body, get_headers

sys.path.append("..")

gmail = Gmail()
print("Connected as", gmail.address)

message_id = gmail.list_new_message_ids(max_results=1)[0]
message = gmail.get_message(message_id)
headers = get_headers(message)
print(headers["from"], "|", headers.get("subject"))
print(get_body(message)[:500])

gmail.send_reply(message, "Thanks, we received your email.")
print("Reply sent")