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
    
<!-- TODO
- ajouter le traitement des tétiêres
- ajouter le traitement des fusions
- ajouter le renvoi aux propriétés CSS (?)
-->
    
<xsl:template match="*:figure[@rend='block']">
<!--    <xsl:comment>traitement des images block, conversion en TEI</xsl:comment>-->
    <xsl:variable name="nextFig">
        <xsl:copy-of select="following::*:figure[@rend='block'][1]"/>
    </xsl:variable>
    <figure>
        <xsl:copy-of select="@*"/>
        <xsl:apply-templates select="." mode="inFig"/>
        <xsl:choose>
            <!-- figure[@rend='block'] permet d'atteindre image, tableau, équation -->
            <xsl:when test="following::*:figure[@rend='block'] and child::draw:frame">
                <xsl:apply-templates select="parent::*/following-sibling::text:p[starts-with(@text:style-name,'TEI_figure')][following::*:figure=$nextFig]" mode="inFig"/>
            </xsl:when>
            <!-- les tableaux ne sont pas dans un élément p, le xpath précédent ne fonctionne donc pas… donc test sur la nature de l'élément dans le bloc figure-->
            <xsl:when test="following::*:figure[@rend='block'] and child::table:table">
                <xsl:apply-templates select="following-sibling::text:p[starts-with(@text:style-name,'TEI_figure')][following::*:figure=$nextFig]" mode="inFig"/>
            </xsl:when>
            <!-- formula -->
            <xsl:when test="following::*:figure[@rend='block'] and child::*:formula">
                <xsl:apply-templates select="following-sibling::text:p[starts-with(@text:style-name,'TEI_figure')][following::*:figure=$nextFig]" mode="inFig"/>
            </xsl:when>
            <xsl:otherwise>
<!--                <xsl:comment>dernière occurence dans le document</xsl:comment>-->
                <xsl:apply-templates select="following::text:p[starts-with(@text:style-name,'TEI_figure')][following::*:endOfDocument]" mode="inFig"/>
            </xsl:otherwise>
        </xsl:choose>     
    </figure>
</xsl:template>
    
<xsl:template match="*:figure[@rend='inline']">
    <figure>
        <xsl:copy-of select="@*"/>
        <xsl:apply-templates mode="inFig"/>
    </figure>
</xsl:template>
    
<!-- ## TABLES ## -->
<xsl:template match="table:table" mode="inFig">
    
<xsl:variable name="tableColumn">
  <xsl:choose>
    <xsl:when test="child::table:table-column/@table:number-columns-repeated and child::table:table-column[not(@table:number-columns-repeated)]">
      <xsl:value-of select="sum(child::table:table-column/@table:number-columns-repeated) + count(child::table:table-column[not(@table:number-columns-repeated)])"/>
    </xsl:when>
    <xsl:when test="child::table:table-column[not(@table:number-columns-repeated)]">
      <xsl:value-of select="count(child::table:table-column)"/>
    </xsl:when>
    <xsl:when test="child::table:table-column/@table:number-columns-repeated">
      <xsl:value-of select="sum(child::table:table-column/@table:number-columns-repeated)"/>
    </xsl:when>
    <xsl:otherwise/>
  </xsl:choose>
</xsl:variable>

    <table>
        <xsl:attribute name="xml:id" select="@table:name"/>
        <xsl:attribute name="rows" select="count(descendant::table:table-row)"/>
        <xsl:attribute name="cols" select="$tableColumn"/>
        <xsl:apply-templates/>
    </table>

</xsl:template>
    
<xsl:template match="table:table-header-rows">
    <xsl:apply-templates/>
</xsl:template>

<xsl:template match="table:table-header-rows/table:table-row">
    <row role="label">
      <xsl:apply-templates/>
    </row>
  </xsl:template>
    
<xsl:template match="table:table-row">
    <row>
        <xsl:apply-templates/>
    </row>
</xsl:template>
    
<xsl:template match="table:table-cell">
    <cell>
        <xsl:if test="@table:number-columns-spanned &gt;'1'">
          <xsl:attribute name="cols">
            <xsl:value-of select="@table:number-columns-spanned"/>
          </xsl:attribute>
        </xsl:if>
        <xsl:if test="@table:number-rows-spanned &gt;'1'">
          <xsl:attribute name="rows">
            <xsl:value-of select="@table:number-rows-spanned"/>
          </xsl:attribute>
        </xsl:if>
        <xsl:attribute name="rendition">
            <!-- Tableau, Tabla, Table, Tabella,  -->
            <xsl:variable name="tableLang">
                <xsl:choose>
                    <xsl:when test="contains(@table:style-name,'Tableau')">Tableau</xsl:when>
                    <xsl:when test="contains(@table:style-name,'Tabla')">Tabla</xsl:when>
                    <xsl:when test="contains(@table:style-name,'Table')">Table</xsl:when>
                    <xsl:when test="contains(@table:style-name,'Tabella')">Tabella</xsl:when>
                    <xsl:when test="contains(@table:style-name,'Tabela')">Tabela</xsl:when>
                </xsl:choose>
            </xsl:variable>
            <xsl:value-of select="concat('#Cell',substring-after(@table:style-name,$tableLang))"/>
  	     </xsl:attribute>
        <xsl:choose>
            <xsl:when test="child::text:p[@text:style-name='TEI_cell']">
                <xsl:apply-templates select="child::text:p[@text:style-name='TEI_cell']/node()"/>
            </xsl:when>
