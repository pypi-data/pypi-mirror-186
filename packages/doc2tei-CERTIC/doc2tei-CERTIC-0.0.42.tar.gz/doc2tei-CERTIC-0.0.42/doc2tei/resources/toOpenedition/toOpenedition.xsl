<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="2.0"
        xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
		xmlns="http://www.tei-c.org/ns/1.0"
        xmlns:tei="http://www.tei-c.org/ns/1.0"
		xmlns:xinclude="http://www.w3.org/2001/XInclude"
		xmlns:mets="http://www.loc.gov/METS/"
   		xmlns:marcrel="http://www.loc.gov/loc.terms/relators"
   		xmlns:mods="http://www.loc.gov/mods/v3"
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
  exclude-result-prefixes="office style text table draw fo xlink dc meta number svg chart  dr3d math form script config ooo ooow oooc dom xforms xsd xsi rpt of xhtml grddl officeooo tableooo drawooo calcext loext field formx css3t tei mets mods marcrel xinclude">

<!-- exclude-result-prefixes="tei"-->

<xsl:output method="xml" encoding="UTF-8" indent="no"/>

<xsl:template match="@*|node()">
  <xsl:copy>
    <xsl:apply-templates select="@*|node()"/>
  </xsl:copy>
</xsl:template>
    
<!-- traitement des éléments du teiHeader : 
• les titres avec enrichissements typographiques…
• métadonnées propres à OE
-->

<xsl:template match="tei:titleStmt">
    <titleStmt>
        <xsl:for-each select="following::tei:titlePart">
            <title type="{@type}">
                <xsl:if test="@xml:lang">
                    <xsl:copy-of select="@xml:lang"/>
                </xsl:if>
                <xsl:apply-templates/>
            </title>
        </xsl:for-each>
        <xsl:copy-of select="child::tei:author|child::tei:editor"/>
    </titleStmt>
</xsl:template>
    
<xsl:template match="tei:publicationStmt">
    <publicationStmt>
        <distributor>OpenEdition</distributor>
<!--        <xsl:apply-templates/>-->
        <xsl:if test="child::tei:date[@type='received'] !='' ">
            <xsl:copy-of select="child::tei:date[@type='received']"/>
        </xsl:if>
        <xsl:if test="child::tei:date[@type='accepted'] !='' ">
            <xsl:copy-of select="child::tei:date[@type='accepted']"/>
        </xsl:if>
        <xsl:if test="//tei:ab[@subtype='openedition']/tei:idno[@type='documentnumber'] !=''">
            <xsl:copy-of select="//tei:ab[@subtype='openedition']/tei:idno[@type='documentnumber']"/>
        </xsl:if>
<!--
        <availability>
            <licence></licence>
        </availability>
-->
    </publicationStmt>
    <sourceDesc>
        <xsl:choose>
            <xsl:when test="//tei:dim[@type='pagination'] != ''">
                <biblStruct>
                    <monogr>
                        <imprint>
                            <biblScope unit="page">
                                <xsl:value-of select="//tei:dim[@type='pagination']"/>
                            </biblScope>
                        </imprint>
                    </monogr>
                </biblStruct>
            </xsl:when>
            <xsl:otherwise>
                <p>Circé</p>
            </xsl:otherwise>
        </xsl:choose>
    </sourceDesc>
</xsl:template>
    
<xsl:template match="tei:figure">
    <figure>
        <xsl:copy-of select="@*"/>
        <xsl:copy-of select="tei:head"/>
        <xsl:copy-of select="tei:table"/>
        <xsl:copy-of select="tei:formula"/>
        <xsl:copy-of select="tei:graphic"/>
        <xsl:copy-of select="tei:figDesc"/>
        <xsl:copy-of select="tei:p"/>
    </figure>
</xsl:template>
    
<xsl:template match="tei:head[parent::tei:div[@type='bibliography']]|tei:head[parent::tei:div[@type='appendix']]"/>
    
<xsl:template match="@change"/>
<xsl:template match="tei:editorialDecl"/>
<xsl:template match="tei:ab"/>
<xsl:template match="tei:titlePage"/>
<xsl:template match="tei:sourceDesc"/>
    
</xsl:stylesheet>
