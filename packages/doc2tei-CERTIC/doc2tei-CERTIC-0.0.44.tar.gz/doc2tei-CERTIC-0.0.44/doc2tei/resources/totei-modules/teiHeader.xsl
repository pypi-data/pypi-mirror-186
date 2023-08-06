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
    
<xsl:template name="teiHeader">
    <teiHeader>
      <fileDesc>
        <titleStmt>
        <!-- surtitre -->
            <xsl:if test="//text:p[@text:style-name='TEI_title:sup']">
                <title type="sup"><xsl:apply-templates select="//text:p[@text:style-name='TEI_title:sup']" mode="teiHeader"/></title>
            </xsl:if>
        <!-- titre principal -->
          <title type="main">
              <xsl:copy-of select="//text:h[@text:outline-level='0']/@xml:lang"/>
<!--              <xsl:copy-of select="//text:h[@text:outline-level='0']/@rendition"/>-->
              <xsl:apply-templates select="//text:h[@text:outline-level='0']" mode="teiHeader"/>
          </title>
        <!-- titre courant -->
        <!-- sous-titre -->
            <xsl:if test="//text:p[@text:style-name='TEI_title:sub']">
                <title type="sub"><xsl:apply-templates select="//text:p[@text:style-name='TEI_title:sub']" mode="teiHeader"/></title>
            </xsl:if>
        <!-- titre traduit -->
            <xsl:if test="//text:p[contains(@text:style-name,'TEI_title:trl')]">
                <xsl:for-each select="//text:p[contains(@text:style-name,'TEI_title:trl')]">
                    <title type="trl">
                        <xsl:copy-of select="@xml:lang"/>
                        <xsl:apply-templates mode="teiHeader"/>
                    </title>
                </xsl:for-each>
            </xsl:if>
            <!-- bloc auteur -->
            <xsl:for-each-group select="//text:p[starts-with(@text:style-name,'TEI_author') or starts-with(@text:style-name,'TEI_editor')]" group-starting-with="text:p[starts-with(@text:style-name,'TEI_author:') or starts-with(@text:style-name,'TEI_editor:')]">
                <xsl:variable name="context">
                    <xsl:choose>
                        <xsl:when test="contains(@text:style-name,'TEI_author')">author</xsl:when>
                        <xsl:when test="contains(@text:style-name,'TEI_editor')">editor</xsl:when>
                        <xsl:otherwise>undefined</xsl:otherwise>
                    </xsl:choose>
                </xsl:variable>
                <xsl:element name="{$context}">
                    <xsl:attribute name="role" select="substring-after(./@text:style-name,':')"/>
                    <xsl:apply-templates select="current-group()[not(contains(@text:style-name,'_biography'))]" mode="teiHeader"/>
                    <xsl:if test="current-group()/.[@text:style-name='TEI_authority_biography']">
                        <note type="biography">
                          <xsl:apply-templates select="current-group()/.[@text:style-name='TEI_authority_biography']" mode="teiHeader"/>
                        </note>
                    </xsl:if>
                </xsl:element>
            </xsl:for-each-group>
        </titleStmt>
        <publicationStmt>
<!--          <publisher></publisher>-->
          <!-- date de réception -->
          <xsl:if test="//text:p[@text:style-name='TEI_date_reception']">
              <date type="received"><xsl:value-of select="//text:p[@text:style-name='TEI_date_reception']"/></date>
          </xsl:if>
          <!-- date d'acceptation' -->
          <xsl:if test="//text:p[@text:style-name='TEI_date_acceptance']">
              <date type="accepted"><xsl:value-of select="//text:p[@text:style-name='TEI_date_acceptance']"/></date>
          </xsl:if>
<!-- blocs <ab> Métopes [todo] -->
            <ab type="site" subtype="openedition">
    <!-- /!\ distributor cause l'invalidité du fichier TEI (schéma TEI all) 
                <distributor></distributor>
                -->            
                <date type="publishing">
<!--                    when=""-->
                    <xsl:comment>Date de publication en ligne</xsl:comment>
                </date>
                <date type="embargoend">
<!--                     when=""-->
                    <xsl:comment>Date de fin d'embargo</xsl:comment>
                </date>
