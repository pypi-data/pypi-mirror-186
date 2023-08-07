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
  exclude-result-prefixes="formx config of svg dr3d calcext loext form field script chart">

<xsl:variable name="source">
    <xsl:value-of select="//meta:user-defined[@meta:name='source']"/>
</xsl:variable> 
    
<!-- Gestion des raccourcis de styles -->
<xsl:template match="*[@text:style-name]">
    
  <xsl:variable name="currentStyle">
    <xsl:value-of select="@text:style-name"/>
  </xsl:variable>
  <xsl:variable name="currentElementName">
    <xsl:value-of select="name(.)"/>
  </xsl:variable>

    <xsl:choose>
    <!-- Suppression des éléments vides -->
    <xsl:when test=".[not(*|comment()|processing-instruction()) and normalize-space()='']"/>
    <!-- Gestion des enrichissements typographiques text:span -->
    <xsl:when test="$currentElementName='text:span'">
        <xsl:choose>
        <!-- enrichissements typo traitement de texte (l'application de styles de caractères ne génère pas de raccourcis de styles)-->
            <xsl:when test="starts-with($currentStyle,'TEI_5f_') and ends-with($currentStyle,'inline')">
                <xsl:apply-templates select="." mode="preserve"/>
            </xsl:when>
            <xsl:when test="child::text:note">
                <xsl:apply-templates/>
            </xsl:when>
            <xsl:when test="$currentStyle='Emphasis'">
                <xsl:element name="text:span">
                        <xsl:attribute name="rendition">italic</xsl:attribute>
                        <xsl:attribute name="text:style-name">italic</xsl:attribute>
                        <xsl:apply-templates/>
                </xsl:element>
            </xsl:when>
            <xsl:when test="matches(@text:style-name,'[T]\d{1,2}')">
                <xsl:choose>
                    <!-- premier test pour une liste des propriétés retenus -->
                    <xsl:when test="//style:style[@style:name=$currentStyle]/style:text-properties/(@fo:font-style|@fo:font-variant|@fo:font-weight|@style:text-position|@style:text-underline-style)">
                    <xsl:element name="text:span">
                        <xsl:attribute name="rendition">
                        <!-- liste fermée des cas à traiter -->
                        <xsl:for-each select="//style:style[@style:name=$currentStyle]/style:text-properties/(@fo:font-style|@fo:font-variant|@fo:font-weight)">
                            <xsl:if test="./position()!=last()">
                                <xsl:text> </xsl:text>
                            </xsl:if>
                            <xsl:value-of select="."/>
                        </xsl:for-each>
                        <xsl:for-each select="//style:style[@style:name=$currentStyle]/style:text-properties/@style:text-position">
                            <xsl:if test="//style:style[@style:name=$currentStyle]/style:text-properties/(@fo:font-style|@fo:font-variant|@fo:font-weight)"><xsl:text> </xsl:text></xsl:if>
                            <xsl:choose>
                                <xsl:when test="contains(.,'super')">
                                    <xsl:text>sup</xsl:text>
                                </xsl:when>
                                <xsl:otherwise>
                                    <xsl:value-of select="substring-before(.,' ')"/>
                                </xsl:otherwise>
                            </xsl:choose>
                        </xsl:for-each>
                        <xsl:for-each select="//style:style[@style:name=$currentStyle]/style:text-properties/@style:text-underline-style">
                            <xsl:if test="//style:style[@style:name=$currentStyle]/style:text-properties/(@fo:font-style|@fo:font-variant|@fo:font-weight|@style:text-position)"><xsl:text> </xsl:text></xsl:if>
                            <xsl:text>underline</xsl:text>
                        </xsl:for-each>
                        <xsl:for-each select="//style:style[@style:name=$currentStyle]/style:text-properties/@style:text-line-through-style">
                            <xsl:text>line-through</xsl:text>
                        </xsl:for-each>                
                        </xsl:attribute>
                        <xsl:attribute name="text:style-name">
                        <!-- liste fermée des cas à traiter -->
                        <xsl:for-each select="//style:style[@style:name=$currentStyle]/style:text-properties/(@fo:font-style|@fo:font-variant|@fo:font-weight)">
                            <xsl:if test="./position()!=last()">
                                <xsl:text> </xsl:text>
                            </xsl:if>
                            <xsl:value-of select="."/>
                        </xsl:for-each>
                        <xsl:for-each select="//style:style[@style:name=$currentStyle]/style:text-properties/@style:text-position">
                            <xsl:if test="//style:style[@style:name=$currentStyle]/style:text-properties/(@fo:font-style|@fo:font-variant|@fo:font-weight)"><xsl:text> </xsl:text></xsl:if>
                            <xsl:choose>
                                <xsl:when test="contains(.,'super')">
                                    <xsl:text>sup</xsl:text>
                                </xsl:when>
                                <xsl:otherwise>
                                    <xsl:value-of select="substring-before(.,' ')"/>
                                </xsl:otherwise>
                            </xsl:choose>
                        </xsl:for-each>
                        <xsl:for-each select="//style:style[@style:name=$currentStyle]/style:text-properties/@style:text-underline-style">
                            <xsl:if test="//style:style[@style:name=$currentStyle]/style:text-properties/(@fo:font-style|@fo:font-variant|@fo:font-weight|@style:text-position)"><xsl:text> </xsl:text></xsl:if>
                            <xsl:text>underline</xsl:text>
                        </xsl:for-each>
                        <xsl:for-each select="//style:style[@style:name=$currentStyle]/style:text-properties/@style:text-line-through-style">
                            <xsl:text>line-through</xsl:text>
                        </xsl:for-each>                
                        </xsl:attribute>
                        <xsl:apply-templates/>
                    </xsl:element>
                    </xsl:when>
                    <!-- dans les autres cas, on ne souhaite pas retenir les propriétés -->
                    <xsl:otherwise>
                        <xsl:apply-templates/>
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:when>
            <xsl:when test="@text:style-name='apple-converted-space'">
                <xsl:text> </xsl:text><xsl:apply-templates/>
            </xsl:when>
            <!-- neutralisation des styles hérités et identifiés -->
            <xsl:when test="starts-with(@text:style-name,'apple') or starts-with(@text:style-name,'Internet_') or starts-with(@text:style-name,'Placeho')">
                <xsl:apply-templates/>
            </xsl:when>
            <!-- style de caractères appliqués -->
<!-- changement de logique : au lieu de supprimer les styles en trop, on ne conserve que les styles dont on connaît le préfixe (métopes ou oe) -->
            <xsl:otherwise>
                <xsl:copy-of select="."/>
                <!-- ne règle pas le problème d'imbrication de span… dans des liens hypertextes par exemple ; tester pour les doubles enrichissements typographiques aussi -->
<!--                <xsl:apply-templates/>-->
            </xsl:otherwise>
        </xsl:choose>
    </xsl:when>
    <!-- Gestion des titres (dont la gestion niveaux @text:outline-level) -->
    <xsl:when test="$currentElementName='text:h' or ($currentElementName='text:p' and @text:outline-level)">
        <xsl:element name="text:h">
            <xsl:copy-of select="@*"/>
            <xsl:attribute name="text:style-name">
                <xsl:choose>
                    <xsl:when test="matches($currentStyle,'[P]\d{1,2}')">
                        <xsl:value-of select="//style:style[@style:name=$currentStyle]/@style:parent-style-name"/>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:value-of select="$currentStyle"/>
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:attribute>
            <xsl:if test="//style:style[@style:name=$currentStyle][child::style:paragraph-properties[@style:writing-mode='rl-tb']]">
                <xsl:attribute name="rendition">#rtl</xsl:attribute>
                <xsl:attribute name="text:style-name">#rtl</xsl:attribute>
             </xsl:if>
            <xsl:choose>
<!-- Sur le titre principal (@text:outline-level="Title…"), on affecte un @text:outline-level à 0  -->
                <xsl:when test="starts-with($currentStyle,'Title') or starts-with(//style:style[@style:name=$currentStyle]/@style:parent-style-name,'Title')">
                    <xsl:attribute name="text:outline-level">0</xsl:attribute>
                </xsl:when>
<!-- surcharge pour la gestion du début de section biblio (OpenEdition) -->
                <xsl:when test="@text:style-name='TEI_5f_bibl_5f_start' or //style:style[@style:name=$currentStyle]/@style:parent-style-name='TEI_5f_bibl_5f_start'">
                    <xsl:attribute name="subtype">biblio</xsl:attribute>
                </xsl:when>
<!-- surcharge pour la gestion du début de section appendix (OpenEdition) -->
                <xsl:when test="@text:style-name='TEI_5f_appendix_5f_start' or //style:style[@style:name=$currentStyle]/@style:parent-style-name='TEI_5f_appendix_5f_start'">
                    <xsl:attribute name="subtype">appendix</xsl:attribute>
                </xsl:when>
<!-- tentative ici d'ajouter +1 au niveau hiérarchique pour les titres de la section biblio et de la section annexe (méthode OpenEdition) -->
                <xsl:when test=".[preceding::text:h[@text:style-name='TEI_5f_bibl_5f_start' or //style:style[@style:name=$currentStyle]/@style:parent-style-name='TEI_5f_bibl_5f_start']] or .[preceding::text:h[@text:style-name='TEI_5f_appendix_5f_start' or //style:style[@style:name=$currentStyle]/@style:parent-style-name='TEI_5f_appendix_5f_start']]">
                    <xsl:attribute name="subtype">
                        <xsl:choose>
                            <xsl:when test=".[preceding::text:h[@text:style-name='TEI_5f_appendix_5f_start' or //style:style[@style:name=$currentStyle]/@style:parent-style-name='TEI_5f_appendix_5f_start']]">sous-appendix</xsl:when>
                            <xsl:otherwise>sousbiblio</xsl:otherwise>
                        </xsl:choose>
                    </xsl:attribute>
<!-- gestion hiérarchique différente pour les sections biblio entre Métopes (Titre section biblio niveau 1) et OpenEdition (pas de titre de section) -->
                    <xsl:attribute name="text:outline-level">
                        <xsl:choose>
                            <xsl:when test="$source='OpenEdition'"><xsl:value-of select="@text:outline-level+1"/></xsl:when>
                            <xsl:otherwise><xsl:value-of select="@text:outline-level"/></xsl:otherwise>
                        </xsl:choose>
                    </xsl:attribute>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:copy-of select="@text:outline-level"/>
                </xsl:otherwise>
            </xsl:choose>
            <xsl:apply-templates/>
        </xsl:element>
    </xsl:when>
    <!-- Gestion du titre principal si source Libre Office : conversion de text:p à text:h  (à voir si besoin d'être conservé, car on peut affecter un niveau de plan via la stylage dans Libre Office) -->
    <xsl:when test="$currentElementName='text:p' and (@text:style-name='Title' or //style:style[@style:name=$currentStyle]/@style:parent-style-name='Title')">
        <xsl:element name="text:h">
            <xsl:copy-of select="@*"/>
            <xsl:attribute name="text:outline-level">0</xsl:attribute>
            <xsl:attribute name="text:style-name">
                <xsl:choose>
                    <xsl:when test="matches($currentStyle,'[P]\d{1,2}')">
                        <xsl:value-of select="//style:style[@style:name=$currentStyle]/@style:parent-style-name"/>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:value-of select="$currentStyle"/>
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:attribute>
            <xsl:if test="//style:style[@style:name=$currentStyle][child::style:paragraph-properties[@style:writing-mode='rl-tb']]">
                <xsl:attribute name="rendition">#rtl</xsl:attribute>
                <xsl:attribute name="text:style-name">#rtl</xsl:attribute>
             </xsl:if>
            <xsl:apply-templates/>
        </xsl:element>
    </xsl:when>
<!-- surcharge pour affecter un niveau de titre pour les références bibliographiques d'ouvrage recensé -->
    <xsl:when test="$currentElementName='text:p' and (@text:style-name='TEI_5f_reviewed_5f_reference' or //style:style[@style:name=$currentStyle]/@style:parent-style-name='TEI_5f_reviewed_5f_reference')">
        <xsl:element name="text:h">
            <xsl:copy-of select="@*"/>
            <xsl:attribute name="text:outline-level">1</xsl:attribute>
            <xsl:attribute name="subtype">review</xsl:attribute>
            <xsl:attribute name="text:style-name">
                <xsl:choose>
                    <xsl:when test="matches($currentStyle,'[P]\d{1,2}')">
                        <xsl:value-of select="//style:style[@style:name=$currentStyle]/@style:parent-style-name"/>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:value-of select="$currentStyle"/>
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:attribute>
            <xsl:if test="//style:style[@style:name=$currentStyle][child::style:paragraph-properties[@style:writing-mode='rl-tb']]">
                <xsl:attribute name="rendition">#rtl</xsl:attribute>
                <xsl:attribute name="text:style-name">#rtl</xsl:attribute>
             </xsl:if>
            <xsl:apply-templates/>
        </xsl:element>
    </xsl:when>
<!-- ajout d'un @outline-level sur le titre de section biblio (Métopes) /!\ -->
	<xsl:when test="$currentElementName='text:p' and (@text:style-name='Titre-section-biblio' or //style:style[@style:name=$currentStyle]/@style:parent-style-name='Titre-section-biblio')">
		<xsl:element name="text:h">
            <xsl:copy-of select="@*"/>
            <xsl:attribute name="text:outline-level">1</xsl:attribute>
            <xsl:attribute name="subtype">biblio</xsl:attribute>
            <xsl:attribute name="text:style-name">
                <xsl:choose>
                    <xsl:when test="matches($currentStyle,'[P]\d{1,2}')">
                        <xsl:value-of select="//style:style[@style:name=$currentStyle]/@style:parent-style-name"/>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:value-of select="$currentStyle"/>
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:attribute>
            <xsl:if test="//style:style[@style:name=$currentStyle][child::style:paragraph-properties[@style:writing-mode='rl-tb']]">
                <xsl:attribute name="rendition">#rtl</xsl:attribute>
                <xsl:attribute name="text:style-name">#rtl</xsl:attribute>
             </xsl:if>
            <xsl:apply-templates/>
        </xsl:element>
	</xsl:when>
    <!-- listes -->
    <xsl:when test="$currentElementName='text:list'">
        <xsl:choose>
            <xsl:when test="descendant::text:h">
                <xsl:apply-templates select="descendant::text:h"/>
            </xsl:when>
        <xsl:otherwise>
            <xsl:variable name="firstChild">
                <xsl:copy-of select="//text:list-style[@style:name=$currentStyle]/*[1]/local-name()"/>
            </xsl:variable>
            <xsl:element name="{$currentElementName}">
                <xsl:copy-of select="@*"/>
                <xsl:if test="//style:style[@style:name=$currentStyle][child::style:paragraph-properties[@style:writing-mode='rl-tb']]">
                    <xsl:attribute name="rendition">#rtl</xsl:attribute>
                    <xsl:attribute name="text:style-name">#rtl</xsl:attribute>
                </xsl:if>
                <xsl:choose>
                    <xsl:when test="$firstChild='list-level-style-number'">
                        <xsl:attribute name="type">ordered</xsl:attribute>
                        <xsl:copy-of select="//text:list-style[@style:name=$currentStyle]/*[1]/@style:num-format"/>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:attribute name="type">unordered</xsl:attribute>
                        <xsl:attribute name="text:bullet-char">
                            <xsl:choose>
                                <xsl:when test="//text:list-style[@style:name=$currentStyle]/*[1][@text:bullet-char=''][child::style:text-properties[@fo:font-family='Symbol']]">●</xsl:when>
                                <xsl:when test="//text:list-style[@style:name=$currentStyle]/*[1][@text:bullet-char=''][child::style:text-properties[@fo:font-family='Wingdings']]">■</xsl:when>
                                <xsl:when test="//text:list-style[@style:name=$currentStyle]/*[1][@text:bullet-char='o'][child::style:text-properties[contains(@fo:font-family,'Courier New')]]">○</xsl:when>
                                <xsl:otherwise>??</xsl:otherwise>
                            </xsl:choose>
                        </xsl:attribute>
                    </xsl:otherwise>
                </xsl:choose>
                <xsl:apply-templates/>
            </xsl:element>
        </xsl:otherwise>
        </xsl:choose>
    </xsl:when>
    <!-- surcharge alignement table -->
    <xsl:when test="$currentElementName='text:p' and parent::table:table-cell and //style:style[@style:name=$currentStyle]/style:paragraph-properties/@fo:text-align">
        <xsl:element name="{$currentElementName}">
            <xsl:copy-of select="@*"/>
            <xsl:attribute name="text:style-name">
                <xsl:choose>
                    <xsl:when test="matches($currentStyle,'[P]\d{1,2}')">
                        <xsl:value-of select="//style:style[@style:name=$currentStyle]/@style:parent-style-name"/>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:value-of select="$currentStyle"/>
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:attribute>
            <xsl:attribute name="align"><xsl:value-of select="//style:style[@style:name=$currentStyle]/style:paragraph-properties/@fo:text-align"/></xsl:attribute>
            <xsl:apply-templates/>
        </xsl:element>
    </xsl:when>
    <!-- début et fin d'encadrés -->
    <xsl:when test="$currentElementName='text:p' and @text:style-name='TEI_5f_floatingText_5f_start'"><start/></xsl:when>
    <xsl:when test="$currentElementName='text:p' and @text:style-name='TEI_5f_floatingText_5f_end'"><end/></xsl:when>
    <!-- Gestion des autres éléments -->
    <xsl:otherwise>
        <xsl:element name="{$currentElementName}">
            <xsl:copy-of select="@*"/>
            <xsl:if test="//style:style[@style:name=$currentStyle][@style:parent-style-name='TEI_5f_verse' and child::style:paragraph-properties[@fo:text-align]]">
                <xsl:attribute name="rendition">
                    <xsl:value-of select="concat('#',//style:style[@style:name=$currentStyle][@style:parent-style-name='TEI_5f_verse']/style:paragraph-properties/@fo:text-align)"/>
                </xsl:attribute>
            </xsl:if>
            <xsl:attribute name="text:style-name">
                <xsl:choose>
                    <!-- est-ce qu'on estime que le système de nommage des raccourcis de styles est normalisé ? -->
                    <xsl:when test="matches($currentStyle,'[P]\d{1,2}')">
                        <xsl:value-of select="//style:style[@style:name=$currentStyle]/@style:parent-style-name"/>
                    </xsl:when>
                    <!-- cas d'un héritage de styles (paragraphes) -->
<!--                <xsl:when test="//style:style[@style:name=$currentStyle and @style:parent-style-name]">
                        <xsl:value-of select="//style:style[@style:name=$currentStyle]/@style:parent-style-name"/>
                    </xsl:when>  -->
                    <!-- style directement accessible -->
                    <xsl:otherwise>
                        <xsl:value-of select="$currentStyle"/>
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:attribute>
            <xsl:if test="//style:style[@style:name=$currentStyle][child::style:paragraph-properties[@style:writing-mode='rl-tb']]">
                <xsl:attribute name="rendition">#rtl</xsl:attribute>
                <xsl:attribute name="text:style-name">#rtl</xsl:attribute>
             </xsl:if>
            <xsl:apply-templates/>
        </xsl:element>
    </xsl:otherwise>
</xsl:choose>
</xsl:template>
          
    
</xsl:stylesheet>