# smapshot-jpdem
Conversion of Japanese DEM XML files into Geotiffs.

The conversion can be done using the CLI Python tool "jpgis-dem" developped by gpxz:
- Blog: https://www.gpxz.io/blog/jpgis-dem  
- Github repository: https://github.com/gpxz/jpgis-dem/tree/main?tab=readme-ov-file  
Installation and usage instructions of jpgis-dem can be found there.

The tool has been developped for converting DEMs. To use it on DGHMs, a quick patch is to simply replace "DGHM" occurrences with "DEM".  

## Usage
1. Patch DGHMs (--zip option if it is a zip folder)      
`python .\fix_dghm_tags.py "{zip_path}" "{patched_path}" --zip`

2. Convert to geotiffs with jpgis-dem  
`jpgis-dem xml2tif "{patched_path}" "{geotiff_path}"`
 
*Notes: the tools can convert both single XML files or ZIP.  jpgis-dem will return a single merged geotiff for all XML within a ZIP folder.*  


