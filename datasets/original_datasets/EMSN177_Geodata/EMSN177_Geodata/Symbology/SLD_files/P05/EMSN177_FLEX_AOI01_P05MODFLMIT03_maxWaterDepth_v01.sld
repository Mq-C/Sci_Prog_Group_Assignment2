<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:sld="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" version="1.0.0">
  <UserLayer>
    <sld:LayerFeatureConstraints>
      <sld:FeatureTypeConstraint/>
    </sld:LayerFeatureConstraints>
    <sld:UserStyle>
      <sld:Name>EMSN177_FLEX_AOI01_P05MODFLMIT03_maxWaterDepth_v01.tif</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:ChannelSelection>
              <sld:GrayChannel>
                <sld:SourceChannelName>1</sld:SourceChannelName>
              </sld:GrayChannel>
            </sld:ChannelSelection>
            <sld:ColorMap type="intervals">
              <sld:ColorMapEntry label="0 -0.2" quantity="0.20000000000000001" color="#00f5f5"/>
              <sld:ColorMapEntry label="> 0.2 - 0.5" quantity="0.5" color="#36a4f7"/>
              <sld:ColorMapEntry label="> 0.5 - 1" quantity="1" color="#345bf7"/>
              <sld:ColorMapEntry label="> 1 - 2" quantity="2" color="#0000f5"/>
              <sld:ColorMapEntry label="> 2 - 5" quantity="5" color="#6e00f5"/>
              <sld:ColorMapEntry label="> 5" quantity="9" color="#b400f5"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </UserLayer>
</StyledLayerDescriptor>
