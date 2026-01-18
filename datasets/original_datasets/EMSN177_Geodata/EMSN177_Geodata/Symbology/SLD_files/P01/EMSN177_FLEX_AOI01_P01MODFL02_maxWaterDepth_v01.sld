<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" version="1.0.0" xmlns:ogc="http://www.opengis.net/ogc" xmlns:gml="http://www.opengis.net/gml" xmlns:sld="http://www.opengis.net/sld">
  <UserLayer>
    <sld:LayerFeatureConstraints>
      <sld:FeatureTypeConstraint/>
    </sld:LayerFeatureConstraints>
    <sld:UserStyle>
      <sld:Name>EMSN177_FLEX_AOI01_P01MODFL02_maxWaterDepth_v01</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:ChannelSelection>
              <sld:GrayChannel>
                <sld:SourceChannelName>1</sld:SourceChannelName>
              </sld:GrayChannel>
            </sld:ChannelSelection>
            <sld:ColorMap type="intervals">
              <sld:ColorMapEntry quantity="0.20000000000000001" color="#00f5f5" label="0 - 0.2"/>
              <sld:ColorMapEntry quantity="0.5" color="#36a4f7" label="> 0.2 - 0.5"/>
              <sld:ColorMapEntry quantity="1" color="#345bf7" label="> 0.5 - 1"/>
              <sld:ColorMapEntry quantity="2" color="#0000f5" label="> 1 - 2"/>
              <sld:ColorMapEntry quantity="5" color="#6e00f5" label="> 2 - 5"/>
              <sld:ColorMapEntry quantity="8" color="#b400f5" label="> 5 - 8"/>
              <sld:ColorMapEntry quantity="8.7201004028320313" color="#f500f5" label="> 8"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </UserLayer>
</StyledLayerDescriptor>