<!--
            <xsl:when test="child::text:p[not(starts-with(@text:style-name,'TEI_')) or @text:style-name='Standard']">
                *<xsl:apply-templates select="child::text:p[not(starts-with(@text:style-name,'TEI_'))]/node()|child::text:p[@text:style-name='Standard']/node()"/>
            </xsl:when>
-->
            <xsl:when test="child::text:p[@text:style-name='Standard']">
                <xsl:apply-templates select="child::text:p[@text:style-name='Standard']/node()"/>
            </xsl:when>
            <xsl:otherwise>
                <xsl:apply-templates/>
            </xsl:otherwise>
        </xsl:choose>
<!--        <xsl:apply-templates/>-->
    </cell>
</xsl:template>

<!-- gérer dans le template table-cell supra -->
<xsl:template match="text:p[@text:style-name='TEI_cell']"/>
 
<xsl:template match="text:p[@text:style-name='TEI_figure_alternative']" mode="inFig">
    <graphic>
        <xsl:attribute name="url">
            <xsl:choose>
                <xsl:when test="$source='Metopes'">
                    <xsl:value-of select="concat('../icono',substring-after(descendant::draw:image/@xlink:href,'icono'))"/>
                </xsl:when>
                <xsl:otherwise><xsl:value-of select="descendant::draw:image/@xlink:href"/></xsl:otherwise>
            </xsl:choose>
        </xsl:attribute>
    </graphic>
    <xsl:apply-templates select="descendant::svg:desc"/>
</xsl:template>
    
<xsl:template match="table:table-column"/>
<xsl:template match="table:covered-table-cell"/>
 
    
<!-- ## FIGURES ## -->
<xsl:template match="text:p[@text:style-name='TEI_figure_title']" mode="inFig">
    <head><xsl:apply-templates/></head>
</xsl:template>
    
<xsl:template match="text:p[@text:style-name='TEI_figure_caption']" mode="inFig">
    <p rend="caption"><xsl:apply-templates/></p>
</xsl:template>
    
<xsl:template match="text:p[@text:style-name='TEI_figure_credits']" mode="inFig">
    <p rend="credits"><xsl:apply-templates/></p>
</xsl:template>
    
<xsl:template match="draw:frame" mode="inFig">
    <xsl:choose>
        <xsl:when test="preceding-sibling::text() or following-sibling::text()">
            <figure rend="inline"><xsl:apply-templates/></figure>
        </xsl:when>
        <xsl:otherwise>
            <xsl:apply-templates/>
        </xsl:otherwise>
    </xsl:choose>
</xsl:template>
    
<xsl:template match="draw:image">
    <xsl:element name="graphic" xmlns="http://www.tei-c.org/ns/1.0">
        <xsl:attribute name="url">
            <xsl:choose>
                <xsl:when test="$source='Metopes'">
                    <xsl:value-of select="concat('../icono',substring-after(@xlink:href,'icono'))"/>
                </xsl:when>
                <xsl:otherwise><xsl:value-of select="@xlink:href"/></xsl:otherwise>
            </xsl:choose>
        </xsl:attribute>
    </xsl:element>
</xsl:template>
    
<xsl:template match="svg:desc">
    <figDesc><xsl:apply-templates/></figDesc>
</xsl:template>
    
<!-- ## FORMULA ## -->
<xsl:template match="*:formula" mode="inFig">
    <xsl:copy>
        <xsl:apply-templates select="@*|node()" />
    </xsl:copy>
</xsl:template>
    
<xsl:template match="text:span[@text:style-name='TEI_formula-inline']">
    <figure rend="inline"><formula notation="latex"><xsl:apply-templates/></formula></figure>
</xsl:template>

<xsl:template match="text:p[@text:style-name='TEI_formula']" mode="inFig"/>

<xsl:template match="text:p[@text:style-name='TEI_figure_caption']"/>
<xsl:template match="text:p[@text:style-name='TEI_figure_credits']"/>
<xsl:template match="text:p[@text:style-name='TEI_figure_alternative']"/>


<xsl:template match="endOfDocument"/>

</xsl:stylesheet>