<!-- bloc numéro du document inséré par défaut (cas imaginé : saisie de métadonnées dans une interface) -->
                <idno type="documentnumber">
                    <xsl:value-of select="//text:p[@text:style-name='TEI_document_number']"/>
                </idno>
                <idno type="DOI"></idno>
                <idno type="URL"></idno>
    <!-- /!\ élément availability invalide ici en TEI (pour Métopes) -->
<!--                <availability><xsl:comment>Licence</xsl:comment></availability>-->
            </ab>
            <ab type="print">
    <!-- /!\ distributor cause l'invalidité du ficheir TEI (schéma TEI all) 
                <distributor></distributor>
                -->  
                <date type="publishing">
<!--        when=""            -->
                    <xsl:comment>Date de publication papier</xsl:comment>
                </date>
                <dimensions>
                    <dim type="pagination">
                        <xsl:value-of select="//text:p[@text:style-name='TEI_pagination']"/>
                    </dim>
                </dimensions>
                <idno type="book"></idno>
            </ab>
        </publicationStmt>
        <sourceDesc>
          <p>COMMONS/Métopes : 1.0</p>
        </sourceDesc>
      </fileDesc>
      <encodingDesc>
        <p>L'encodage de ce fichier a été produit au moyen des outils Métopes.</p>
        <xsl:if test="not(//meta:user-defined[@meta:name='tplVersion'])">
            <FATAL>
                <xsl:text>WRONG WORD TEMPLATE USED</xsl:text>
          </FATAL>
        </xsl:if>
        <appInfo>
            <application ident="Word-tpl">
                <xsl:attribute name="version">
                    <xsl:value-of select="//meta:user-defined[@meta:name='tplVersion']"/>
                </xsl:attribute>
                <label>Word template</label>
                <desc>Version du modèle de stylage utilisé</desc>
                <ref target="#"/>
            </application>
            <application ident="circe" version="0.0.44">
                <label>Circé</label>
                <desc>Document converti en TEI avec l'application Circé</desc>
                <ref target="#"/>
            </application>
        </appInfo>
    <!-- génération conditionnelle du tagsDecl : ajouter test table -->
          <xsl:if test="//text:list or //*[starts-with(@rendition,'#')]">
            <tagsDecl>
            <xsl:comment>l'élément tagsDecl peut-il être vide ? sinon, conditionner à la présence de listes ou de tableaux</xsl:comment>
            <xsl:if test="//*[@rendition='#rtl']">
                <rendition scheme="css" xml:id="rtl">direction:right-to-left;</rendition>
            </xsl:if>
            <!-- traitement exhaustif cas par cas car syntaxe des instructions CSS parfois différentes de la valeur de l'@rendition -->
            <xsl:if test="//*[@rendition='#center']">
                <rendition scheme="css" xml:id="center">
                    <xsl:text>text-align:center;</xsl:text>
                </rendition>
            </xsl:if>
            <xsl:if test="//*[@rendition='#justify']">
                <rendition scheme="css" xml:id="justify">
                    <xsl:text>text-align:justify;</xsl:text>
                </rendition>
            </xsl:if>
            <xsl:if test="//*[@rendition='#end']">
                <rendition scheme="css" xml:id="end">
                    <xsl:text>text-align:end;</xsl:text>
                </rendition>
            </xsl:if>
            <!-- liste des valeurs : disc, square, circle | decimal, lower-roman, upper-roman, lower-alpha, upper-alpha -->
              <xsl:if test="//text:list/@style:num-format='1'"><rendition scheme="css" xml:id="list-decimal">list-style-type:decimal;</rendition></xsl:if>
              <xsl:if test="//text:list/@style:num-format='i'"><rendition scheme="css" xml:id="list-lower-roman">list-style-type:lower-roman;</rendition></xsl:if>
              <xsl:if test="//text:list/@style:num-format='I'"><rendition scheme="css" xml:id="list-upper-roman">list-style-type:upper-roman;</rendition></xsl:if>
              <xsl:if test="//text:list/@style:num-format='a'"><rendition scheme="css" xml:id="list-lower-alpha">list-style-type:lower-alpha;</rendition></xsl:if>
              <xsl:if test="//text:list/@style:num-format='A'"><rendition scheme="css" xml:id="list-upper-alpha">list-style-type:upper-alpha;</rendition></xsl:if>
              <xsl:if test="//text:list/@text:bullet-char='■'"><rendition scheme="css" xml:id="list-square">list-style-type:square;</rendition></xsl:if>
              <xsl:if test="//text:list/@text:bullet-char='○'"><rendition scheme="css" xml:id="list-circle">list-style-type:circle;</rendition></xsl:if>
              <xsl:if test="//text:list/@text:bullet-char='●'"><rendition scheme="css" xml:id="list-disc">list-style-type:disc;</rendition></xsl:if>
              <!-- définir un comportement si autre cas rencontré ? -->
            </tagsDecl>
        </xsl:if>
    <!-- rendu des cellules de tableaux -->
        <xsl:if test="//table:table">
            <tagsDecl>
                <xsl:for-each select="//style:style[@style:family='table-cell']">
                    <xsl:variable name="cellKey">
                        <xsl:analyze-string select="@style:name" regex="(\d+)\.[A-Z](\d+)">
                          <xsl:matching-substring>
                              <xsl:value-of select="."/>
                          </xsl:matching-substring>
                          <xsl:non-matching-substring/>
                        </xsl:analyze-string>
                    </xsl:variable>
                    <rendition scheme="css">
                        <xsl:attribute name="xml:id">
                            <xsl:value-of select="concat('Cell',$cellKey)"/>
                        </xsl:attribute>
                        <xsl:variable name="cellRendition">
                            <xsl:if test="child::style:table-cell-properties/@fo:border">
                                <xsl:value-of select="concat(string-join((local-name(child::style:table-cell-properties/@fo:border),child::style:table-cell-properties/@fo:border), ':'),'; ')"/>
                            </xsl:if>
                            <xsl:if test="child::style:table-cell-properties/@fo:border-top">
                                <xsl:value-of select="concat(string-join((local-name(child::style:table-cell-properties/@fo:border-top),child::style:table-cell-properties/@fo:border-top), ':'),'; ')"/>
                            </xsl:if>
                            <xsl:if test="child::style:table-cell-properties/@fo:border-right">
                                <xsl:value-of select="concat(string-join((local-name(child::style:table-cell-properties/@fo:border-right),child::style:table-cell-properties/@fo:border-right), ':'),'; ')"/>
                            </xsl:if>
                            <xsl:if test="child::style:table-cell-properties/@fo:border-bottom">
                                <xsl:value-of select="concat(string-join((local-name(child::style:table-cell-properties/@fo:border-bottom),child::style:table-cell-properties/@fo:border-bottom), ':'),'; ')"/>
                            </xsl:if>
                            <xsl:if test="child::style:table-cell-properties/@fo:border-left">
                                <xsl:value-of select="concat(string-join((local-name(child::style:table-cell-properties/@fo:border-left),child::style:table-cell-properties/@fo:border-left), ':'),'; ')"/>
                            </xsl:if>
                            <xsl:if test="child::style:table-cell-properties/@fo:background-color">
                                <xsl:value-of select="concat(string-join((local-name(child::style:table-cell-properties/@fo:background-color),child::style:table-cell-properties/@fo:background-color), ':'),'; ')"/>
                            </xsl:if>
                            <xsl:if test="child::style:table-cell-properties/@style:vertical-align">
                                <xsl:value-of select="concat(string-join((local-name(child::style:table-cell-properties/@style:vertical-align),child::style:table-cell-properties/@style:vertical-align), ':'),'; ')"/>
                            </xsl:if>
                        </xsl:variable>
                        <xsl:value-of select="$cellRendition"/>
                    </rendition>
                </xsl:for-each>
            </tagsDecl>
        </xsl:if>
        <editorialDecl>
            <normalization rendition="notes">
                <p rendition="note" select="restart"/>
                <p rendition="table" select="restart"/>
                <p rendition="annexe" select="restart"/>
                <p rendition="floatingText" select="restart"/>
            </normalization>
        </editorialDecl>
      </encodingDesc>
      <profileDesc>
        <langUsage>
          <language>
              <!-- diff Métopes/OE : combien de code de langue -->
              <xsl:attribute name="ident">
                  <xsl:value-of select="//text:p[@text:style-name='TEI_language']"/>
              </xsl:attribute>
          </language>
        </langUsage>
        <!-- mots-clés -->
        <xsl:if test="//text:p[starts-with(@text:style-name,'TEI_keywords')]">
            <textClass>
                <xsl:for-each select="//text:p[starts-with(@text:style-name,'TEI_keywords')]">
                    <xsl:call-template name="keywords"/>
                </xsl:for-each>
            </textClass>
        </xsl:if>
      </profileDesc>
