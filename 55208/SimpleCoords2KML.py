# By: Brendan Luke
# Date: February 16, 2022
# Scope: turn .csv of Alt, Lat, Lon data into KML file for Google Earth Pro viewing

# Libraries
import os
from csv import reader

# Load Files as Text
dirname = os.path.dirname(__file__) # use relative file path (same folder)

# String initial (KML spec)
kmlString = """<?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2">
    <Document>
    \t<name>KML File</name>
    \t<description>
    \t\tThis file was generated via: <link>https://github.com/BrendanLuke15/SX_SE_Repo/tree/main/55208</link>.
    \t</description>
    \t<Style id="RedLine">
    \t\t<LineStyle>
    \t\t\t<color>ff0000ff</color>
    \t\t\t<width>2</width>
    \t\t</LineStyle>
    \t\t<PolyStyle>
    \t\t\t<fill>0</fill>
    \t\t</PolyStyle>
    \t</Style>
    \t<Folder id="Main">
    \t\t<visibility>1</visibility>
    \t\t<open>1</open>
    \t\t<name>Simple CSV Data</name>
    \t\t<Placemark id="3DPathNoExtrude">
    \t\t\t<name>3D Path</name>
    \t\t\t<styleUrl>#RedLine</styleUrl>
    \t\t\t<LineString>
    \t\t\t\t<extrude>0</extrude>
    \t\t\t\t<tessellate>0</tessellate>
    \t\t\t\t<altitudeMode>absolute</altitudeMode>
    \t\t\t\t<coordinates>\n"""

# Read file by line and populate string
with open(dirname + '/csvData.csv', 'r') as f_in: # change filename as needed
    csv_reader = reader(f_in)
    for row in csv_reader:
        kmlString += row[2] + ',' + row[1] + ',' + row[0] + '\n' # add data

# Closeout KML spec
endStr = """\t\t\t\t</coordinates>
\t\t\t</LineString>
\t\t</Placemark>
\t</Folder>
</Document>
</kml>"""
kmlString = kmlString + endStr

# Write file
with open(dirname + '/OutFile.kml','w') as f_out: # change filename as needed
    f_out.write(kmlString)