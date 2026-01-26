---
layout: post
title: Trying to make sense of the Mapbox ecosystem
tag: datavis, maps, learning,
categories: [article]
summary: '"Mapbox and I seem to have a typical love-hate-relationship."'
image: /pic/141104_mapbox-f.png
permalink: /:year/:month/:day/:title/
comments: disabled
---

![IMAGE](/pic/141104_mapbox.jpg)

<p>I like maps. I like maps because they are the most data-dense infographics you can get (Hello, Tufte and data-ink), and because they provide the ultimate overview.&nbsp;</p>
<p>So I've been trying to get into the wonderful world of <a href="mapbox.com" target="_blank">Mapbox</a> for the last two days. And...well, Mapbox and I seem to have a typical love-hate-relationship. I tried four of the tools Mapbox offers with data about <a href="http://daten.berlin.de/datensaetze/berliner-weihnachtsm%C3%A4rkte-2014" target="_blank">Christmas Markets in Berlin</a>&nbsp;and some OpenStreetMap shapefiles from Berlin.&nbsp;It was not my intention to try all four tools. It happened because I wasn't satisfied with any of them 100%.&nbsp;</p>
<p>I started with <a href="https://www.mapbox.com/mapbox-studio/" target="_blank">Mapbox Studio</a>. It's their new flagship; it's the new thing that will replace TileMill. Well...I surrendered at some point. It took me way too long to figure out the difference between "source" and "style" (which should seem intuitive), and it seems like I can use some features only if I upload my maps to mapbox.com. Which wouldn't be a problem &ndash; if it would work. Sometimes it did work. Sometimes it didn't. Short story: I moved on to the maybe more reliable TileMill.</p>
<p>And <a href="https://www.mapbox.com/tilemill/" target="_blank">TileMill</a> is great! It's by far my most favourite tool of the four (after I got it installed through the terminal). But...well, it was not quite adjustable enough for me. I like CartoCSS, that seems nice; but I cared about tooltips, and they were...not so well adjustable? Maybe I didn't google enough.</p>

![IMAGE](/pic/141104_mapbox2.png)

<p>Anyway, so I wanted to try the "hard stuff": <a href="https://www.mapbox.com/mapbox.js/api/v2.1.4/" target="_blank">Mapbox.js</a>. For that, I needed a project key, so I uploaded my christmas market data for the third time, in the <a href="https://www.mapbox.com/mapbox.js/api/v2.1.4/" target="_blank">mapbox.com Editor</a>. Which worked fine. It was even less adjustable: I didn't understand why I shouldn't be able to change more than one marker at the same time. That seems like a incredible often-used feature...well, ok. I just want the project-key for Mapbox.js.</p>
<p><span>But Mapbox.js then was this very confusing experience, where I felt I lost all my overview: My data was online, ok, but it seemed like I could also pull csv-data directly? Same for the styles: I already styled roads and buildings on Mapbox.com &ndash; and now I would be able to overwrite this? And my markers were already in my online map...and the tooltips for them I would add in Mapbox.js?&nbsp;</span></p>
<p><span>That's where I stopped and made the graphic above. It's a very uninformed graphic. I'm not a programmer, and the only thing I've ever done with maps was building tiles for a zoomable Leaflet-map of a big infographic I designed. I also think everything could be clearer for me at my current state, if I would have have read more on the Mapbox.com website. They do have good documentations. But I thought I'd understand it&nbsp;intuitively and therefore&nbsp;tried to google&nbsp;more than doing reading in a structured way (which was weird, because surprisingly few people seem to talk about Mapbox on the web).&nbsp;</span></p>
<p><span>Well, I will continue with Mapbox. And in the end, everything will make sense. Hopefully.&nbsp;</span></p>
<p>--------</p>
<p>Btw: I got the geo coordinates for the christmas market data from <a href="www.openrefine.org" target="_blank">OpenRefine</a>&nbsp;(in connection with GoogleMaps). I reeeally like OpenRefine. After some break I rediscovered it yesterday again, and had a very good time doing so. Lots of success moments on the way; great learning experience. And I'm a big fan of <a href="http://en.wikipedia.org/wiki/Regular_expression" target="_blank">regular expressions</a> now.</p>
