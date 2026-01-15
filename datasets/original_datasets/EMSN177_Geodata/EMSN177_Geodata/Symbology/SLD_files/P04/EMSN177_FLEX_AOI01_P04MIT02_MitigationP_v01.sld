<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ogc="http://www.opengis.net/ogc" version="1.1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd" xmlns:se="http://www.opengis.net/se">
  <NamedLayer>
    <se:Name>EMSN177_FLEX_AOI01_P04MIT_MitigationP_v01</se:Name>
    <UserStyle>
      <se:Name>EMSN177_FLEX_AOI01_P04MIT_MitigationP_v01</se:Name>
      <se:FeatureTypeStyle>
        <se:Rule>
          <se:Name>New culvert</se:Name>
          <se:Description>
            <se:Title>New culvert</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>Type</ogc:PropertyName>
                <ogc:Literal>New culvert</ogc:Literal>
              </ogc:PropertyIsEqualTo>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>UC_100</ogc:PropertyName>
                <ogc:Literal>Yes</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:And>
          </ogc:Filter>
          <se:PointSymbolizer>
            <se:Graphic>
              <se:Mark>
                <se:WellKnownName>circle</se:WellKnownName>
                <se:Fill>
                  <se:SvgParameter name="fill">#a3ff73</se:SvgParameter>
                </se:Fill>
                <se:Stroke>
                  <se:SvgParameter name="stroke">#232323</se:SvgParameter>
                  <se:SvgParameter name="stroke-width">0.5</se:SvgParameter>
                </se:Stroke>
              </se:Mark>
              <se:Size>15</se:Size>
            </se:Graphic>
          </se:PointSymbolizer>
          <se:PointSymbolizer>
            <se:Graphic>
              <se:Mark>
                <se:OnlineResource xlink:href="ttf://Arial" xlink:type="simple"/>
                <se:Format>ttf</se:Format>
                <se:MarkIndex>67</se:MarkIndex>
                <se:Fill>
                  <se:SvgParameter name="fill">#000000</se:SvgParameter>
                </se:Fill>
              </se:Mark>
              <se:Size>10</se:Size>
              <se:Displacement>
                <se:DisplacementX>0</se:DisplacementX>
                <se:DisplacementY>-1</se:DisplacementY>
              </se:Displacement>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
      </se:FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
