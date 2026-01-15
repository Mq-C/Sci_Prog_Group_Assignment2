<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" version="1.0.0" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc">
  <UserLayer>
    <sld:LayerFeatureConstraints>
      <sld:FeatureTypeConstraint/>
    </sld:LayerFeatureConstraints>
    <sld:UserStyle>
      <sld:Name>EMSN177_FLEX_AOI01_P05MODFLMIT02_maxWaterDepth_v01.tif</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:ChannelSelection>
              <sld:GrayChannel>
                <sld:SourceChannelName>1</sld:SourceChannelName>
              </sld:GrayChannel>
            </sld:ChannelSelection>
            <sld:ColorMap type="intervals">
              <sld:ColorMapEntry color="#00f5f5" quantity="0.20000000000000001" label="0 - 0.2"/>
              <sld:ColorMapEntry color="#36a4f7" quantity="0.5" label="> 0.2 - 0.5"/>
              <sld:ColorMapEntry color="#345bf7" quantity="1" label="> 0.5 - 1"/>
              <sld:ColorMapEntry color="#0000f5" quantity="2" label="> 1 - 2"/>
              <sld:ColorMapEntry color="#6e00f5" quantity="5" label="> 2 - 5"/>
              <sld:ColorMapEntry color="#b400f5" quantity="8" label="> 5 - 8"/>
              <sld:ColorMapEntry color="#f500f5" quantity="8.7201004028320313" label="> 8"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </UserLayer>
</StyledLayerDescriptor>
