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
                <xsl:value-of select="font[@size='5']" />
            </title>
            <version>
                <xsl:value-of select="font[@size='3']" />
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
                <xsl:value-of select="div[@class='odd']/div[@class='col1']/b" />
            </date>
            <label_number>
                <xsl:choose>
                    <xsl:when test="div[@class='odd']/div[@class='col1']/a">
                        <xsl:value-of select="normalize-space(div[@class='odd']/div[@class='col1']/a/text())" />
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:value-of
                            select="normalize-space(//div[@class='odd']/div[@class='col1']/b/following-sibling::node()[2])" />
                    </xsl:otherwise>
                </xsl:choose>
            </label_number>
            <timings>
                <total_time>
                    <xsl:value-of select="normalize-space(div[@class='odd']/div[@class='col5']/b)" />
                </total_time>
                <xsl:if test="string-length(normalize-space(div[@class='odd']/div[@class='col5'][2])) &gt; 0">
                    <mvmt number="1">
                        <xsl:value-of select="normalize-space(div[@class='odd']/div[@class='col5'][2])" />
                    </mvmt>
                </xsl:if>
                <xsl:if test="string-length(normalize-space(div[@class='odd']/div[@class='col5'][3])) &gt; 0">
                    <mvmt number="2">
                        <xsl:value-of select="normalize-space(div[@class='odd']/div[@class='col5'][3])" />
                    </mvmt>
                </xsl:if>
                <xsl:if test="string-length(normalize-space(div[@class='odd']/div[@class='col5'][4])) &gt; 0">
                    <mvmt number="3">
                        <xsl:value-of select="normalize-space(div[@class='odd']/div[@class='col5'][4])" />
                    </mvmt>
                </xsl:if>
                <xsl:if test="div[@class='odd']/div[@class='col5'][5]">
                    <xsl:if test="string-length(normalize-space(div[@class='odd']/div[@class='col5'][5])) &gt; 0">
                        <mvmt number="4">
                            <xsl:value-of select="normalize-space(div[@class='odd']/div[@class='col5'][5])" />
                        </mvmt>
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