<!--
      <revisionDesc>
          <listChange>
              <change type="##">
                  <xsl:attribute name="when">
                      <xsl:value-of select="current-date()"/>
                  </xsl:attribute>
                  <xsl:text>XML-TEI file created</xsl:text>
              </change>
          </listChange>
      </revisionDesc>
-->
    </teiHeader>
</xsl:template>

<xsl:template match="text:h[@text:outline-level='0']" mode="front">
    <xsl:apply-templates/>
</xsl:template>
    
<xsl:template match="text:p[starts-with(@text:style-name,'TEI_author:')]" mode="teiHeader">
    <persName>
        <xsl:variable name="name"><xsl:value-of select="normalize-space(.)"/></xsl:variable>
        <xsl:variable name="surname"><xsl:value-of select="tokenize($name,' ')[last()]"/></xsl:variable>
        <forename><xsl:value-of select="normalize-space(substring-before($name,$surname))"/></forename>
        <surname><xsl:value-of select="$surname"/></surname>
    </persName>
</xsl:template>
    
<xsl:template match="text:p[starts-with(@text:style-name,'TEI_editor:')]" mode="teiHeader">
    <persName>
        <xsl:variable name="name"><xsl:value-of select="normalize-space(.)"/></xsl:variable>
        <xsl:variable name="surname"><xsl:value-of select="tokenize($name,' ')[last()]"/></xsl:variable>
        <forename><xsl:value-of select="normalize-space(substring-before($name,$surname))"/></forename>
        <surname><xsl:value-of select="$surname"/></surname>
    </persName>
