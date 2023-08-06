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
    
<xsl:template match="text:p[starts-with(@text:style-name,'TEI_quote')]">
    <xsl:variable name="quoteType" select="@text:style-name"/>
    <xsl:choose>
        <xsl:when test="preceding-sibling::*[1][local-name()='cit']">
        <xsl:comment>suppression de la quote de traduction déjà rappatriée dans l'élément cit</xsl:comment></xsl:when>
        <xsl:otherwise>
            <quote>
                <xsl:copy-of select="@xml:lang"/>
                <xsl:if test="$quoteType='TEI_quote2'">
                    <xsl:attribute name="type">quotation2</xsl:attribute>
                </xsl:if>
                <xsl:apply-templates/>
             </quote>
        </xsl:otherwise>
    </xsl:choose>    
</xsl:template>

<xsl:template match="text:p[@text:style-name='TEI_bibl_citation']">
    <bibl><xsl:apply-templates/></bibl>
</xsl:template>

<!--
<xsl:template match="text:p[@text:style-name='TEI_quote_continuation']" mode="inCit">
    <xsl:for-each-group select="node()" group-ending-with="text:line-break">
        <quote>
            <xsl:apply-templates select="current-group()"/>
        </quote>
    </xsl:for-each-group>
    <xsl:if test="following-sibling::text:*[1][@text:style-name='TEI_bibl_citation']">
        <xsl:apply-templates select="following-sibling::text:*[1][@text:style-name='TEI_bibl_citation']" mode="inCit"/>
    </xsl:if>
</xsl:template>
    
<xsl:template match="text:p[@text:style-name='TEI_bibl_citation']"/>
<xsl:template match="text:p[@text:style-name='TEI_quote_nested']"/>
<xsl:template match="text:p[@text:style-name='TEI_quote_continuation']"/>
    
-->
    
<!--
<xsl:template match="text:p[starts-with(@text:style-name,'TEI_quote')]" mode="inCit">
    <quote>
        <xsl:attribute name="xml:lang" select="substring-after(@text:style-name,':')"/>
        <xsl:apply-templates/>
    </quote>
</xsl:template>
    
<xsl:template match="text:p[starts-with(@text:style-name,'TEI_quote:')]">*</xsl:template>
-->

<xsl:template match="text:span[@text:style-name='TEI_quote-inline']">
    <cit><quote><xsl:copy-of select="@xml:lang"/><xsl:apply-templates/></quote></cit>
</xsl:template>
    
<xsl:template match="text:p[starts-with(@text:style-name,'TEI_epigraph')][parent::*:div]">
    <epigraph>
        <cit>
            <quote><xsl:apply-templates/></quote>
            <xsl:if test="following-sibling::text:*[1][@text:style-name='TEI_bibl_citation']">
                <xsl:apply-templates select="following-sibling::text:*[1][@text:style-name='TEI_bibl_citation']" mode="inCit"/>
            </xsl:if>
        </cit>
    </epigraph>
</xsl:template>
    
<xsl:template match="text:p[@text:style-name='TEI_verse']">
    <lg>
        <xsl:copy-of select="@rendition"/>
        <xsl:for-each-group select="node()" group-ending-with="text:line-break">            <l>
            <xsl:variable name="lineNum" select="."/>
                <xsl:if test="$lineNum/local-name()='span' and $lineNum/@text:style-name='TEI_versenumber-inline'">
                    <xsl:attribute name="n">
                        <xsl:analyze-string select="." regex="(\d+)">
                            <xsl:matching-substring><xsl:value-of select="."/></xsl:matching-substring>
                            <xsl:non-matching-substring></xsl:non-matching-substring>
                        </xsl:analyze-string>
                    </xsl:attribute>
                </xsl:if>
                <xsl:apply-templates select="current-group()"/>
            </l>
        </xsl:for-each-group>
    </lg>
</xsl:template>
    
<xsl:template match="text:span[@text:style-name='TEI_versenumber-inline']">
    <num><xsl:apply-templates/></num>
</xsl:template>
    
<xsl:template match="text:tab">
    <xsl:choose>
        <xsl:when test="parent::text:p[@text:style-name='TEI_verse']">
            <caesura/>
        </xsl:when>
        <xsl:otherwise/>
    </xsl:choose>
</xsl:template>
    
<!-- ## entretien ## -->
<xsl:template match="text:p[@text:style-name='TEI_question']|text:p[@text:style-name='TEI_answer']">
    <p><xsl:apply-templates/></p>
</xsl:template>

<xsl:template match="text:p[@text:style-name='TEI_speaker']">
    <speaker><xsl:apply-templates/></speaker>
</xsl:template>
    
<xsl:template match="text:span[@text:style-name='TEI_speaker-inline']">
    <name type="speaker"><xsl:apply-templates/></name>
</xsl:template>
    
<!-- ## théâtre ## -->
<xsl:template match="text:p[@text:style-name='TEI_didascaly']|text:span[@text:style-name='TEI_didascaly-inline']">
	<stage>
		<xsl:apply-templates/>
	</stage>
</xsl:template>

<xsl:template match="text:p[@text:style-name='TEI_replica']">
<!--	<p><xsl:apply-templates/></p>-->
    <xsl:for-each-group select="node()" group-ending-with="text:line-break">
        <p>
            <xsl:apply-templates select="current-group()"/>
        </p>
    </xsl:for-each-group>
</xsl:template>

<xsl:template match="text:p[@text:style-name='TEI_versifiedreplica']">
<!--    <l><xsl:apply-templates/></l>-->
    <xsl:for-each-group select="node()" group-ending-with="text:line-break">
        <l>
            <xsl:apply-templates select="current-group()"/>
        </l>
    </xsl:for-each-group>
</xsl:template>
    
</xsl:stylesheet>