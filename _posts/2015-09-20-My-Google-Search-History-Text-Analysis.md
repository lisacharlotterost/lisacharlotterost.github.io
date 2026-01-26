---
layout: post
title: My Google Search History – Text Analysis in R
tag: dayproject, datavis, google
categories: [article]
summary:
image: /pic/150920_table-f.png
permalink: /:year/:month/:day/:title/
comments: disabled
---

Text analysis! That's where the fun begins in R. That's where we go more and more away from "Excel could do that, too", to "Woah, I didn't know that is only a matter of a few lines of code." For that magic, you need to install the [tm](https://cran.r-project.org/web/packages/tm/index.html) (="text mining") library in R. And then we can do awesome stuff, like removing the whitespace of your text in one line. Or removing punctuation. Or removing the most common words in English, called "stopwords": "the", "a", "such", "those", "doing", etc. And that's only the beginning.

There are lots of [great](https://rpubs.com/lmullen/nlp-chapter) [text mining](https://eight2late.wordpress.com/2015/05/27/a-gentle-introduction-to-text-mining-using-r/) [tutorials](https://deltadna.com/blog/text-mining-in-r-for-term-frequency/) out there, so I won't get into code details here. What I did was removing stopwords and then writing a csv with all the words and their number of occurrences. I then sorted this table a little bit (by hand instead of with [Named Entity Recognition](https://en.wikipedia.org/wiki/Named-entity_recognition) libraries like [OpenNLP](https://opennlp.apache.org/)) and came to this result:  

![image](/pic/150920_table.png)

Because I haven't exported such a list of most searched for terms in [the main visual analysis of my Google Search history](http://lisacharlotterost.github.io/2015/06/20/Searching-through-the-years/), some interpretation might be necessary: In the list of all the most common queries, locations are definitely the most dominant ones. Which makes sense, because **that's what I use Google most often for: searching for directions.** That's why "Germany" (705 times) is so high in this list, too – not because I'm googling for my home country so often, but because it sometimes appears in a query for directions (especially an auto-completed query).

No surprises in the **list of location** queries: Places I've lived in (Berlin, New York, Weimar) at the top; places of vacations and travelling (Hamburg, Lisbon, Cuba) at the bottom.

**List of brands:** I'm as shocked as you that "Wordpress" (146) is so high in this list – it results from being a co-organizer of a conference last year and using Wordpress to set up our website for that. "Windows" (142) before "Mac" (134) makes sense, too: I was using a Windows OS until last summer. Wait for a few more months and the "mac" count will certainly overtake the "windows" count. And I need to smile about "iphone" (120) being before "android" (118): I have owned, but I've never used an iPhone. Or an "iPad" (47). Or a "Nexus" (44).

The **list of concepts** is to show how poetic Google Search queries can be – at least on the surface. In half of the queries for "information" (177) I was searching for "information design" (85). When I google for "free" (125), I search for "freemason lodge" (in 2011), "freemium examples" (2012) or even "sainsbury rooibos tea naturally caffeine free dragonfly organic" (in 2010. I have no idea what happened there). But of course, mostly I search for "tumblr free grid themes", "dollar bill vector free" or "screenshot programm freeware". And when I google for "time" (161), I don't want to get into the philosophical and physical discussion if time exists, and if, how so – I just want to know which time it is currently in San Francisco.

The World Wide Web: Full of information humankind has gathered in thousands of years; full of information I could use to gain incredible knowledge. And I ask the gatekeeper (aka Google) for free templates and rooibos tea. Which, you know, has its legitimation, too.