</xsl:template>
    
<xsl:template match="text:p[@text:style-name='TEI_authority_affiliation']" mode="teiHeader">
    <affiliation>
        <orgName>
            <xsl:apply-templates/>
        </orgName>
    </affiliation>
</xsl:template>
    
<xsl:template match="text:p[@text:style-name='TEI_authority_mail']" mode="teiHeader">
    <email>
        <xsl:apply-templates select=".//text()"/>
    </email>
</xsl:template>
    
<xsl:template match="text:p[@text:style-name='TEI_authority_biography']" mode="teiHeader">
    <p>
        <xsl:apply-templates/>
    </p>
</xsl:template>
    
<xsl:template match="text:p[starts-with(@text:style-name,'TEI_author:')]|text:p[starts-with(@text:style-name,'TEI_editor')]">
    <xsl:choose>
        <xsl:when test="ancestor::*:div[@type='review']">
<!--            <xsl:comment>author and editor mode review</xsl:comment>-->
            <docAuthor>
                <name><xsl:apply-templates/></name>
                <xsl:if test="following-sibling::text:*[1][@text:style-name='TEI_authority_affiliation']">
                    <affiliation><xsl:apply-templates select="following-sibling::text:*[1][@text:style-name='TEI_authority_affiliation']" mode="preserve"/></affiliation>
                </xsl:if>
            </docAuthor>
        </xsl:when>
        <xsl:otherwise/>
    </xsl:choose>
</xsl:template>
    
<xsl:template match="text:p[@text:style-name='TEI_authority_affiliation']" mode="preserve">
    <xsl:apply-templates/>
</xsl:template>

