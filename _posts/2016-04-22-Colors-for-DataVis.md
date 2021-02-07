---
layout: post
title: Your Friendly Guide to Colors in Data visualization
image: /pic/160423-colorguide-f.png
categories: [article]
summary: The original version of my guide to color tools. I published an updated version in 2019.
permalink: /:year/:month/:day/:title/
---

*Edit:* This post got [translated into Japanese](http://lab.sugimototatsuo.com/2016/05/colors-for-datavis/). I also published an updated version of this blogpost in 2018 for Datawrapper. [Find it here](https://blog.datawrapper.de/colorguide/).

A few days ago, I approached my Twitter followers with [a request to help me](https://twitter.com/lisacrost/status/722948084703956992) in an urgent matter: "Can somebody tell me how to get better with color?," I wrote. " My color decisions are awful." Thanks to a retweet by Scott Murray I got a lot of replies with links to websites and tools. They were awesome. And I want to share them with you, annotated with my own thoughts about them. Here you go:


## Why color?

First, watch this **[video](https://www.youtube.com/watch?v=Qj1FK8n7WgY&feature=youtu.be)** about why color decisions are important and how to mix colors. I'll sum up the main reasons to use colors here: Color is important because (a) it lets you set the mood and (b) color lets you guide the viewer's eye, draw attention to something and therefore tell a story.

[![image](/pic/16023_video.png)](https://www.youtube.com/watch?v=Qj1FK8n7WgY&feature=youtu.be)

Both aspects are important for data visualizations. For example, the **mood** is set very nicely in Pitch Interactive's ["Out of Sight, Out of Mind"](http://drones.pitchinteractive.com/"). The red drops make you almost see the blood spread. And color in data vis is often used to set **highlights**, a very important tool to guide the viever's eye. I often told my students "Grey is your best friend in data vis", referring to that [great article by Andy Kirk](http://www.visualisingdata.com/2015/01/make-grey-best-friend/).  

![image](/pic/160423-mood.png)

So how should you choose colors for your project? I think in data vis, there are two challenges regarding color: **Sequential/diverging data and qualitative data.** To explain them: Sequential/diverging data is data that progresses from low to high and therefore requires gradients. Qualitative data are categories and require colors which scream: "I'm by myself and have nothing do to with all these other colors here!"

The challenges for these two use cases are different ones. If you work with **gradients**, your main concern is that the differences between your steps are high enough. Meaning, you want your reader to clearly differentiate between a light green and a ...lighter green. In the next section of this post, I will introduce tools which try to solve this problem.

When working with **qualitative data**, your mission is to find colors which go well together and attract the reader's eye. This problem is typical in graphic design circles, so tools in this area are very popular. I will mention some of them in the second part, called "Color Compositions".



## 1. Data Vis Gradients

**[ColorBrewer 2.0](http://colorbrewer2.org/)** NEEDS to be mentioned first. It's a classic. THE color tool of color tools for every ambitious data vis designer. It's not only a tool: While making your choices, it also teaches you about the best use of color in data vis. If you haven't yet, click on the question marks and read these wonderful explanations.
[![image](/pic/160423-colobrewer.png)](http://colorbrewer2.org/)

Another tool that's not only really helpful, but also makes me understand color better, is **["Colorpicker for data"](http://tristen.ca/hcl-picker/#/hlc/6/1.05/CAF270/453B52)** by Tristen Brown. Here you can not only choose gradients, but invent millions of them yourself. Don't miss the "Visualized" button at the top, to show a choropleth map of your gradient. Too bad the map is not on the same page as the color picker, but hey, better than nothing.
[![image](/pic/160423-colorpicker.png)](http://tristen.ca/hcl-picker/#/hlc/6/1.05/CAF270/453B52)
[![image](/pic/160423-colorpicker1.png)](http://tristen.ca/hcl-picker/#/hlc/6/1.05/CAF270/453B52)


Gregor Aisch's **[Chroma.js Color Scale Helper](http://gka.github.io/palettes/#diverging|c0=darkred,deeppink,lightyellow|c1=lightyellow,lightgreen,teal|steps=13|bez0=1|bez1=1|coL0=1|coL1=1)** doesn't only show you the gradients, but helps you to find the ones with the biggest difference between the steps. With showing you actual steps. This little tool is the one I use the most often. If you're interested in the background: Gregor also wrote [a nice explanation](https://vis4.net/blog/posts/mastering-multi-hued-color-scales/) of this tool.
[![image](/pic/160423-chromajs.png)](http://gka.github.io/palettes)


If you feel like you mastered all these tools and need more, **[I want hue](http://tools.medialab.sciences-po.fr/iwanthue/)** will be your choice. It promises "color for data scientists" and is actually so complicated that it offers [Tutorials](http://tools.medialab.sciences-po.fr/iwanthue/tutorial.php). Definitely not the most understandable tool for beginners and I feel it's overkill for my needs (correct me if I'm wrong). The emoticons as grades for the differentiation of the colors are a nice touch, though:  

[![image](/pic/160423-medialab1.png)](http://tools.medialab.sciences-po.fr/iwanthue/tutorial.php)
[![image](/pic/160423-medialab2.png)](http://tools.medialab.sciences-po.fr/iwanthue/tutorial.php)


<br><br>



## 2a. Color Compositions - Learn from the Masters

After covering the gradients, let's move on to Color Palettes. When I asked my question on Twitter, three people recommended me painters, so I feel like there is some demand to cover them. To be honest: I appreciate the old masters, and as a Bauhaus University alumna I see the special something you can get from Albers, Itten and Co. (As an ex Weimar resident I can also see the delight one can get from [Goethe's Theory of Color](https://en.wikipedia.org/wiki/Theory_of_Colours).) But...you know...their available colors were different. Who knows what they would have thought of with bright neon green. That said, I'm sure we can still learn a lot from their writings about color composition.

Let's start with **Josef Albers** and his "Interaction of Color" book. He had important stuff to say, [eg](https://www.brainpickings.org/2013/08/16/interaction-of-color-josef-albers-50th-anniversary/): "In visual perception a color is almost never seen as it really is — as it physically is." And his color compositions are beautiful indeed:
![image](/pic/160423-albers.png)

Another Bauhaus-Star (and the teacher of Albers at the Bauhaus): The crazy **Johannes Itten** and his book ["The Art of Color"](https://monoskop.org/images/4/46/Itten_Johannes_The_Elements_of_Color.pdf). He's most famous for his color spheres, in which he showed colors and there hues:
![image](/pic/160423-itten.png)

Of course I need to mention THE color hero: the American painter **Mark Rothko**, who is famous for his huge portraits of colors. Fun fact: Rothko famously said "If you are only moved by color relationships, you are missing the point. I am interested in expressing the big emotions". I'm not sure if I understand that, since the color relationships definitely help in expressing these big emotions:
![image](/pic/160423-rothko.png)

(Apropos Emotions: A fun book seems to be [Colorist](https://www.amazon.co.uk/Colorist-Practical-Handbook-Personal-Professional/dp/4770023235/280-9109244-2898349?ie=UTF8&qid=1184782140&ref_=sr_1_1&s=books&sr=8-1) by Shigenobu Kobayashi who works in the field of "color psychology" and tries to "demystify color aesthetics".)
![image](/pic/160423-colorist.png)

Coming slowly back to the present day: The website [ColorLisa](http://colorlisa.com/) lets you see the color palettes of artists, which is a nice idea. But the execution is so poor that I want to leave the page quickly:
[![image](/pic/160423-colorlisa.png)](http://colorlisa.com/)



## 2b. Color Compositions - Learn from the Movies

Let's move from art to a more pop-culture relevant phenomenon: Movies. Master of storytelling, this medium knows how to use color to set highlights, lead your eye, set the mood and make you feel delighted.

General color palettes with colors from movie stills can be found at
**[Film Palettes](http://film-palettes.tumblr.com/)** and especially **[Movies in Color](http://moviesincolor.com/)**. **[The Colors of Motion](http://thecolorsofmotion.com/)** has a more artistic approach and shows the colors of all frames of a movie. Not sure if that can actually be helpful, but it's definitely interesting.
[![image](/pic/160423-filmpalettes.png)](http://film-palettes.tumblr.com/)


Some dude who works especially well with colors is Wes Anderson. The **[Wes Anderson Palettes](http://wesandersonpalettes.tumblr.com/)** is kind of legendary. Inspired by this blog, there is even an [R library](https://github.com/karthik/wesanderson) for Wes Anderson Color Palettes.
[![image](/pic/160423-anderson.png)](http://wesandersonpalettes.tumblr.com/)

If you want to examine the colors of your own movie stills or other images you have, tools like **[DeGraeve](http://www.degraeve.com/color-palette/)** can help. You can upload a photo and automatically create a color palette. As you can see, this palette will turn out far less saturated than you "see" the colors.
[![image](/pic/160423-photo.png)](http://www.degraeve.com/color-palette/)

Because of that, it might be helpful to create a palette of the colors as you "see" them in photos or movie stills. An automated approach or color pickers won't help you much with that; it will always look more grey-ish than the colors appear. Bill Hart-Davidson [suggests](https://twitter.com/billhd/status/722968554673475584) to use photos of tropical fish as a basis for color palettes, and I can see how this might work very well. That said, tools like DeGraeve are definitely still helpful for art or graphic design work.


## 2c. Color Compositions - Learn from Others

There are so, so many color palette collections.
[ColorHunt](http://www.colorhunt.co/), [ColourLovers](http://www.colourlovers.com/palettes), [Coolors](https://coolors.co/browser), [LOLcolors](http://www.lolcolors.com/)
and of course [Adober Color CC](https://color.adobe.com/explore/most-popular/?time=all) are just examples for the wide range of collections that color lovers around the globe created to get their fix. If you want it especially digital and sleek, the color palette for the [Material Design by Google](https://www.google.com/design/spec/style/color.html#color-color-palette) will make you happy:
[![image](/pic/160423-google.png)](https://www.google.com/design/spec/style/color.html#color-color-palette)

But how are all thee color palettes used in practice? The color searching options from **[Designspiration](http://designspiration.net/colors/D73224,3778FA/)** and **[Dribble](https://dribbble.com/colors/e83a30?percent=30)** can answer these questions. Their biggest use case for me: You can get inspiration for additional colors which go well with your existing palette. Personally, I prefer Designspiration for that: I'm a fan of this website anyway, and it lets you not only search for one, but multiple colors.
[![image](/pic/160423-designspiration.png)](http://designspiration.net/colors/D73224,3778FA/)

It's also a great idea to get inspired in a bigger sense: Go to museums and galleries. Look at art. Look at other data visualizations. Or look at blogs from people who are enthusiastic about color, for example [The Colorist](http://www.sophianahmad.com/).
[![image](/pic/160423_colorblog.png)](http://www.sophianahmad.com/)


## 2d. Color Compositions - Create them yourself

**[Smashing Magazine](https://www.smashingmagazine.com/2016/04/web-developer-guide-color/)** provides a good introduction to create your very first color palette yourself. I especially like the idea of "creating harmonious grays" with overlaying some very raw grays with your main color. I've never thought about it, but it makes a lot of sense to make your color palette feel more harmonious.
[![image](/pic/160423-smashing.png)](https://www.smashingmagazine.com/2016/04/web-developer-guide-color/)


The Smashing Magazine introduction also make use of **[Paletton](http://paletton.com/#uid=c013t00490kRlxYaFw0g0qFqFg0w0aF)**, the more advanced version of Adobe Color CC. If you know what you're doing, this tool can help a lot:
[![image](/pic/160423-paletton.png)](http://paletton.com/#uid=c013t00490kRlxYaFw0g0qFqFg0w0aF)


## 3. Color Blindness

You found awesome colors to use? SWEET. Now make sure that they fulfill their purpose and can be distinguished by colorblind people as well! The conventional wisdom is that the difference between red and blue is hard to tell for colorblind people – but that really depends on the shades of red and blue, as you can see on the image. A browser extension like [Spectrum](https://chrome.google.com/webstore/detail/spectrum/ofclemegkcmilinpcimpjkfhjfgmhieb?hl=en) or an app like [Sim Daltonism](https://michelf.ca/projects/mac/sim-daltonism/) can simulate the colors as seen by people with different color blindnesses. There is also the [R library "viridis"](https://cran.r-project.org/web/packages/viridis/vignettes/intro-to-viridis.html), which beautiful color palettes work especially well for colorblind people.
![image](/pic/160423-colorblind.png)


## 4. Fuuuuuuun with Colors

Ok, after all that work, let's watch a **[Sesame Street Video](https://www.youtube.com/watch?v=yu44JRTIxSQ&feature=youtu.be)** by the fabulous OK GO peeps:
[![image](/pic/160423-okgo.png)](https://www.youtube.com/watch?v=yu44JRTIxSQ&feature=youtu.be)

You've done that? Ok, then let's play a game. It's called **[Color](http://color.method.ac/)** (good name) (do you know that feeling when you've heard a word for so many time that it looses its meaning..) and is a little bit more addicting than I thought it is. Your goal is to match colors. Go:
[![image](/pic/160423-game.png)](http://color.method.ac/)


Thanks to all the people who replied to my tweet and helped me discover these treats! I definitely feel more comfortable around colors now. Also, let me know if you know tools or websites that can't be missed in this blog post! Find me on [Twitter](https://twitter.com/lisacrost) or write me an email: lisacharlotterost@gmail.com
