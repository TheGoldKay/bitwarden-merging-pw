import csv, time

with open('BITWARDEN_VAULT.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    delay = 1.2
    data = dict()
    for row in csv_reader:
        # Column names are -> folder, favorite, type, name, notes, fields, reprompt, login_uri, login_username, login_password, login_totp
        #print(f'[{row[0]}], [{row[1]}], [{row[2]}], [{row[3]}], [{row[4]}], [{row[5]}], [{row[6]}], [{row[7]}], [{row[8]}], [{row[9]}], [{row[10]}]')
        username = row[8].strip()
        password = row[9].strip()
        url = row[7].strip()
        name = row[3].strip()
        key = f"{username}{password}"
        if not data.get(key):
            data[key] = {"URL": url, "Name": name}
        line_count += 1
        #data.add(u)#((username, password, url, name))
        print(f"User: {username} | Pass: {password} | Url: {url} | Name: {name}")
        time.sleep(delay)
    # Processed 997 lines.
    print(f'\n\nProcessed {len(data)} lines.\n\n')