<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="2.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0"
  xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0"
  xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0"
  xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0"
  xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0"
  xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0"
  xmlns:xlink="http://www.w3.org/1999/xlink"
  xmlns:dc="http://purl.org/dc/elements/1.1/"
  xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0"
  xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0"
  xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" 
  xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" 
  xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" 
  xmlns:math="http://www.w3.org/1998/Math/MathML" 
  xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" 
  xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" 
  xmlns:config="urn:oasis:names:tc:opendocument:xmlns:config:1.0" 
  xmlns:ooo="http://openoffice.org/2004/office" 
  xmlns:ooow="http://openoffice.org/2004/writer" 
  xmlns:oooc="http://openoffice.org/2004/calc" 
  xmlns:dom="http://www.w3.org/2001/xml-events" 
  xmlns:xforms="http://www.w3.org/2002/xforms" 
  xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
  xmlns:rpt="http://openoffice.org/2005/report" 
  xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" 
  xmlns:xhtml="http://www.w3.org/1999/xhtml" 
  xmlns:grddl="http://www.w3.org/2003/g/data-view#" 
  xmlns:officeooo="http://openoffice.org/2009/office" 
  xmlns:tableooo="http://openoffice.org/2009/table" 
  xmlns:drawooo="http://openoffice.org/2010/draw" 
  xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" 
  xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" 
  xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" 
  xmlns:formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0" 
  xmlns:css3t="http://www.w3.org/TR/css3-text/"
  xmlns="http://www.tei-c.org/ns/1.0"
  exclude-result-prefixes="#all">
    
<xsl:output method="xml" encoding="UTF-8" indent="no"/>
    
<xsl:template match="text:h">
    <xsl:choose>
        <xsl:when test="@subtype='review'">
            <listBibl><xsl:apply-templates select="." mode="review"/></listBibl>
        </xsl:when>
        <xsl:otherwise>
            <head>
                <xsl:copy-of select="@rendition"/>
                <xsl:apply-templates/>
            </head>
        </xsl:otherwise>
    </xsl:choose>
</xsl:template>
    
<xsl:template match="text:p[@text:style-name='Standard']|text:p[@text:style-name='Normal']">
    <xsl:choose>
        <!-- image block simple (pas de titre, légende, crédits) -->
        <xsl:when test="child::draw:frame and not(child::text()) and not(parent::*:figure)">
            <figure><xsl:apply-templates/></figure>
        </xsl:when>
        <!-- image block complexe (suppression du paragraphe Normal englobant) -->
        <xsl:when test="child::draw:frame and not(child::text()) and parent::*:figure">
            <xsl:apply-templates/>
        </xsl:when>
        <xsl:when test="parent::table:table-cell"/>
        <xsl:otherwise>
            <p>
                <xsl:copy-of select="@rendition|@xml:lang"/>
                <xsl:apply-templates/>
            </p>
        </xsl:otherwise>
    </xsl:choose>
</xsl:template>
    
<xsl:template match="text:p[@text:style-name='TEI_paragraph_break']">
    <p rend="break">
        <xsl:copy-of select="@rendition"/>
        <xsl:apply-templates/>
    </p>
</xsl:template>
    
<xsl:template match="text:p[@text:style-name='TEI_paragraph_consecutive']">
    <p rend="consecutive">
        <xsl:copy-of select="@rendition"/>
        <xsl:apply-templates/>
    </p>
</xsl:template>
    
<xsl:template match="*:div">
  <div>
    <xsl:copy-of select="@*"/>  
    <xsl:apply-templates/>
  </div>
</xsl:template>

<!-- ### floatingText ### -->
<xsl:template match="*:floatingText">
  <floatingText>
    <xsl:copy-of select="@*"/> 
      <body>
        <xsl:apply-templates/>
      </body>
  </floatingText>
</xsl:template>
    
<xsl:template match="text:p[@text:style-name='TEI_floatingText_title']">
    <head>
        <xsl:copy-of select="@* except(@text:style-name)"/> 
        <xsl:apply-templates/>
    </head>
</xsl:template>
    
</xsl:stylesheet>