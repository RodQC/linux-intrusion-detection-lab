import re
from datetime import datetime

log_file = "/var/log/auth.log"

#Captures the timestamp at line start (The &(\S+)
#The from part captures the attackers ip address
pattern = r"^(\S+).*Failed password.*from (\d+\.\d+\.\d+\.\d+)"

attacks = {}

with open(log_file, "r") as f:
	for line in f:
		match = re.search(pattern, line)
		if match:
			timestamp = match.group(1)
			ip = match.group(2)

			#Converst timestamp to real time object
			time_obj = datetime.fromisoformat(timestamp.replace("Z",""))

			#The attack[ip] stores the count and the time window per attacker
			if ip not in attacks:
				attacks[ip] = {"count": 1, "first": time_obj, "last": time_obj}
			else:
				attacks[ip]["count"] += 1
				attacks[ip]["last"] = time_obj

THRESHOLD = 5

print("\n--- Intrusion Detection Report---\n")

for ip, data in attacks.items():
#Alert block, if log in attempts is >= 5 then it will consider it as a attack
	if data["count"] >= THRESHOLD:
		duration = data["last"] - data["first"]
		print(f"ALERT: {ip}")
		print(f" Attempts: {data['count']}")
		print(f" First Seen: {data['first']}")
		print(f" Last Seen: {data['last']}")
		print(f" Duration: {duration}\n")

		import subprocess
		subprocess.run(["sudo", "ufw", "deny", "from", ip])
