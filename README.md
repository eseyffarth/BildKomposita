# BildKomposita
Twitterbot that generates random compound words that look like BILD headlines. See [@BILD_Komposita] (https://twitter.com/BILD_Komposita) for sample output.

## How it works
The data collector collects recently published RSS items from BILD and extracts all compounds that have the pattern "Wort1-Wort2" from the item descriptions. The elements of the compounds are stored in a file on the server. When the tweeting module is executed, it loads the files and generates a random compound from the data found there.

## Why I made it
BILD compounds are weird. My linguist friends theorized that the authors put the dash in there to make the resulting words more parseable. So, theoretically, you can understand any compound as long as it contains that segment-delimiting dash? I decided to find out, by generating some nonsensical compounds. I'd say the results don't differ all that much from the original data. For a comparison with actual BILD compounds, have a look at the RSS feed that provides the data.