<xsl:template name="keywords">
    <keywords>
        <xsl:copy-of select="@xml:lang"/>
        <xsl:if test="ends-with(@text:style-name,'keywords')">
            <xsl:attribute name="scheme">keyword</xsl:attribute>
        </xsl:if>
        <xsl:if test="contains(@text:style-name,'keywords_subjects:')">
            <xsl:attribute name="scheme" select="substring-after(@text:style-name,'keywords_subjects:')"/>
        </xsl:if>
        
        <list>
            <xsl:variable name="list">
                <xsl:choose>
                    <xsl:when test="contains(.,':')">
                        <xsl:value-of select="substring-after(., ': ')"/>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:value-of select="."/>
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:variable>
            <xsl:choose>
            <!-- personcited -->
                <xsl:when test="contains(@text:style-name,'personcited')">
                    <xsl:call-template name="keyWordsListPC">
                        <xsl:with-param name="list">
                            <xsl:value-of select="$list"/>
                        </xsl:with-param>
                    </xsl:call-template>
                </xsl:when>
            <!-- autres listes de mc -->
                <xsl:otherwise>
                    <xsl:call-template name="keyWordsList">
                        <xsl:with-param name="list">
                            <xsl:value-of select="$list"/>
                        </xsl:with-param>
                    </xsl:call-template>
                </xsl:otherwise>
            </xsl:choose>         
        </list>
    </keywords>
</xsl:template>

<xsl:template name="keyWordsList">
    <xsl:param name="list"/>
    <xsl:variable name="first" select="substring-before($list, ', ')" />
    <xsl:variable name="remaining" select="substring-after($list, ', ')" />
    <xsl:choose>
        <xsl:when test="$first">
            <item><xsl:value-of select="$first"/></item>
            <xsl:if test="$remaining">
                <xsl:call-template name="keyWordsList">
                    <xsl:with-param name="list" select="$remaining" />
                </xsl:call-template>
            </xsl:if>
        </xsl:when>
        <xsl:otherwise>
            <item><xsl:value-of select="$list"/></item>
        </xsl:otherwise>
    </xsl:choose>
</xsl:template>
    
<xsl:template name="keyWordsListPC">
    <xsl:param name="list"/>
    <xsl:variable name="first" select="substring-before($list, ', ')" />
    <xsl:variable name="remaining" select="substring-after($list, ', ')" />
    <xsl:choose>
        <xsl:when test="$first">
            <xsl:variable name="surname"><xsl:value-of select="tokenize(substring-before($list, ', '),' ')[last()]"/></xsl:variable>
            <item>
                <persName>
                    <forename>
                        <xsl:value-of select="normalize-space(substring-before($first,$surname))"/>
                    </forename>
                    <surname>
                        <xsl:value-of select="$surname"/>
                    </surname>
                </persName>
            </item>
            <xsl:if test="$remaining">
                <xsl:call-template name="keyWordsListPC">
                    <xsl:with-param name="list" select="$remaining" />
                </xsl:call-template>
            </xsl:if>
        </xsl:when>
        <xsl:otherwise>
            <xsl:variable name="surname"><xsl:value-of select="tokenize(.,' ')[last()]"/></xsl:variable>
            <item>
                <persName>
                    <forename>
                        <xsl:value-of select="normalize-space(substring-before($list,$surname))"/>
<!--                        <xsl:value-of select="normalize-space(substring-before($first,$surname))"/>-->
                    </forename>
                    <surname>
                        <xsl:value-of select="$surname"/>
                    </surname>
                </persName>
            </item>
        </xsl:otherwise>
    </xsl:choose>
</xsl:template>
    
<xsl:template match="//text:h[@text:outline-level='0']"/>
<xsl:template match="//text:p[@text:style-name='title-sup']"/>
<xsl:template match="//text:p[@text:style-name='TEI_date_reception']"/>
<xsl:template match="//text:p[@text:style-name='TEI_date_acceptance']"/>
<xsl:template match="//text:p[starts-with(@text:style-name,'TEI_keywords')]"/>
<xsl:template match="//text:p[@text:style-name='TEI_language']"/>
<xsl:template match="//text:p[@text:style-name='TEI_pagination']"/>
<xsl:template match="//text:p[@text:style-name='TEI_document_number']"/>
<xsl:template match="text:p[@text:style-name='TEI_authority_affiliation']"/>
    
</xsl:stylesheet>