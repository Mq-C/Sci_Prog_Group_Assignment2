<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:se="http://www.opengis.net/se" version="1.1.0" xmlns:ogc="http://www.opengis.net/ogc" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xlink="http://www.w3.org/1999/xlink">
  <NamedLayer>
    <se:Name>EMSN177_FLEX_AOI01_P03EXP02_IndustryA_v01</se:Name>
    <UserStyle>
      <se:Name>EMSN177_FLEX_AOI01_P03EXP02_IndustryA_v01</se:Name>
      <se:FeatureTypeStyle>
        <se:Rule>
          <se:Name>Breakwater, 0.2-0.5</se:Name>
          <se:Description>
            <se:Title>Breakwater, 0.2-0.5</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>obj_type</ogc:PropertyName>
                <ogc:Literal>Breakwater</ogc:Literal>
              </ogc:PropertyIsEqualTo>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>exp_m_clas</ogc:PropertyName>
                <ogc:Literal>0.2-0.5</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:And>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#73c2ff</se:SvgParameter>
            </se:Fill>
            <se:Stroke>
              <se:SvgParameter name="stroke">#6edfff</se:SvgParameter>
              <se:SvgParameter name="stroke-width">1</se:SvgParameter>
              <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
            </se:Stroke>
          </se:PolygonSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Dam, 0.5-1</se:Name>
          <se:Description>
            <se:Title>Dam, 0.5-1</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>obj_type</ogc:PropertyName>
                <ogc:Literal>Dam</ogc:Literal>
              </ogc:PropertyIsEqualTo>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>exp_m_clas</ogc:PropertyName>
                <ogc:Literal>0.5-1</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:And>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#268fff</se:SvgParameter>
            </se:Fill>
            <se:Stroke>
              <se:SvgParameter name="stroke">#732600</se:SvgParameter>
              <se:SvgParameter name="stroke-width">1</se:SvgParameter>
              <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
            </se:Stroke>
          </se:PolygonSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Dam, 2-5</se:Name>
          <se:Description>
            <se:Title>Dam, 2-5</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>obj_type</ogc:PropertyName>
                <ogc:Literal>Dam</ogc:Literal>
              </ogc:PropertyIsEqualTo>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>exp_m_clas</ogc:PropertyName>
                <ogc:Literal>2-5</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:And>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#0041a8</se:SvgParameter>
            </se:Fill>
            <se:Stroke>
              <se:SvgParameter name="stroke">#732600</se:SvgParameter>
              <se:SvgParameter name="stroke-width">1</se:SvgParameter>
              <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
            </se:Stroke>
          </se:PolygonSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Extraction mine, 2-5</se:Name>
          <se:Description>
            <se:Title>Extraction mine, 2-5</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>obj_type</ogc:PropertyName>
                <ogc:Literal>Extraction mine</ogc:Literal>
              </ogc:PropertyIsEqualTo>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>exp_m_clas</ogc:PropertyName>
                <ogc:Literal>2-5</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:And>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#0041a8</se:SvgParameter>
            </se:Fill>
            <se:Stroke>
              <se:SvgParameter name="stroke">#000000</se:SvgParameter>
              <se:SvgParameter name="stroke-width">1.5</se:SvgParameter>
              <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
            </se:Stroke>
          </se:PolygonSymbolizer>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:GraphicFill>
                <se:Graphic>
                  <se:ExternalGraphic>
                    <se:OnlineResource xlink:href="EMSN177_FLEX_AOI01_P3EXP02_IndustryA_v01.png" xlink:type="simple"/>
                    <se:Format>image/png</se:Format>
                  </se:ExternalGraphic>
                  <se:Size>8</se:Size>
                </se:Graphic>
              </se:GraphicFill>
            </se:Fill>
          </se:PolygonSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Processing facility, 1-2</se:Name>
          <se:Description>
            <se:Title>Processing facility, 1-2</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>obj_type</ogc:PropertyName>
                <ogc:Literal>Processing facility</ogc:Literal>
              </ogc:PropertyIsEqualTo>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>exp_m_clas</ogc:PropertyName>
                <ogc:Literal>1-2</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:And>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#005ee0</se:SvgParameter>
            </se:Fill>
            <se:Stroke>
              <se:SvgParameter name="stroke">#a87000</se:SvgParameter>
              <se:SvgParameter name="stroke-width">1</se:SvgParameter>
              <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
            </se:Stroke>
          </se:PolygonSymbolizer>
        </se:Rule>
      </se:FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
