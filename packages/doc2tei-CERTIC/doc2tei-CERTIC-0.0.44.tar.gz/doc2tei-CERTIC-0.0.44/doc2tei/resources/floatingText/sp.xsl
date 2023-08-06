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
  exclude-result-prefixes="dr3d style chart  calcext math xsd loext table ooow xhtml meta oooc grddl number dom xsi officeooo svg xforms tableooo drawooo fo rpt xlink ooo of dc ooow formx config css3t office text form field draw script">

<xsl:output method="xml" encoding="UTF-8" indent="no"/>
 
<xsl:template match="@*|text()">
    <xsl:copy>
        <xsl:apply-templates select="@*|text()"/>
    </xsl:copy>
</xsl:template>
    
<xsl:template match="@*|node()" mode="group">
    <xsl:choose>
        <xsl:when test="local-name()='endSP'"/>
        <xsl:otherwise> 
          <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
          </xsl:copy>
        </xsl:otherwise>
    </xsl:choose>
</xsl:template>
    
<xsl:template match="element()">
    <xsl:if test="not(preceding-sibling::*:startSP) or not(following-sibling::*:endSP) or local-name(preceding::*[local-name()='endSP' or local-name()='startSP'][1])='endSP' or local-name()='startSP' or local-name()='endSP'">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:if>
</xsl:template>
    
<xsl:template match="*:startSP">
    <xsl:variable name="rend" select="@rend"/>
    <xsl:for-each-group select="following-sibling::*" group-ending-with="*:endSP">
        <xsl:if test="position()=1">
            <sp>
                <xsl:if test="$rend!=''">
                    <xsl:attribute name="rend" select="$rend"/>
                </xsl:if>
                <xsl:apply-templates select="current-group()" mode="group"/>
            </sp>
        </xsl:if>
    </xsl:for-each-group>
</xsl:template>

<xsl:template match="*:endSP"/>
    
</xsl:stylesheet>