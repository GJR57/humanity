import streamlit as st
import requests
import xml.etree.ElementTree as ET
import pandas as pd

# Send a GET request to the URL and retrieve the XML content
#https://lbezone.hkust.edu.hk/rse/western-collection

url = "https://lbezone.hkust.edu.hk/rse/OAI/Server.php?verb=ListRecords&metadataPrefix=oai_dc&set=western_collection"
response = requests.get(url)
response.encoding = 'utf-8'
xml_content = response.content

# Parse the XML content
root = ET.fromstring(xml_content)

# Create lists to store the extracted information
titles = []
dates = []
languages = []
urls = []
thumb_urls =[]

# Iterate over each record and extract the desired information
for record in root.findall(".//{http://www.openarchives.org/OAI/2.0/}record"):
    title = record.find(".//{http://purl.org/dc/elements/1.1/}title").text
    date = record.find(".//{http://purl.org/dc/elements/1.1/}date").text
    lang = record.find(".//{http://purl.org/dc/elements/1.1/}language").text

    titles.append(title)
    dates.append(date)
    languages.append(lang)

    identifiers = record.findall('.//{http://purl.org/dc/elements/1.1/}identifier')
    thumb_url = identifiers[1].text
    thumb_urls.append(thumb_url)

    doi_url = identifiers[4].text
    urls.append(doi_url)

# Create a dataframe from the extracted information
data = {
    "Title": titles,
    "Year": dates,
    "Language": languages,
    "URL": urls,
    "Thumbnail image": thumb_urls
}
data = pd.DataFrame(data)
st.dataframe(data, hide_index=True)