---
title: "How I love my code of many colours"
categories:
  - Blog
excerpt: "With apologies to Andrew Lloyd Webber, an article on the topic of syntax highlighting. Does colour help in the creative process, and if so why isn't there more?"
custom_css:
  - darknav
  - decorations
toc: true
toc_sticky: true
toc_label: "&nbsp;&nbsp;Contents"
toc_icon: "palette"
---

A close look at syntax highlighting, and what you can do to get the most from it.
*N.B.* Image attributions can be found at the [end of the article](#image-attributions)
{: .notice--primary}

![Colourful textiles](/assets/images/posts/syntax/textiles.jpg){: .align-center .framed .poem-banner-top}

*Walls of tinted text  
An ASCII kaleidoscope  
Defining my world*
{: .poem}

![Colourful textiles](/assets/images/posts/syntax/textiles_inv.jpg){: .align-center .framed .poem-banner-bottom}



# About syntax highlighting

[Syntax highlighting](https://en.wikipedia.org/wiki/Syntax_highlighting) is one of those phenomena that becomes more of a puzzle the more you think about it. *(If you're unfamiliar with the term, it means* ***automatic formatting*** *of text based on its content –  programmers like their code to show in colour to make it easier to read and write)*.

[![Syntax highlighting](/assets/images/posts/syntax/highlighting.png){: .align-center .framed}](/assets/images/posts/syntax/highlighting.png)
1\. &nbsp; unhighlighted / highlighted renderings of text in an editor
{: .caption}

I mean, this feature is everywhere. But where did it come from? How did it grow to be so indispensable? Why do we obsess about colour in source code but not elsewhere? Are we even doing it right for plaintext? If so, why are there so many variations?

After reading around I am still unsatisfied, so I've decided to explore the topic myself and see what answers emerge. In this article I will:
1. Cover some background and unpack why this topic interests me.
2. Examine the problem from a theoretical perspective.
3. Share some resources and practical help for using highlighters.
4. Finish with my wish-list for further use of colour.

If you're intrigued like I have been, then read on...


# Background

## Communicating with colour
Though ubiquitous in programming, syntax highlighting is far less common in other areas. Probably the next best examples are links ([www.bayesiansaddles.com](https://www.bayesiansaddles.com)), or those squiggly lines you get under <span class="spelling text-error">misspeled</span> words. The idea is that the differences in formatting convey some important information.

Unfortunately, we've waded straight into hot water with this premise. Since syntax highlighting is dependent on the text, it is technically *redundant*. Nothing new is communicated. All the information contained in formatting is already in the text itself; the colours just emphasize something we should already know: the language we're using.

Ah, but some people need a little help with that.

## A learning aid
Indeed, the [first](https://patents.google.com/patent/US4617643A/en) syntax highlighter (written for BASIC in 1982) was intended as an aid for beginners, especially children. Novices *don't* fully know the language, so the colour is genuinely informative to them. This approach underpins the design of Scratch, a language used since 2007 for teaching kids to program.

[![Scratch programming language for kids](/assets/images/posts/syntax/scratch.png){: .align-center .framed style="width: 50%;"}](/assets/images/posts/syntax/scratch.png)
2\. &nbsp; the scratch language
{: .caption}

Analogously, music is often taught in colour so the pitches can more easily be distinguished. We're not just talking about babies' xylophones here: in recent years an effort has been made to standardize on a scheme called [ChromaNotes™](http://chroma-notes.com/), linking music notation to a cyclic spectrum of colour. This helps fledgling musicians as they learn to read the stave, no matter what instrument they play.

[![ChromaNotes system for associating colour with pitch](/assets/images/posts/syntax/chromanotes.png){: .align-center .framed style="width: 60%;"}](/assets/images/posts/syntax/chromanotes.png)
3\. &nbsp; the chromanotes™ system of colour–pitch correspondence
{: .caption}

Some instruments also incorporate the colours by design:

[![Boomwhackers, a colourful musical instrument](/assets/images/posts/syntax/boomwhackers.jpg){: .align-center .framed style="width: 60%;"}](/assets/images/posts/syntax/boomwhackers.jpg)
4\. &nbsp; "boomwhackers" – an instrument coloured using the system.
{: .caption}

There is evidence to support the use of colour in both [music](https://en.wikipedia.org/wiki/Colored_music_notation) and [programming](https://www.researchgate.net/publication/293652017_The_impact_of_syntax_colouring_on_program_comprehension), showing that beginners do read with colour more fluently and make fewer mistakes compared to reading without it. The same is true for spellchecking. But among professional musicians the world is notably monochrome – while programming remains as colourful as ever. Why these differences?

## Power users
In a field that usually likes to see things reduced to the bare bones, this is a notable affectation. And it's not as if there's a standard, either. Even if everyone on a team uses the same editor, font, and style conventions (rare given the choice), you might see them each using different colour palettes to suit individual preferences. And, yes, there are some who [eschew highlighting altogether](https://www.robertmelton.com/posts/syntax-highlighting-off/). But most programmers do work in colour, not least because editing software tends to highlight by default.

It's easy to answer why trained musicians *aren't* drowning in rainbows. But what about the opposite question: why is programming so colourful even among elites?

[![Sheet music for Rossini's Cat Duet](/assets/images/posts/syntax/sheet_music.png){: .align-center .framed style="width: 60%;"}](/assets/images/posts/syntax/sheet_music.png)
5\. &nbsp; sheet music, typically devoid of colour
{: .caption}

I think there's an argument by kinetics here:

$$ \frac{\mathrm{d} (\text{number of users})}{\mathrm{d} t} \;=\; \text{adoption rate} - \text{abandonment rate}.$$

If the adoption rate is high and the abandonment rate is low, then the number of users will increase. It doesn't matter why – it just happens. There are some basic facts about the tech community and about syntax highlighting as a tool that make it 'inevitably ubiquitous':

The **adoption rate** is high, because...
- Programmers like to experiment with new tools.
- They are especially likely to try easy tools.
  - Syntax highlighting is one of the easiest tools to use.
  - It integrates simply and unobtrusively in editors.
  - It comes as a user-controlled option, enabled by default.

The **abandonment rate** is low, because...
- If a tool is not a nuisance, there is no reason to abandon it.
  - There is no effort to using syntax highlighting.
  - The visual appearance is adaptable to a user's taste.
  - Highlighters are ultra-lean, consuming minimal resources.
- People become emotionally invested in things they choose.
  - Programmers can customize colouring rather than disabling it.
  - Once they do so, there is a stronger relationship to the feature.
  - Users who feel strongly will evangelize to the ones who don't.

Much like keeping a low-maintenance indoor plant, syntax highlighting is so simple, so visible, and so harmless that it's inescapably popular. It is a highly successful meme. But is it more than this?

[![Succulent plants](/assets/images/posts/syntax/succulents.jpg){: .align-center .framed style="width: 75%;"}](/assets/images/posts/syntax/succulents.jpg)
6\. &nbsp; syntax highlighters: the succulents of the tech world
{: .caption}

## The greater good
Notice how I haven't yet said anything about the merits of syntax highlighting. Don't worry, I'm not so cynical that I think they don't exist! If nothing else, colour is beautiful, and who am I to deny self-expression?

So, in the next section I'll explore the potential of colour to benefit programmers of all experience levels. Here, then, is the case for syntax highlighting being more than "just a meme".


# Theory

## Perception and understanding
What happens when you read text?

## A primer on vision
The human eye, in most people, uses four types of light-sensitive cell to see. Three of these are **cones**, dominating the centre of our vision. The remaining type, rods, are scattered throughout our peripheral vision with lower resolution but higher sensitivity. Each type of cell also responds differently to light at different wavelengths:

[![Human vision cell responses](/assets/images/posts/syntax/vision.png){: .align-center .framed style="width: 80%;"}](/assets/images/posts/syntax/vision.png)
7\. &nbsp; response spectra of human rod **r** and cone **s m l** cells
{: .caption}

The different responses allow for colour vision, since the brain can interpret any particular combination of responses as a colour. In the plot below, invisible parts of the spectrum – beyond ultraviolet or infrared – are at the origin; as light of increasing wavelength is detected, the three cone cells respond in amounts that trace out a curve through 3D space.

[![Spectrum locus in LMS space](/assets/images/posts/syntax/lms.png){: .align-center .framed style="width: 80%;"}](/assets/images/posts/syntax/lms.png)
8\. &nbsp; locus of the visible spectrum in cone cell response coordinates
{: .caption}

Mixing pure spectral colours lands you anywhere in the shaded volume.
<span style="border-radius:0.25em;border-style:solid;border-color:#ff00ff;background-color:#ff00ff;color:white;padding:1px;">Magenta</span>
is here, as are desaturated colours all the way down to
<span style="border-radius:0.25em;border-style:solid;border-color:#999999;background-color:#999999;color:white;padding:1px;">greys</span>.
Greater light intensity distorts the volume away from the origin, and
<span style="border-radius:0.25em;border-style:solid;border-color:#bbbbbb;color:#888888;padding:1px;">white</span>
is the perceived colour when all responses are 'maximum'. *N.B. this is a loose definition of white, with several layers of complexity not addressed. Think of it as a relative maximum, not an absolute one.*

To understand our perception of colour better, the coordinates are usually transformed from $$(L,M,S)$$ to $$(l, m, M)$$, where lowercase letters mean proportions of the total response. And a 'standard observer' uses mathematical versions of $$L$$, $$M$$, and $$S$$, denoted $$X$$, $$Y$$ and $$Z$$. So the resulting colour space is called **xyY**.

<video class="align-center" width="50%" autoplay loop muted style="margin-bottom:0.5em;">
    <source src="/assets/images/posts/syntax/xyY.webm" type="video/webm"></source>
    Sorry, your browser does not support video elements.
</video>
9\. &nbsp; xyY color space
{: .caption}

[![xyY color space](/assets/images/posts/syntax/xyY.png){: .align-center .framed style="width: 25%;"}](/assets/images/posts/syntax/xyY.png)
10\. &nbsp; a slice at constant Y
{: .caption}

In this space, white is at $$(\frac{1}{3}, \frac{1}{3}, 100)$$. $$Y$$ is not just any approximation to $$M$$: it is the *luminance*. So darker colours have smaller $$Y$$, with black at $$Y=0$$.

This is a

[![L\*u\*v\* colour space](/assets/images/posts/syntax/Luv.png){: .align-center .framed style="width: 25%;"}](/assets/images/posts/syntax/Luv.png)
11\. &nbsp; a slice of the L\*u\*v\* color space at constant L\*
{: .caption}

## Text in higher dimensions

## Extremes


# Practice
Brunel

## Regular Expressions

## Abstract Syntax Trees


# Growing in colour

## Prose
Colour is clearly a valuable cognitive tool. I have a feeling that it can be used more widely and to greater effect – but to understand how, we first need to sift through quite the mess of theory, opinion, and evidence...

## Dear synaesthetes...

<br /><br /><br /><br />

# Image attributions
(see [terms of use](/faq/#using-my-content))

**Banners.** *(Modified from [original by kesie91](https://pixabay.com/photos/textile-color-colorful-fabric-548716/) under [Pixabay license](https://pixabay.com/service/license/)):*

<span style="color:#b0b0bb">**\>**</span>&nbsp;&nbsp;*Derivative work [<span rel="http://purl.org/dc/terms/title">Colourful fabric 1</span>](/assets/images/posts/syntax/textiles.jpg){: rel="http://creativecommons.org/ns#attributionURL"} by [<span rel="http://creativecommons.org/ns#attributionName">William Fletcher</span>](/){: rel="http://creativecommons.org/ns#attributionURL"}, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0)*
{: .license-text style="margin-top:-1em;"}

<span style="color:#b0b0bb">**\>**</span>&nbsp;&nbsp;*Derivative work [<span rel="http://purl.org/dc/terms/title">Colourful fabric 2</span>](/assets/images/posts/syntax/textiles_inv.jpg){: rel="http://creativecommons.org/ns#attributionURL"} by [<span rel="http://creativecommons.org/ns#attributionName">William Fletcher</span>](/){: rel="http://creativecommons.org/ns#attributionURL"}, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0)*
{: .license-text style="margin-top:-1em;"}

**1\.** *Original work [<span rel="http://purl.org/dc/terms/title">Syntax highlighting</span>](/assets/images/posts/syntax/highlighting.png){: rel="http://creativecommons.org/ns#attributionURL"} by [<span rel="http://creativecommons.org/ns#attributionName">William Fletcher</span>](/){: rel="http://creativecommons.org/ns#attributionURL"}, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0)*
{: .license-text}

**2\.** *Modified from [original by Lubaochuan](https://commons.wikimedia.org/wiki/File:Draw_triangle.png) under [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0)*

**3\.** *Original work [<span rel="http://purl.org/dc/terms/title">Coloured C major scale</span>](/assets/images/posts/syntax/chromanotes.png){: rel="http://creativecommons.org/ns#attributionURL"} by [<span rel="http://creativecommons.org/ns#attributionName">William Fletcher</span>](/){: rel="http://creativecommons.org/ns#attributionURL"}, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0) made using this Python script and the [abjad](https://abjad.github.io/) library:*
{: .license-text}

```python
import abjad

colors = [abjad.SchemeColor(x) for x in
    ('red',
     'DarkOrange',
     'gold',
     'GreenYellow',
     'CadetBlue',
     'SlateBlue',
     'magenta')
]
pitches = [[x] for x in [0,2,4,5,7,9,11]]
color_map = abjad.ColorMap(colors=colors, pitch_iterables=pitches)

QUARTER = abjad.Duration(1,4)
notes = [abjad.Note(x, QUARTER) for x in [0,2,4,5,7,9,11,12]]
staff = abjad.Staff(notes)
abjad.label(staff).color_note_heads(color_map)

abjad.show(staff)
```
{: .align-center style="font-size: 60%; width: 90%; margin-bottom: 2em;"}

**4\.** *Product info [here](https://boomwhackers.com). Image obtained from [this listing](https://www.thomann.de/gb/boomwhackers_bw_xts_boomophone.htm)*

**5\.** *Rossini's cat duet, [score by Dean Shannon](https://commons.wikimedia.org/wiki/File:Duetto_buffo_di_due_gatti_sheet_music_(Page_3).png) reproduced under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0)*

**6\.** *[Photo by Ylanite Koppens](https://www.pexels.com/photo/five-succulent-plants-1906439/) shared under [Pexels license](https://www.pexels.com/license/)*

**7\.** *Modified from [original plot by Bhutajata](https://commons.wikimedia.org/wiki/File:Normalized_response_spectra_of_human_cones.png) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0).
Derivative work [<span rel="http://purl.org/dc/terms/title">Vision cell responses</span>](/assets/images/posts/syntax/vision.png){: rel="http://creativecommons.org/ns#attributionURL"} by [<span rel="http://creativecommons.org/ns#attributionName">William Fletcher</span>](/){: rel="http://creativecommons.org/ns#attributionURL"}, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)*
{: .license-text}

**8\.** *Modified from [original plot by Maneesh](https://commons.wikimedia.org/wiki/File:3D_Graph_of_LMS_Color_Space.png) under [CC0 1.0](http://creativecommons.org/publicdomain/zero/1.0/).
Derivative work [<span rel="http://purl.org/dc/terms/title">LMS spectrum locus</span>](/assets/images/posts/syntax/lms.png){: rel="http://creativecommons.org/ns#attributionURL"} by [<span rel="http://creativecommons.org/ns#attributionName">William Fletcher</span>](/){: rel="http://creativecommons.org/ns#attributionURL"}, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0)*
{: .license-text}
