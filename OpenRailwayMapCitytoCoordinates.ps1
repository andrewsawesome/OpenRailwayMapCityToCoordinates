Install-Module -Name OSMGeocode -ErrorAction SilentlyContinue
Import-Module OSMGeocode
$city= [PSCustomObject]@{
"postalcode" = 0
}

$city.postalcode = Read-Host "What is the postal code of the city?"

$results=($($city | Invoke-OSM -Email "a@c.com" -ResultsLanguage "en"))
$lat=$results.lat
$lon=$results.lon

Start-Process "https://openrailwaymap.app/#view=12.17/$lat/$lon"