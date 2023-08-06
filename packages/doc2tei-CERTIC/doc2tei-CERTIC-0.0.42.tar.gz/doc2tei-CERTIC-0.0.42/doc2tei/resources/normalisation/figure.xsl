<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="2.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns="http://www.tei-c.org/ns/1.0"
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
    
    
<xsl:template match="@office:value-type"/>    
    
<xsl:template match="draw:frame[parent::*[not(@text:style-name='TEI_figure_alternative')]]">
    <xsl:choose>
        <!-- images inline -->
        <xsl:when test="parent::*[child::text()]">
            <xsl:comment>*image inline*</xsl:comment>
            <figure rend="inline">
                <xsl:copy>
                    <xsl:apply-templates select="@*|node()" />
                </xsl:copy>
            </figure>
        </xsl:when>
        <!-- image block -->
        <xsl:otherwise>
            <xsl:comment>*image block*</xsl:comment>
             <xsl:choose>
                <xsl:when test="$source='OpenEdition'">
                    <figure rend="block">
                        <xsl:choose>
                            <!-- test du premier nœud précédent -->
                            <xsl:when test="parent::*[preceding-sibling::*[1][local-name()='p' and @text:style-name='TEI_figure_title']]">
                                <!-- on inverse l'ordre des éléments -->
                                <xsl:copy>
                                    <xsl:apply-templates select="@*|node()" />
                                </xsl:copy>
                                <!-- copie du titre -->
                                <xsl:apply-templates select="parent::*/preceding-sibling::*[1][local-name()='p' and @text:style-name='TEI_figure_title']" mode="preserve"/>
                            </xsl:when>
                            <!-- cas des images sans titre -->
                            <xsl:otherwise>
                                <xsl:copy>
                                    <xsl:apply-templates select="@*|node()" />
                                </xsl:copy>
                            </xsl:otherwise>
                        </xsl:choose>                      
                    </figure>
                </xsl:when>
                <xsl:otherwise>
                    <!-- source 'Métopes' : on ne change pas l'ordre mais on fait un structure englobante -->
                    <figure rend="block">
                        <xsl:apply-templates select="." mode="preserve"/>
                    </figure>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:otherwise>
    </xsl:choose>
</xsl:template>

    
<!-- copy a node adding an attribute 
<xsl:copy>
    <xsl:attribute name="width">100</xsl:attribute>
    <xsl:apply-templates select="@*|node()" />
</xsl:copy>
-->
    
<!-- Inversion de la position du titre de tableau pour unicité du traitement dans la pass totei -->
<xsl:template match="table:table">
    <figure rend="block">
        <xsl:choose>
            <xsl:when test="$source='OpenEdition'">
                <xsl:choose>
                    <xsl:when test="preceding-sibling::*[1][local-name()='p' and @text:style-name='TEI_figure_title']">
                    <!-- on inverse l'ordre des éléments -->
                        <xsl:copy>
                            <xsl:apply-templates select="@*|node()" />
                        </xsl:copy>
                        <xsl:apply-templates select="preceding-sibling::*[1][local-name()='p' and @text:style-name='TEI_figure_title']" mode="preserve"/>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:copy>
                            <xsl:apply-templates select="@*|node()" />
                        </xsl:copy>
                    </xsl:otherwise>
                </xsl:choose>

            </xsl:when>
            <xsl:otherwise>
                <!-- source 'Métopes' : on ne change pas l'ordre mais on fait un structure englobante -->
                    <xsl:apply-templates select="." mode="preserve"/>
            </xsl:otherwise>
        </xsl:choose>
    </figure>
</xsl:template>
    
<!-- math -->
<xsl:template match="draw:frame[child::draw:object]">
    <xsl:apply-templates select="child::draw:object/node()"/>
</xsl:template>

<!-- formula -->
<xsl:template match="text:p[@text:style-name='TEI_formula']">
    <figure rend="block">
        <formula>
            <xsl:attribute name="notation">
                <xsl:choose>
                    <xsl:when test="descendant::*:math">mathml</xsl:when>
                    <xsl:otherwise>latex</xsl:otherwise>
                </xsl:choose>
            </xsl:attribute>
            <xsl:apply-templates/>
        </formula>
        <xsl:choose>
            <xsl:when test="$source='OpenEdition'">
                <xsl:choose>
                    <xsl:when test="preceding-sibling::*[1][local-name()='p' and @text:style-name='TEI_figure_title']">
                    <!-- on inverse l'ordre des éléments -->
                        <xsl:copy>
                            <xsl:apply-templates select="@*|node()" />
                        </xsl:copy>
                        <xsl:apply-templates select="preceding-sibling::*[1][local-name()='p' and @text:style-name='TEI_figure_title']" mode="preserve"/>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:copy>
                            <xsl:apply-templates select="@*|node()" />
                        </xsl:copy>
                    </xsl:otherwise>
                </xsl:choose>

            </xsl:when>
            <xsl:otherwise>
                <!-- source 'Métopes' : on ne change pas l'ordre mais on fait un structure englobante -->
                    <xsl:apply-templates select="." mode="preserve"/>
            </xsl:otherwise>
        </xsl:choose>
    </figure> 
</xsl:template>

<!-- Les éléments sont identifiés dans une pass ultérieure -->
    
<xsl:template match="text:p[@text:style-name='TEI_figure_title']" mode="preserve">
    <xsl:copy>
        <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
</xsl:template>
<xsl:template match="text:p[@text:style-name='TEI_figure_title']"/>

    
<!-- ?? Ces traitements ne devraient-ils pas figurer dans la phase (#1) de clean up ? -->
<xsl:template match="@draw:style-name"/>
<xsl:template match="@draw:z-index"/>    
<xsl:template match="@svg:height"/>
<xsl:template match="@svg:width"/>
<xsl:template match="@text:anchor-type"/>
<xsl:template match="@xlink:actuate"/>
<xsl:template match="@xlink:show"/>
<xsl:template match="@xlink:type"/>
    
</xsl:stylesheet>