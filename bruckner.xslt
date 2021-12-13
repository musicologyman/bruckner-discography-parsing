<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml" indent="yes" />

    <xsl:template match="/|div[@id='content']">
        <discography>
            <xsl:apply-templates select="//div[@class='recordingheading']" />
        </discography>
    </xsl:template>

    <xsl:template match="div[@class='recordingheading']">
        <!--<xsl:if test="font[@size='3']/text()!='Transcriptions'">-->
        <work>
            <title>
                <xsl:value-of select="normalize-space(font[@size='5'])" />
            </title>
            <version>
                <xsl:value-of select="normalize-space(font[@size='3'])" />
            </version>
            <recordings>
                <xsl:apply-templates select="following-sibling::div[@class='row']" />
            </recordings>
        </work>
        <!--</xsl:if>-->
    </xsl:template>

    <xsl:template match="div[@class='row']">
        <recording>
            <xsl:apply-templates select="div[@class='even']" />
            <date>
                <xsl:value-of select="normalize-space(div[@class='odd']/div[@class='col1']/b)" />
            </date>
            <label_number>
                <xsl:choose>
                    <xsl:when test="div[@class='odd']/div[@class='col1']/a">
                        <xsl:value-of select="normalize-space(div[@class='odd']/div[@class='col1']/a/text())" />
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:value-of
                            select="normalize-space(substring(normalize-space(div[@class='odd']/div[@class='col1']/b/following-sibling::text()[1]),2))" />
                    </xsl:otherwise>
                </xsl:choose>
            </label_number>
            <timings>
                <total_time>
                    <timing><xsl:value-of select="normalize-space(div[@class='odd']/div[@class='col5']/b)" /></timing>
                </total_time>
                <xsl:if test="string-length(normalize-space(div[@class='odd']/div[@class='col5'][2])) &gt; 0">
                    <movement>
                    	<number>1</number>
                        <timing><xsl:value-of select="normalize-space(div[@class='odd']/div[@class='col5'][2])" /></timing>
                    </movement>
                </xsl:if>
                <xsl:if test="string-length(normalize-space(div[@class='odd']/div[@class='col5'][3])) &gt; 0">
                    <movement>
                    	<number>2</number>
                        <timing>
                            <xsl:value-of select="normalize-space(div[@class='odd']/div[@class='col5'][3])" />
                        </timing>
                    </movement>
                </xsl:if>
                <xsl:if test="string-length(normalize-space(div[@class='odd']/div[@class='col5'][4])) &gt; 0">
                    <movement>
                    	<number>3</number>
                        <timing>
                            <xsl:value-of select="normalize-space(div[@class='odd']/div[@class='col5'][4])" />
                        </timing>
                    </movement>
                </xsl:if>
                <xsl:if test="div[@class='odd']/div[@class='col5'][5]">
                    <xsl:if test="string-length(normalize-space(div[@class='odd']/div[@class='col5'][5])) &gt; 0">
                        <movement>
                        	<number>4</number>
                            <timing>
                                <xsl:value-of select="normalize-space(div[@class='odd']/div[@class='col5'][5])" />
                            </timing>
                        </movement>
                    </xsl:if>
                </xsl:if>
            </timings>
        </recording>
    </xsl:template>

    <xsl:template match="div[@class='even']">
        <conductor>
            <xsl:value-of select="normalize-space(div[@class='col2'][1]/a/text())" />
        </conductor>
        <orchestra>
            <xsl:value-of select="normalize-space(div[@class='col2'][2]/a/text())" />
        </orchestra>
    </xsl:template>

</xsl:stylesheet>
