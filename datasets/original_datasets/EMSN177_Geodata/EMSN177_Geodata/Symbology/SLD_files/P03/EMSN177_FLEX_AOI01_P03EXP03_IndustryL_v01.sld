<?xml version="1.0" encoding="ISO-8859-1" standalone="yes"?>
<sld:StyledLayerDescriptor version="1.0.0" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xlink="http://www.w3.org/1999/xlink">
  <sld:NamedLayer>
    <sld:Name>P03EXP03_industryL</sld:Name>
    <sld:UserStyle>
      <sld:Name>Style1</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:FeatureTypeName>P03EXP03_industryL</sld:FeatureTypeName>
        <sld:Rule>
          <sld:Name>0.001-0.2</sld:Name>
          <sld:Title>0.001-0.2</sld:Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>exp03_clas</ogc:PropertyName>
              <ogc:Literal>0.001-0.2</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <sld:LineSymbolizer>
            <sld:Stroke>
              <sld:CssParameter name="stroke">#006100</sld:CssParameter>
              <sld:CssParameter name="stroke-width">2.25</sld:CssParameter>
              <sld:CssParameter name="stroke-opacity">1</sld:CssParameter>
            </sld:Stroke>
          </sld:LineSymbolizer>
        </sld:Rule>
        <sld:Rule>
          <sld:Name>0.2-0.5</sld:Name>
          <sld:Title>0.2-0.5</sld:Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>exp03_clas</ogc:PropertyName>
              <ogc:Literal>0.2-0.5</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <sld:LineSymbolizer>
            <sld:Stroke>
              <sld:CssParameter name="stroke">#619900</sld:CssParameter>
              <sld:CssParameter name="stroke-width">2.25</sld:CssParameter>
              <sld:CssParameter name="stroke-opacity">1</sld:CssParameter>
            </sld:Stroke>
          </sld:LineSymbolizer>
        </sld:Rule>
        <sld:Rule>
          <sld:Name>0.5-1</sld:Name>
          <sld:Title>0.5-1</sld:Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>exp03_clas</ogc:PropertyName>
              <ogc:Literal>0.5-1</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <sld:LineSymbolizer>
            <sld:Stroke>
              <sld:CssParameter name="stroke">#C5DB00</sld:CssParameter>
              <sld:CssParameter name="stroke-width">2.25</sld:CssParameter>
              <sld:CssParameter name="stroke-opacity">1</sld:CssParameter>
            </sld:Stroke>
          </sld:LineSymbolizer>
        </sld:Rule>
        <sld:Rule>
          <sld:Name>1-2</sld:Name>
          <sld:Title>1-2</sld:Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>exp03_clas</ogc:PropertyName>
              <ogc:Literal>1-2</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <sld:LineSymbolizer>
            <sld:Stroke>
              <sld:CssParameter name="stroke">#FFD900</sld:CssParameter>
              <sld:CssParameter name="stroke-width">2.25</sld:CssParameter>
              <sld:CssParameter name="stroke-opacity">1</sld:CssParameter>
            </sld:Stroke>
          </sld:LineSymbolizer>
        </sld:Rule>
        <sld:Rule>
          <sld:Name>2-5</sld:Name>
          <sld:Title>2-5</sld:Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>exp03_clas</ogc:PropertyName>
              <ogc:Literal>2-5</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <sld:LineSymbolizer>
            <sld:Stroke>
              <sld:CssParameter name="stroke">#FF8400</sld:CssParameter>
              <sld:CssParameter name="stroke-width">2.25</sld:CssParameter>
              <sld:CssParameter name="stroke-opacity">1</sld:CssParameter>
            </sld:Stroke>
          </sld:LineSymbolizer>
        </sld:Rule>
        <sld:Rule>
          <sld:Name>&gt;5</sld:Name>
          <sld:Title>&gt;5</sld:Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>exp03_clas</ogc:PropertyName>
              <ogc:Literal>&gt;5</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <sld:LineSymbolizer>
            <sld:Stroke>
              <sld:CssParameter name="stroke">#FF2600</sld:CssParameter>
              <sld:CssParameter name="stroke-width">2.25</sld:CssParameter>
              <sld:CssParameter name="stroke-opacity">1</sld:CssParameter>
            </sld:Stroke>
          </sld:LineSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </sld:NamedLayer>
</sld:StyledLayerDescriptor>