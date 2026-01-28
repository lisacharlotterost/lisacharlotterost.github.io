<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="3.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:atom="http://www.w3.org/2005/Atom">
  <xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes"/>
  <xsl:template match="/">
    <html xmlns="http://www.w3.org/1999/xhtml" lang="en">
      <head>
        <title>RSS Feed - Lisa Charlotte Muth</title>
        <meta charset="utf-8" />
        <style type="text/css">
          body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background: #fff;
            color: #000;
            line-height: 1.6;
            padding: 50px 20px;
            max-width: 700px;
            margin: 0 auto;
          }
          .header {
            padding-bottom: 40px;
            margin-bottom: 50px;
          }
          h1 { 
            font-size: 1.2rem; 
            letter-spacing: 2px; 
            text-transform: uppercase; 
            margin: 0 0 10px 0;
          }
          .alert {
            background: #f9f9f9;
            padding: 20px;
            border: 1px solid #eee;
            font-size: 0.9rem;
            margin-bottom: 20px;
          }
          .item { margin-bottom: 60px; }
          .item h2 { margin: 0; font-size: 1.5rem; }
          .item h2 a { color: #000; text-decoration: none; }
          .item h2 a:hover { color: #cc0000; }
          .date { 
            font-size: 0.8rem; 
            color: #808080; 
            text-transform: uppercase; 
            letter-spacing: 1px;
            margin-bottom: 15px;
            display: block;
          }
          .content img {
            max-width: 100%;
            height: auto;
          }
        </style>
      </head>
      <body>
        <div class="header">
          <xsl:choose>
            <xsl:when test="contains(rss/channel/title, 'Notes')">
              <h1>RSS feed for Lisa's notes</h1>
              <div class="alert">
                <strong>Hi! This is an RSS feed.</strong> Subscribe to it by copying the URL of this page into an RSS reader (my favorite one is <a href="https://feedbin.com/">Feedbin</a>). Once subscribed, my latest notes will appear directly in your reader.<br/>Thanks for adding this feed!
              </div>
            </xsl:when>
            
            <xsl:otherwise>
              <h1>RSS feed for Lisa's articles, projects, talks, etc.</h1>
              <div class="alert">
                <strong>Hi! This is an RSS feed.</strong> Subscribe to it by copying the URL of this page into an RSS reader (my favorite one is <a href="https://feedbin.com/">Feedbin</a>). Once subscribed, my latest articles, projects, and talks will appear directly in your reader.<br/>Thanks for adding this feed!
              </div>
            </xsl:otherwise>
          </xsl:choose>
          <p>Here are the latest posts:</p>
        </div>
        <xsl:for-each select="rss/channel/item">
          <div class="item">
            <span class="date"><xsl:value-of select="pubDate"/></span>
            <h2><a href="{link}"><xsl:value-of select="title"/></a></h2>
            <div class="content">
              <xsl:value-of select="description" disable-output-escaping="yes" />
            </div>
          </div>
        </xsl:for-each>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
