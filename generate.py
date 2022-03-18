import requests

r = requests.get('http://webconcepts.info/concepts/http-status-code.json')
json = r.json()
template = "response-template.html"

for i in json["values"]:
    with open(template) as f:
        content = f.read()
        new_content = content
        error_code = int(i["value"])

        #print("Error Code: %d" % (error_code))

        if error_code == 418 or error_code < 400 or error_code > 599:
            continue
        # Set the background and body color for the different error codes
        body_color = "#fefefe"
        if error_code < 200:
            # 1xx codes
            bg_color = "#78909C"
        elif error_code < 300:
            # 2xx codes
            bg_color = "#1E88E5"
        elif error_code < 500:
            # 3xx and 4xx codes
            bg_color = "#e74c3c"
        elif error_code < 600:
            # 5xx codes
            bg_color = "#f1c40f"
        new_content = new_content.replace("$ERROR_CODE", i["value"])
        new_content = new_content.replace("$ERROR_NAME", i["description"])
        new_content = new_content.replace("$ERROR_DESC", i["details"][0]["description"])
        new_content = new_content.replace("$BG_COLOR", bg_color)
        new_content = new_content.replace("$BODY_COLOR", body_color)
        with open(i["value"] + ".html", "w") as output_file:
            output_file.write(new_content)
        print(f"ErrorDocument {error_code} /errors/{error_code}.html")


