#Filter Hyperlink
# Read hyperlinks from the "hyperlinks.txt" file
with open("hyperlinks.txt", "r") as f:
    hyperlinks = f.readlines()

# Separate the hyperlinks into two lists based on the condition
filtered_hyperlinks = []
remaining_hyperlinks = []

for hyperlink in hyperlinks:
    if hyperlink.startswith("url"):
        filtered_hyperlinks.append(hyperlink)
    else:
        remaining_hyperlinks.append(hyperlink)

# Save the filtered hyperlinks to one file
with open("filtered_hyperlinks.txt", "w") as f:
    f.writelines(filtered_hyperlinks)

# Save the remaining hyperlinks to another file
with open("remaining_hyperlinks.txt", "w") as f:
    f.writelines(remaining_hyperlinks)