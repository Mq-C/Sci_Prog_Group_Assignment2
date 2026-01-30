<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:se="http://www.opengis.net/se" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd" version="1.1.0">
  <NamedLayer>
    <se:Name>EMSN177_FLEX_AOI01_P04MIT01_MitigationP_v01</se:Name>
    <UserStyle>
      <se:Name>EMSN177_FLEX_AOI01_P04MIT01_MitigationP_v01</se:Name>
      <se:FeatureTypeStyle>
        <se:Rule>
          <se:Name>New culvert</se:Name>
          <se:Description>
            <se:Title>New culvert</se:Title>
            <se:Abstract>New culvert</se:Abstract>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>Type</ogc:PropertyName>
                <ogc:Literal>New culvert</ogc:Literal>
              </ogc:PropertyIsEqualTo>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>UC_500</ogc:PropertyName>
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
                  <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                  <se:SvgParameter name="stroke-width">0.5</se:SvgParameter>
                </se:Stroke>
              </se:Mark>
              <se:Size>13</se:Size>
            </se:Graphic>
          </se:PointSymbolizer>
          <se:PointSymbolizer>
            <se:Graphic>
              <!--Parametric SVG-->
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="base64:PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+Cjxzdmcgdmlld0JveD0iMC41NDc4NTIgLTguMDA4MyA2Ljk2MDk0IDguMTQyNTgiCiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiAgdmVyc2lvbj0iMS4yIiBiYXNlUHJvZmlsZT0idGlueSI+Cjx0aXRsZT5RdCBTVkcgRG9jdW1lbnQ8L3RpdGxlPgo8ZGVzYz5HZW5lcmF0ZWQgd2l0aCBRdDwvZGVzYz4KPGRlZnM+CjwvZGVmcz4KPGcgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIHN0cm9rZS1saW5lY2FwPSJzcXVhcmUiIHN0cm9rZS1saW5lam9pbj0iYmV2ZWwiID4KCjxnIGZpbGw9InBhcmFtKGZpbGwpIiBmaWxsLW9wYWNpdHk9InBhcmFtKGZpbGwtb3BhY2l0eSkiIHN0cm9rZT0icGFyYW0ob3V0bGluZSkiIHN0cm9rZS1vcGFjaXR5PSJwYXJhbShvdXRsaW5lLW9wYWNpdHkpIDEiIHN0cm9rZS13aWR0aD0icGFyYW0ob3V0bGluZS13aWR0aCkgMCIgdHJhbnNmb3JtPSJtYXRyaXgoMSwwLDAsMSwwLDApIgpmb250LWZhbWlseT0iTVMgU2hlbGwgRGxnIDIiIGZvbnQtc2l6ZT0iOC4yNSIgZm9udC13ZWlnaHQ9IjQwMCIgZm9udC1zdHlsZT0ibm9ybWFsIiAKPgo8cGF0aCB2ZWN0b3ItZWZmZWN0PSJub25lIiBmaWxsLXJ1bGU9Im5vbnplcm8iIGQ9Ik02LjQ2NjgsLTIuNzYwNzQgTDcuNTA4NzksLTIuNDk3NTYgQzcuMjkwMzYsLTEuNjQxNzYgNi44OTczOCwtMC45ODkxNzYgNi4zMjk4MywtMC41Mzk3OTUgQzUuNzYyMjksLTAuMDkwNDEzNCA1LjA2ODUyLDAuMTM0Mjc3IDQuMjQ4NTQsMC4xMzQyNzcgQzMuMzk5OSwwLjEzNDI3NyAyLjcwOTcyLC0wLjAzODQ5MjggMi4xNzc5OCwtMC4zODQwMzMgQzEuNjQ2MjQsLTAuNzI5NTc0IDEuMjQxNjIsLTEuMjI5OTggMC45NjQxMTEsLTEuODg1MjUgQzAuNjg2NjA1LC0yLjU0MDUzIDAuNTQ3ODUyLC0zLjI0NDE0IDAuNTQ3ODUyLC0zLjk5NjA5IEMwLjU0Nzg1MiwtNC44MTYwOCAwLjcwNDUwOCwtNS41MzEzMyAxLjAxNzgyLC02LjE0MTg1IEMxLjMzMTE0LC02Ljc1MjM2IDEuNzc2OTQsLTcuMjE2MDYgMi4zNTUyMiwtNy41MzI5NiBDMi45MzM1MSwtNy44NDk4NSAzLjU2OTk5LC04LjAwODMgNC4yNjQ2NSwtOC4wMDgzIEM1LjA1MjQxLC04LjAwODMgNS43MTQ4NCwtNy44MDc3OCA2LjI1MTk1LC03LjQwNjc0IEM2Ljc4OTA2LC03LjAwNTcgNy4xNjMyNSwtNi40NDE3MyA3LjM3NDUxLC01LjcxNDg0IEw2LjM0ODYzLC01LjQ3MzE0IEM2LjE2NjAyLC02LjA0NjA2IDUuOTAxMDQsLTYuNDYzMjIgNS41NTM3MSwtNi43MjQ2MSBDNS4yMDYzOCwtNi45ODYgNC43Njk1MywtNy4xMTY3IDQuMjQzMTYsLTcuMTE2NyBDMy42MzgwMiwtNy4xMTY3IDMuMTMyMjQsLTYuOTcxNjggMi43MjU4MywtNi42ODE2NCBDMi4zMTk0MiwtNi4zOTE2IDIuMDMzODUsLTYuMDAyMiAxLjg2OTE0LC01LjUxMzQzIEMxLjcwNDQzLC01LjAyNDY2IDEuNjIyMDcsLTQuNTIwNjcgMS42MjIwNywtNC4wMDE0NiBDMS42MjIwNywtMy4zMzE4NyAxLjcxOTY1LC0yLjc0NzMxIDEuOTE0NzksLTIuMjQ3OCBDMi4xMDk5NCwtMS43NDgyOSAyLjQxMzQxLC0xLjM3NSAyLjgyNTIsLTEuMTI3OTMgQzMuMjM2OTgsLTAuODgwODU5IDMuNjgyNzgsLTAuNzU3MzI0IDQuMTYyNiwtMC43NTczMjQgQzQuNzQ2MjYsLTAuNzU3MzI0IDUuMjQwNCwtMC45MjU2MTggNS42NDUwMiwtMS4yNjIyMSBDNi4wNDk2NCwtMS41OTg4IDYuMzIzNTcsLTIuMDk4MzEgNi40NjY4LC0yLjc2MDc0ICIvPgo8L2c+CjwvZz4KPC9zdmc+Cg==?fill=%23000000&amp;fill-opacity=1&amp;outline=%23232323&amp;outline-opacity=1&amp;outline-width=0"/>
                <se:Format>image/svg+xml</se:Format>
              </se:ExternalGraphic>
              <!--Plain SVG fallback, no parameters-->
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="base64:PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+Cjxzdmcgdmlld0JveD0iMC41NDc4NTIgLTguMDA4MyA2Ljk2MDk0IDguMTQyNTgiCiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiAgdmVyc2lvbj0iMS4yIiBiYXNlUHJvZmlsZT0idGlueSI+Cjx0aXRsZT5RdCBTVkcgRG9jdW1lbnQ8L3RpdGxlPgo8ZGVzYz5HZW5lcmF0ZWQgd2l0aCBRdDwvZGVzYz4KPGRlZnM+CjwvZGVmcz4KPGcgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIHN0cm9rZS1saW5lY2FwPSJzcXVhcmUiIHN0cm9rZS1saW5lam9pbj0iYmV2ZWwiID4KCjxnIGZpbGw9InBhcmFtKGZpbGwpIiBmaWxsLW9wYWNpdHk9InBhcmFtKGZpbGwtb3BhY2l0eSkiIHN0cm9rZT0icGFyYW0ob3V0bGluZSkiIHN0cm9rZS1vcGFjaXR5PSJwYXJhbShvdXRsaW5lLW9wYWNpdHkpIDEiIHN0cm9rZS13aWR0aD0icGFyYW0ob3V0bGluZS13aWR0aCkgMCIgdHJhbnNmb3JtPSJtYXRyaXgoMSwwLDAsMSwwLDApIgpmb250LWZhbWlseT0iTVMgU2hlbGwgRGxnIDIiIGZvbnQtc2l6ZT0iOC4yNSIgZm9udC13ZWlnaHQ9IjQwMCIgZm9udC1zdHlsZT0ibm9ybWFsIiAKPgo8cGF0aCB2ZWN0b3ItZWZmZWN0PSJub25lIiBmaWxsLXJ1bGU9Im5vbnplcm8iIGQ9Ik02LjQ2NjgsLTIuNzYwNzQgTDcuNTA4NzksLTIuNDk3NTYgQzcuMjkwMzYsLTEuNjQxNzYgNi44OTczOCwtMC45ODkxNzYgNi4zMjk4MywtMC41Mzk3OTUgQzUuNzYyMjksLTAuMDkwNDEzNCA1LjA2ODUyLDAuMTM0Mjc3IDQuMjQ4NTQsMC4xMzQyNzcgQzMuMzk5OSwwLjEzNDI3NyAyLjcwOTcyLC0wLjAzODQ5MjggMi4xNzc5OCwtMC4zODQwMzMgQzEuNjQ2MjQsLTAuNzI5NTc0IDEuMjQxNjIsLTEuMjI5OTggMC45NjQxMTEsLTEuODg1MjUgQzAuNjg2NjA1LC0yLjU0MDUzIDAuNTQ3ODUyLC0zLjI0NDE0IDAuNTQ3ODUyLC0zLjk5NjA5IEMwLjU0Nzg1MiwtNC44MTYwOCAwLjcwNDUwOCwtNS41MzEzMyAxLjAxNzgyLC02LjE0MTg1IEMxLjMzMTE0LC02Ljc1MjM2IDEuNzc2OTQsLTcuMjE2MDYgMi4zNTUyMiwtNy41MzI5NiBDMi45MzM1MSwtNy44NDk4NSAzLjU2OTk5LC04LjAwODMgNC4yNjQ2NSwtOC4wMDgzIEM1LjA1MjQxLC04LjAwODMgNS43MTQ4NCwtNy44MDc3OCA2LjI1MTk1LC03LjQwNjc0IEM2Ljc4OTA2LC03LjAwNTcgNy4xNjMyNSwtNi40NDE3MyA3LjM3NDUxLC01LjcxNDg0IEw2LjM0ODYzLC01LjQ3MzE0IEM2LjE2NjAyLC02LjA0NjA2IDUuOTAxMDQsLTYuNDYzMjIgNS41NTM3MSwtNi43MjQ2MSBDNS4yMDYzOCwtNi45ODYgNC43Njk1MywtNy4xMTY3IDQuMjQzMTYsLTcuMTE2NyBDMy42MzgwMiwtNy4xMTY3IDMuMTMyMjQsLTYuOTcxNjggMi43MjU4MywtNi42ODE2NCBDMi4zMTk0MiwtNi4zOTE2IDIuMDMzODUsLTYuMDAyMiAxLjg2OTE0LC01LjUxMzQzIEMxLjcwNDQzLC01LjAyNDY2IDEuNjIyMDcsLTQuNTIwNjcgMS42MjIwNywtNC4wMDE0NiBDMS42MjIwNywtMy4zMzE4NyAxLjcxOTY1LC0yLjc0NzMxIDEuOTE0NzksLTIuMjQ3OCBDMi4xMDk5NCwtMS43NDgyOSAyLjQxMzQxLC0xLjM3NSAyLjgyNTIsLTEuMTI3OTMgQzMuMjM2OTgsLTAuODgwODU5IDMuNjgyNzgsLTAuNzU3MzI0IDQuMTYyNiwtMC43NTczMjQgQzQuNzQ2MjYsLTAuNzU3MzI0IDUuMjQwNCwtMC45MjU2MTggNS42NDUwMiwtMS4yNjIyMSBDNi4wNDk2NCwtMS41OTg4IDYuMzIzNTcsLTIuMDk4MzEgNi40NjY4LC0yLjc2MDc0ICIvPgo8L2c+CjwvZz4KPC9zdmc+Cg=="/>
                <se:Format>image/svg+xml</se:Format>
              </se:ExternalGraphic>
              <!--Well known marker fallback-->
              <se:Mark>
                <se:WellKnownName>square</se:WellKnownName>
                <se:Fill>
                  <se:SvgParameter name="fill">#000000</se:SvgParameter>
                </se:Fill>
                <se:Stroke>
                  <se:SvgParameter name="stroke">#232323</se:SvgParameter>
                  <se:SvgParameter name="stroke-width">0.5</se:SvgParameter>
                </se:Stroke>
              </se:Mark>
              <se:Size>9</se:Size>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
      </se:FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
