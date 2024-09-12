import feedparser

# URL of the RSS feed
feed_url = "https://www.sec.gov/Archives/edgar/usgaap.rss.xml"

# Fetch and parse the RSS feed
feed = feedparser.parse(feed_url)

# Print the available keys in the feed object to understand its structure
print("Feed Object Keys:", feed.feed.keys())

# Print feed details if available
if 'title' in feed.feed:
    print(f"Feed Title: {feed.feed.title}")
else:
    print("Feed Title: Not available")

if 'link' in feed.feed:
    print(f"Feed Link: {feed.feed.link}")
else:
    print("Feed Link: Not available")

if 'description' in feed.feed:
    print(f"Feed Description: {feed.feed.description}")
else:
    print("Feed Description: Not available")

if 'updated' in feed.feed:
    print(f"Last Updated: {feed.feed.updated}")
else:
    print("Last Updated: Not available")

# Process each item in the feed
for entry in feed.entries:
    print("\n---")
    if 'title' in entry:
        print(f"Title: {entry.title}")
    else:
        print("Title: Not available")

    if 'link' in entry:
        print(f"Link: {entry.link}")
    else:
        print("Link: Not available")

    if 'published' in entry:
        print(f"Publication Date: {entry.published}")
    else:
        print("Publication Date: Not available")

    # Extract XBRL filing information
    if 'edgar:xbrlFiling' in entry:
        xbrl_filing = entry['edgar:xbrlFiling']
        print(f"Company Name: {xbrl_filing.get('edgar:companyName', 'N/A')}")
        print(f"Form Type: {xbrl_filing.get('edgar:formType', 'N/A')}")
        print(f"Filing Date: {xbrl_filing.get('edgar:filingDate', 'N/A')}")
        print(f"CIK Number: {xbrl_filing.get('edgar:cikNumber', 'N/A')}")
        print(f"Accession Number: {xbrl_filing.get('edgar:accessionNumber', 'N/A')}")
        print(f"File Number: {xbrl_filing.get('edgar:fileNumber', 'N/A')}")
        print(f"Acceptance Datetime: {xbrl_filing.get('edgar:acceptanceDatetime', 'N/A')}")
        print(f"Period: {xbrl_filing.get('edgar:period', 'N/A')}")
        print(f"Assistant Director: {xbrl_filing.get('edgar:assistantDirector', 'N/A')}")
        print(f"Assigned SIC: {xbrl_filing.get('edgar:assignedSic', 'N/A')}")
        print(f"Fiscal Year End: {xbrl_filing.get('edgar:fiscalYearEnd', 'N/A')}")

    # Print XBRL file URLs
    if 'edgar:xbrlFiles' in entry:
        for xbrl_file in entry['edgar:xbrlFiles']:
            print(f"XBRL File URL: {xbrl_file.get('edgar:url', 'N/A')}")
