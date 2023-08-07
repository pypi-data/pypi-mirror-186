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
  exclude-result-prefixes="">
    
<xsl:template match="text:p[@text:style-name='TEI_quote']|text:p[@text:style-name='TEI_quote2']">
    <xsl:comment>ici</xsl:comment>
    <cit>
        <xsl:copy>
            <xsl:apply-templates select="@*|node()" />
        </xsl:copy>
        <xsl:if test="following-sibling::*[1][local-name()='p' and @text:style-name='TEI_bibl_citation']">
            <xsl:comment>récup. <xsl:value-of select="@text:style-name"/> [start]</xsl:comment>
            <xsl:copy-of select="following-sibling::*[1][local-name()='p' and @text:style-name='TEI_bibl_citation']" />
            <xsl:comment>récup. <xsl:value-of select="@text:style-name"/> [end]</xsl:comment>
        </xsl:if>
        <xsl:if test="following-sibling::*[1][local-name()='p' and starts-with(@text:style-name,'TEI_quote') and not(@text:style-name='TEI_quote')]">
            <xsl:comment>récup. <xsl:value-of select="@text:style-name"/> [start]</xsl:comment>
            <xsl:choose>
                <xsl:when test="following-sibling::*[1][local-name()='p' and @text:style-name='TEI_quote_nested']">
                    <cit><xsl:copy-of select="following-sibling::*[1][local-name()='p' and @text:style-name='TEI_quote_nested']"/></cit>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:copy-of select="following-sibling::*[1][local-name()='p' and starts-with(@text:style-name,'TEI_quote')]"/>
                </xsl:otherwise>
            </xsl:choose>
            <xsl:comment>récup. <xsl:value-of select="@text:style-name"/> [end]</xsl:comment>
            <!--<plop><xsl:copy-of select="."/></plop>-->
            <xsl:if test="following-sibling::*[1][local-name()='p' and starts-with(@text:style-name,'TEI_quote')]/following-sibling::*[1][local-name()='p' and @text:style-name='TEI_bibl_citation']">
                <xsl:copy-of select="following-sibling::*[1][local-name()='p' and starts-with(@text:style-name,'TEI_quote')]/following-sibling::*[1][local-name()='p' and @text:style-name='TEI_bibl_citation']"/>
            </xsl:if>
        </xsl:if>
<!--
        <xsl:if test="following-sibling::*[position() &lt; 3 and local-name()='p' and @text:style-name='TEI_quote_continuation']">
            <xsl:comment>récup. <xsl:value-of select="@text:style-name"/> [start]</xsl:comment>
            <xsl:copy-of select="following-sibling::*[position() &lt; 3 and local-name()='p' and @text:style-name='TEI_quote_continuation']" />
            <xsl:comment>récup. <xsl:value-of select="@text:style-name"/> [end]</xsl:comment>
        </xsl:if>
-->
    </cit>
</xsl:template>
  
<xsl:template match="text:p[@text:style-name='TEI_bibl_citation']">
    <xsl:choose>
        <xsl:when test="preceding-sibling::*[1][local-name()='p' and starts-with(@text:style-name,'TEI_quote')]">
<!--            <xsl:comment>(suppr.) réf. biblio intégrée au cit</xsl:comment>-->
        </xsl:when>
        <xsl:otherwise>
<!--            <xsl:comment>réf biblio conservée</xsl:comment>-->
            <xsl:copy-of select="."/>
        </xsl:otherwise>
    </xsl:choose>
</xsl:template>
    
<xsl:template match="text:p[starts-with(@text:style-name,'TEI_quote|')]">
    <xsl:choose>
        <xsl:when test="preceding-sibling::*[1][local-name()='p' and starts-with(@text:style-name,'TEI_quote')]">
<!--            <xsl:comment>(suppr.) quote intégrée au cit</xsl:comment>-->
        </xsl:when>
        <xsl:otherwise>
<!--            <xsl:comment>quote conservée</xsl:comment>-->
            <cit>
                <quote>
                    <xsl:attribute name="xml:lang">
                        <xsl:value-of select="substring-after(@text:style-name,'TEI_quote|')"/>
                    </xsl:attribute>
                    <xsl:apply-templates/>
                </quote>
            </cit>
        </xsl:otherwise>
    </xsl:choose>
</xsl:template>
    
<xsl:template match="text:p[@text:style-name='TEI_quote_nested']">
    <xsl:choose>
        <xsl:when test="preceding-sibling::*[1][local-name()='p' and starts-with(@text:style-name,'TEI_quote')]">
<!--            <xsl:comment>(suppr.) quote nested intégrée au cit</xsl:comment>-->
        </xsl:when>
        <xsl:otherwise>
<!--            <xsl:comment>quote conservée</xsl:comment>-->
            <xsl:copy-of select="."/>
        </xsl:otherwise>
    </xsl:choose>
</xsl:template>
    
<!-- ## entretien ## préfiguration des <sp> -->
<xsl:template match="text:p[@text:style-name='TEI_speaker']">
    <startSP>
        <xsl:attribute name="rend">
            <xsl:choose>
                <xsl:when test="following-sibling::text:p[1][@text:style-name='TEI_question']">question</xsl:when>
                <xsl:when test="following-sibling::text:p[1][@text:style-name='TEI_versifiedreplica']"/>
                <xsl:when test="following-sibling::text:p[1][@text:style-name='TEI_replica']"/>
                <xsl:otherwise>answer</xsl:otherwise>
            </xsl:choose>
        </xsl:attribute>
    </startSP>
    <xsl:copy>
        <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
