---
layout: post
title: One Chart, Nine Tools – Revisited
tag: tools, datavis
summary: 2.5 years ago I recreated the same chart with 24 different charting tools. It's time to revisit some of them.
image: /pic/180929-twitter.png
desc: Recreating the same chart with nine different charting tools.
permalink: datavistools-revisited
categories: [fav, article]
---

![image](/pic/180929-header.png)

*Disclaimer: Since November 2017 I work for [Datawrapper](http://datawrapper.de), a charting tool. Which means that I can't review any charting tool unbiased anymore. I will still try.*

2.5 years ago I wrote an article recreating the same bubble chart with 24 different charting tools: [twelve charting apps](https://lisacharlotterost.github.io/2016/05/17/one-chart-tools/) and [twelve libraries/frameworks](https://lisacharlotterost.github.io/2016/05/17/one-chart-code/). Afterward, I wrote an article for SOURCE [explaining what I had learned](https://source.opennews.org/articles/what-i-learned-recreating-one-chart-using-24-tools/) during this experiment.

During the last 2.5 years, the tool landscape changed. It's time to look at it again! I will review three fresh tools (**Infogram, Flourish, Data Illustrator**), will review three already reviewed tools freshly (**Plotly, Google Sheets, Datawrapper**) and update three other ones with better descriptions and/or GIFs (**Tableau Public, RAW, Adobe Illustrator**). Scroll to the end of this article if you're curious about my decisions what I included and excluded.

The chart I'll rebuild is the same as last time. You can find the underlying data [in this Google Spreadsheet](https://docs.google.com/spreadsheets/d/1qmOCE6RBQc2hy-vW8Kefp--LcWpgwCysmgIgARy0gDk/edit?usp=sharing).


[![image](/pic/160425_gapminder.png)](http://www.gapminder.org/tools/bubbles#_)

[![image](/pic/160426_data.png)](https://docs.google.com/spreadsheets/d/1qmOCE6RBQc2hy-vW8Kefp--LcWpgwCysmgIgARy0gDk/edit?usp=sharing)

There's also something new: **I'll embed all embeddable charts**, e.g. from Infogram, Flourish, Datawrapper, Plotly and Google Sheets. So try to hover over a chart or two. And yes, this is a heavy blog post. (I hope you're reading this on wifi.) (Sorry.)

**As last time, I will have opinions.** Keep in mind that these are utterly subjective and only about the workflow that I had when creating this specific bubble chart with this specific data. My reviews won't tell you about the experience of creating another chart type with the same tool. Or about the experience of creating the same chart with different data. Or which chart types you can create in these tools (head over to Andy Kirk's [Chartmaker Directory](http://chartmaker.visualisingdata.com/) to find out). I hope it's still useful to see these tools in action. Let's start:


## Embeddable Charts

**Infogram** I'm not sure why I missed [Infogram](https://infogram.com/) in the last blog post. Now owned by Prezi, it's a colorful tool that outputs interactive charts. What I liked (and most tools don't offer): Infogram showed me my chart and its underlying data on the same page. In general, this tool did exactly what I wanted, although I missed some options: setting the opacity and a log scale, and adding labels to my bubbles. And I couldn't assign data columns to axes: If my columns were in a different order, I would have needed to reorder them first.  

![image](/pic/180929-infogram.gif)

<div class="embed"><div class="embed-120">

<script id="infogram_0_c4720150-8a3d-4d2d-b7c3-8ecc8e42be94" title="" src="https://e.infogram.com/js/dist/embed.js?Xgi" type="text/javascript"></script><div style="padding:8px 0;font-family:Arial!important;font-size:13px!important;line-height:15px!important;text-align:center;border-top:1px solid #dadada;margin:0 30px"><br><a href="https://infogram.com" style="color:#989898!important;text-decoration:none!important;"  rel="nofollow">Infogram</a></div>

</div></div>

<br><br>
**Flourish** The [new](https://flourish.studio/2018/02/01/flourish_public_launch/) player in the tool landscape! Exciting. It's neat to see [Flourish](https://flourish.studio/) evolve. Like Infogram, Flourish did what I wanted it to do. But better than Infogram, I could assign data columns to axes (typing in the column numbers requires a bit of concentration). Flourish even gave me labels, although I couldn't get them to work well with my many bubbles. Opposite to Infogram, there wasn't a simple "make background transparent and have no margins" options, though. I had to set the margins manually.

![Flourish GIF of the process](/pic/180929-flourish.gif)

<div class="embed"><div class="embed-120">

<div class="flourish-embed" data-src="visualisation/115286" data-height="350px"></div><script src="https://public.flourish.studio/resources/embed.js"></script>

</div></div>



<br><br>
**Datawrapper** In case you missed it: I work for [Datawrapper](https://www.datawrapper.de/). They pay me. Money. With that out of the way, here's what I (personally, privately) like better in Flourish and Infogram than in Datawrapper: I get to see a chart immediately and don't need to go through 2 (!) steps of looking at my data in a table first. And both tools so far gave me good automatic tooltips, without needing to create them myself like I have to in Datawrapper. However, the data point labeling & the data-to-axis-assignment work better in this tool. Plus, the axis ticks are neither tilted nor too small.

![Datawrapper chart process as a gif](/pic/180929_Datawrapper.gif)


<div class="embed"><div class="embed-120">

<iframe id="datawrapper-chart-oJtgY" src="//datawrapper.dwcdn.net/oJtgY/1/" scrolling="no" frameborder="0" allowtransparency="true" style="width: 0; min-width: 100% !important;" height="400"></iframe><script type="text/javascript">if("undefined"==typeof window.datawrapper)window.datawrapper={};window.datawrapper["oJtgY"]={},window.datawrapper["oJtgY"].embedDeltas={"100":400,"200":400,"300":400,"400":400,"500":400,"700":400,"800":400,"900":400,"1000":400},window.datawrapper["oJtgY"].iframe=document.getElementById("datawrapper-chart-oJtgY"),window.datawrapper["oJtgY"].iframe.style.height=window.datawrapper["oJtgY"].embedDeltas[Math.min(1e3,Math.max(100*Math.floor(window.datawrapper["oJtgY"].iframe.offsetWidth/100),100))]+"px",window.addEventListener("message",function(a){if("undefined"!=typeof a.data["datawrapper-height"])for(var b in a.data["datawrapper-height"])if("oJtgY"==b)window.datawrapper["oJtgY"].iframe.style.height=a.data["datawrapper-height"][b]+"px"});</script>

</div></div>


This is how I created the same chart in Datawrapper for the last blog post, in June 2017:

![gif](/pic/160426-datawrapper.gif)


<br><br>
**Tableau Public**
What can I say - [Tableau Public](https://public.tableau.com/s/) works well for data like this. The embedded graphic is too massive to actually use it in an article, but it's one of my favorite tool for exploration. Too bad I can't save my charts in the Public version of Tableau locally: I need to upload it to the cloud. But once I do that, I can export it as a PDF and can re-use it in Adobe Illustrator...so that's neat.

![gif](/pic/180929-tableau.gif)

<div class="embed"><div class="embed-120">

<div class='tableauPlaceholder' id='viz1538251135815' style='position: relative'><noscript><a href='#'><img alt='Sheet 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;He&#47;HealthvsIncome&#47;Sheet1&#47;1_rss.png' style='border: none'/></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='HealthvsIncome&#47;Sheet1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;He&#47;HealthvsIncome&#47;Sheet1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /></object>
</div>
<script type='text/javascript'>var divElement = document.getElementById('viz1538251135815'); var vizElement = divElement.getElementsByTagName('object')[0]; vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.6)+'px'; var scriptElement = document.createElement('script'); scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js'; vizElement.parentNode.insertBefore(scriptElement, vizElement); </script>

</div></div>

<br><br>
**Plotly** I like [Plotly](https://plot.ly). It was definitely one of my favorite tools last time – <s>but last time, I was also able to let my population column resize the bubbles. Not this time. In Chrome, the site froze; in Firefox, it showed me giant bubbles which size I couldn't change.</s> Edit: Plotly fixed this error after the blogpost came out. The bubbles don't resize automatically, but at least it works. Yay! (I updated the GIF below, too.) Plotly is still close to my heart, though: It handles big-ish datasets well and can create all kinds of fancy visualizations that you'd only need as a scientist ([3D](https://plot.ly/~chris/10796)! [Heatmaps!](https://plot.ly/~DanielCarrera/13/vertical-direction-vs-radial-direction/#/)!).

![gif](/pic/180929_plotlynew.gif)

<div class="embed"><div class="embed-120">

<iframe width="100%" height="350px" frameborder="0" scrolling="no" src="//plot.ly/~lisacrost/19.embed"></iframe>

</div></div>

Below you can see how I created the same chart in Plotly for the last blog post, in April 2016. Assigning variables to the axes was better solved back then. In the new chart editor, I need to choose column header numbers, Flourish-style. Also, the old editor named my axes automatically ("income", "health"). <s>And did I mention that my bubbles sized properly back then? Good old times.</s>

![gif](/pic/160426-plotly.gif)



<br><br>
**Google Sheets** Let me quote from what I wrote about Google Sheets in my blog post back then: "[Google Sheets](https://www.google.com/sheets/about/) CAN do bubble charts, but only with a little hack – I would have needed to change my data for it." Well, they changed the editor. Bubble charts, here I come! Variable bubble sizes are possible now. I can't change the color of my bubbles to one color, but hey, who cares about color. (Irony doesn't work well online, does it.) Fun fact: Of all the chart I've embedded in this blog post, the Google Sheets chart is the only one that's interactive but not responsive.

![gif](/pic/180929_googlesheets.gif)


<div class="embed"><div class="embed-120">

<iframe width="100%" height="370px" frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTpXl5zc2MVunQejAOYnNcUiwh61OFdzwNl8j-gJrOof3sRk0u-_gdLcF5bsjv9fRDij7oGWMlvFk_Q/pubchart?oid=1840595858&amp;format=interactive"></iframe>

</div></div>

That's how I created the same chart 2.5 years ago:

![image](/pic/160426-google.gif)


## Non-embeddable Charts

**Adobe Illustrator**
Ah, [Adobe Illustrator](https://www.adobe.com/products/illustrator.html). A tool that almost every Information Designer uses for static designs, daily. Let's be precise here: The charting options in Illustrator suck. There's no way to set the circle size or a log scale, but I'd just call that limited functionality. What's really frustrating is that you can't edit the data anymore once you decide that it's time to properly design the chart.

![image](/pic/180929_illustrator.gif)
![image](/pic/160426_illustrator.png)

<br><br>
**Data Illustrator** There's hope coming out of Adobe! It's a bit weird, though: In October 2017, Bernard Kerr from Adobe [showed off](http://www.visualisingdata.com/2017/10/adobe-sneak-peak-project-lincoln/) a new [Lyra](http://idl.cs.washington.edu/projects/lyra/)-like tool he had been working on, "Lincoln". Seven months later, researchers from Adobe and the Georgia Institute of Technology came out with [Data Illustrator](http://data-illustrator.com/). It has nothing to do with Lincoln and works almost the same: One also binds data (variables) directly to geometries. That takes some time to get used to, but I'm a big fan of the concept. The output of Data Illustrator are SVGs – perfect to keep going in Adobe Illustrator.

![Data Illustrator GIF of the process](/pic/180929_dataillustrator.gif)

![Data Illustrator chart](/pic/180929_dataillustrator.png)

By the way, this is how I create the same chart in [**Lyra**](http://idl.cs.washington.edu/projects/lyra/), a tool from 2014. The creation process feels more intuitive than Data Illustrator, but maybe that's just the case for this very bubble chart. If you're interested in these data-drawing tools, [Maarten Lambrechts links to four of them here](https://twitter.com/maartenzam/status/1052124132115173377).

![gif](/pic/160426_lyra.gif)


<br><br>
**RAW by DensityDesign**
I'd call [RAW](https://rawgraphs.io/) a super-easy-to-use extension for Adobe Illustrator: You can export fancy charts as SVG or PDF and then tweak them in Illustrator. RAW even has the option to change the size of the bubbles. Alas, no log scale. And if you just want a simple line or bar chart, RAW doesn't have you covered.
![gif](/pic/160426-raw.gif)
[![image](/pic/160426_raw.png)](http://app.raw.densitydesign.org/)



## Outtakes

Like this entire review, my selection is massively biased and subjective. In general, I focus on drag&drop charting apps with the goal of presentation, not analysis. But when I wrote the [predecessor of this blog post](https://lisacharlotterost.github.io/2016/05/17/one-chart-tools/) 2.5 years ago, I reviewed seven more tools. Why did I not update my reviews for them? Here's why:

- **Lyra**: I'm still 😍 about this tool, but nobody uses it and it hasn't changed. I talk about it in the review of Data Illustrator.
- **HighCharts Cloud**: I've tried it shortly. It changed, but it's still as bad as back then. I gave up after 3 minutes of trying to get it to show me...anything, really.
- **Excel**: I don't have access to this tool anymore. I assume it's very similar to [2.5 years ago](https://lisacharlotterost.github.io/2016/05/17/one-chart-tools/), but I'm happy to be proven wrong. If you're an Excel fan, please do so!
- **Easycharts**: Doesn't seem to have an online version anymore.
- **Quadrigram**: I don't see anyone use or mention it anymore.
- **Nodebox**: Also didn't catch on / too niche.
- **PoleStar, now Voyager 2**: I would have loved to cover this open source tool again. Sadly, the peeps at the [University of Washington Interactive Data Lab](http://idl.cs.washington.edu/) decided to discontinue developing it. Instead, they included the remains of PoleStar in the new [Voyager 2](https://vega.github.io/voyager2/) and [called](https://github.com/vega/voyager) it a "data exploration tool that blends manual and automated chart specification." Which is exciting for data exploration! But with the new tool, you can't change anything slightly design-related – which makes it far less interesting for this blog post.

<br>
That’s it! Did I make a mistake or missed an important app? Let me know on [Twitter: @lisacrost](https://twitter.com/lisacrost) or via email: [lisacharlotterost@gmail.com](mailto:lisacharlotterost@gmail.com).