</xsl:template>
    
<xsl:template match="text:p[@text:style-name='TEI_question']">
    <xsl:choose>
        <xsl:when test="preceding-sibling::text:p[1][@text:style-name='TEI_speaker']"></xsl:when>
        <xsl:when test="preceding-sibling::text:p[1][@text:style-name='TEI_question']"></xsl:when>
        <xsl:otherwise><startSP rend="question"/></xsl:otherwise>
    </xsl:choose>
    <xsl:copy>
        <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
    <xsl:choose>
        <xsl:when test="following-sibling::text:p[1][@text:style-name='TEI_question']"></xsl:when>
        <xsl:otherwise><endSP/></xsl:otherwise>
    </xsl:choose>
</xsl:template>
    
<xsl:template match="text:p[@text:style-name='TEI_answer']">
    <xsl:choose>
        <xsl:when test="child::text:span[@text:style-name='TEI_speaker-inline']">
            <startSP rend="answer"/>
        </xsl:when>
        <xsl:when test="preceding-sibling::text:p[1][@text:style-name='TEI_speaker']"></xsl:when>
        <xsl:when test="preceding-sibling::text:p[1][@text:style-name='TEI_answer']"/>
        <xsl:otherwise><startSP rend="answer"/></xsl:otherwise>
    </xsl:choose>
    <xsl:copy>
        <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
    <xsl:choose>
        <xsl:when test="following-sibling::text:p[1][@text:style-name='TEI_answer'][child::text:span[@text:style-name='TEI_speaker-inline']]"><endSP/></xsl:when>
        <xsl:when test="following-sibling::text:p[1][@text:style-name='TEI_answer']"></xsl:when>
        <xsl:otherwise><endSP/></xsl:otherwise>
    </xsl:choose>
</xsl:template>
    
<xsl:template match="text:p[@text:style-name='TEI_versifiedreplica']">
    <xsl:choose>
        <xsl:when test="child::text:span[@text:style-name='TEI_speaker-inline']">
            <startSP/><!-- rend="versifiedreplica" -->
        </xsl:when>
        <xsl:when test="preceding-sibling::text:p[1][@text:style-name='TEI_speaker']"></xsl:when>
<!--        <xsl:when test="preceding-sibling::text:p[1][@text:style-name='TEI_versifiedreplica']"/>-->
        <xsl:otherwise><startSP/><!-- rend="versifiedreplica"--></xsl:otherwise>
    </xsl:choose>
    <xsl:copy>
        <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
    <xsl:choose>
        <xsl:when test="following-sibling::text:p[1][@text:style-name='TEI_bibl_reference']"/>
        <xsl:when test="following-sibling::text:p[1][@text:style-name='TEI_versifiedreplica'][child::text:span[@text:style-name='TEI_speaker-inline']]"><endSP/></xsl:when>
<!--        <xsl:when test="following-sibling::text:p[1][@text:style-name='TEI_versifiedreplica']"></xsl:when>-->
        <xsl:otherwise><endSP/></xsl:otherwise>
    </xsl:choose>
</xsl:template>
    
<xsl:template match="text:p[@text:style-name='TEI_replica']">
    <xsl:choose>
        <xsl:when test="child::text:span[@text:style-name='TEI_speaker-inline']">
            <startSP/><!-- end="replica" -->
        </xsl:when>
        <xsl:when test="preceding-sibling::text:p[1][@text:style-name='TEI_speaker']"></xsl:when>
<!--        <xsl:when test="preceding-sibling::text:p[1][@text:style-name='TEI_replica']"/>-->
        <xsl:otherwise><startSP/><!-- rend="replica"--></xsl:otherwise>
    </xsl:choose>
    <xsl:copy>
        <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
    <xsl:choose>
        <xsl:when test="following-sibling::text:p[1][@text:style-name='TEI_bibl_reference']"/>
        <xsl:when test="following-sibling::text:p[1][@text:style-name='TEI_replica'][child::text:span[@text:style-name='TEI_speaker-inline']]"><endSP/></xsl:when>
<!--        <xsl:when test="following-sibling::text:p[1][@text:style-name='TEI_replica']"></xsl:when>-->
        <xsl:otherwise><endSP/></xsl:otherwise>
    </xsl:choose>
</xsl:template>
    
<xsl:template match="text:p[@text:style-name='TEI_bibl_reference']">
    <xsl:choose>
        <xsl:when test="preceding-sibling::text:p[1][@text:style-name='TEI_versifiedreplica']">
            <xsl:copy-of select="."/>
            <endSP/>
        </xsl:when>
        <xsl:when test="preceding-sibling::text:p[1][@text:style-name='TEI_replica']">
            <xsl:copy-of select="."/>
            <endSP/>
        </xsl:when>
        <xsl:otherwise>
            <xsl:copy-of select="."/>
        </xsl:otherwise>
    </xsl:choose>
</xsl:template>
    
</xsl:stylesheet>