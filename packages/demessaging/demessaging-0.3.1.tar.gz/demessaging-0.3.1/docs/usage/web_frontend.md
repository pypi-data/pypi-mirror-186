# Connecting backend modules and web frontend components
One common aspect of data analytics is of course data visualization. DASF supports this by providing a variety of web frontend visualization components. Since we initially developed DASF in a geo-scientific context we start with some examples visualizing spatio-temporal data.

```{admonition} Flood Event Explorer
:class: note

For a general impression of what is possible with DASF you can checkout the Digital Earth Flood Event Explorer. It was developed with DASF. In case you don't want to dive too deep into the individual workflows of the Flood Event Explorer, you might watch some videos showing the usage of the tool and providing some overview of what kind of visualizations are supported. The videos are linked in the applications landing page linked below or via the projects [youtube channel](https://www.youtube.com/channel/UCGajghuiOBoafRg4K5Xkk-Q).

- Homepage: [https://digitalearth-hgf.de/results/workflows/flood-event-explorer/](https://digitalearth-hgf.de/results/workflows/flood-event-explorer/)
- Source Code Repository: [https://git.geomar.de/digital-earth/flood-event-explorer](https://git.geomar.de/digital-earth/flood-event-explorer)
- Deployed Application: [http://rz-vm154.gfz-potsdam.de:8080/de-flood-event-explorer/](http://rz-vm154.gfz-potsdam.de:8080/de-flood-event-explorer/)

Citation Reference:  
Eggert, Daniel; Rabe, Daniela; Dransch, Doris; Lüdtke, Stefan; Nam, Christine; Nixdorf, Erik; Wichert, Viktoria; Abraham, Nicola; Schröter, Kai; Merz, Bruno (2022): The Digital Earth Flood Event Explorer: A showcase for data analysis and exploration with scientific workflows. GFZ Data Services. [https://doi.org/10.5880/GFZ.1.4.2022.001](https://doi.org/10.5880/GFZ.1.4.2022.001)
```

## The DASF map component: Demap
The geo-visualization backbone of DASF is a web map component called `Demap` which is part of the `dasf-web` library. The `De` part originates from the Digital Earth project through which the development was funded. It is a Vue component and based on the popular Openlayers ([https://openlayers.org/](https://openlayers.org/)) library. In order to use the components provided by `dasf-web` you have to include it in your vue-based web application (also see: {ref}`websetup`).

As any other custom Vue component import the `Demap` and add it to the html template of your own page/component. The map component supports the following customization properties and events:

### Props

| Name | Type | Default | Description |
| ---- | ---- | ------- | ----------- |
| zoom | number | 9 | Initial zoom level of the map |
| projection | string | 'EPSG:3857' | EPSG-Code of the projection used by the map
| center | [number, number] | [13.740107, 51.055168] | Coordinates to center the map in geographical coordinates (EPSG: 4326)
| legend-collapsed | boolean | false | If set, the legend will be initially collapsed |
| no-legend | boolean | false | If set, the map component will disable it's integrated legend / layerswitcher component |
| force-actions-append | boolean | false | If set, custom layer actions registered via `window['default_raster_layer_actions']` are added to new layers, even if the internal legend is deactivated |
| map-view | ol.View | null | External `view` instance, can be used to create linked views (e.g. Pan&Zoom) between multiple `Demap` instances.
| show-osm | boolean | false | If set, adds the default OpenStreetMap tile layer as a basemap
| enable-rotation | boolean | false | If set, enables the map rotation feature (mobile: [pinch](https://openlayers.org/en/latest/apidoc/module-ol_interaction_PinchRotate-PinchRotate.html); desktop: [alt+shift+drag](https://openlayers.org/en/latest/apidoc/module-ol_interaction_DragRotate-DragRotate.html))
| disable-auto-zoom-to-layer | boolean | false | If set, the map does not automatically pans and zooms to newly added layers
| start-layers | ol.Layer[] \| Promise<ol.Layer[]> | null | An array of layers (or a Promise resolving to an array of layers) that will be added to the map right from the start (or as soon as the Promise resolves).

### Events

| Name | Description |
| ---- | ----------- |
| item-selected | called with an array of ol.Feature that have been selected in the map |
| load-custom-file | called with a File that was drag'n'drop onto the map, but no internal file handler was found supporting the files format. (integrated file handlers: .geojson are .nc) also see: add-layer component |
| set-roi | called with a ol.Geometry that the user has selected as a region of interest through the roi layer action. |
| unset-roi | called when the user unselects the previously selected roi geometry. |
| layer-added | called with a ol.Layer instance that was just added to the map component via the `addLayer` function. |

### Api

In case you created an object reference (e.g. via the @Ref annotation) for the `Demap` component you can utilize the following api to interact with it.

| Name | Description |
| ---- | ----------- |
| getLayers | Returns an array of all layers registered with the map |
| updateSelectInteraction | Accepting an optional ol.StyleLike style and an optional FilterFunction used for the build-in feature selection interaction. Also refer to [OL Select API](https://openlayers.org/en/v6.4.3/apidoc/module-ol_interaction_Select-Select.html) |
| updateSelectedFeature | Accepting an instance of ol.Feature and selecting it, if the internal selection interaction is enabled, e.g. via 'updateSelectInteraction' |
| updateSelectedFeatures | Accepting an array of ol.Feature and selecting them, if the internal selection interaction is enabled, e.g. via 'updateSelectInteraction' |
| addBaseLayer | Accepting an instance of ol.TileLayer to be added as an additional base layer |
| startEditLayer | Accepting an instance of ol.Layer and initializing the build-in editing feature in case the provided layer has a ol.VectorSource. This is mainly used by the edit layer LayerAction. |
| stopEditLayer | Finishes the build-in editing feature. This is mainly used by the edit layer LayerAction. |
| createVectorLayer | Returns a new instance of an ol.VectorLayer, accepting a title string, an optional ol.VectorSource an optional array of DemapLayerActions |
| Demap.isVectorLayer | Returns `true` if the given layer is an instance of ol.VectorLayer |
| addLayer | Accepting an instance of ol.Layer and adding it to the map, adding new layers to the map through this method also creates color scales for all numeric properties of the underlying data |
| panAndZoomToExtent | Accepting an instance of ol.Layer or ol.Extent and pans and zooms the map so the entire (layers) extent is visible. |
| getMap | Returns the internally used ol.Map instance |
| getThematicLayerGroup | Returns the ol.LayerGroup containing all added non-base layers |
| dispose | Disposes the ol.Map context by setting its target element to `null` |

### Common spatio-temporal datastructure
Now the initial goal was to connect data produced/provided by backend modules with a web visualization component, e.g. `Demap`.
For this to work we need a common datastructure for the data. In case of spatio-temporal data we rely on the NETCDF format. In the scope of a python backend module the popular xarray library can be used to load, create or manipulate the data. Finally we send it to the front-end application for visualization. In order to interpret the netcdf data the `dasf-web` library provides a `NetcdfRasterSource` class, which can be wrapped into a `TemporalImageLayer` and directly added to the map component.

```{admonition} Network Common Data Format (NetCDF)
:class: note

The NetCDF is a pretty generic format, so its practically impossible to interpret all possible data arrangements. Therefore we need to enforce certain conventions. For this we assume the NetCDF data to follow the commonly used [CF conventions](https://cfconventions.org/).

Especially important is the global `crs` attribute, defining the coordinate reference system for the spatial data. It has to be a string containing the EPSG code of the CRS, e.g. `'EPSG:4326'`.
```

(demap)=
### Demap example
The following example creates a web front-end utilizing the `Demap` component.

```{code-block} vue
---
lineno-start: 1
emphasize-lines: 7-13, 28-29
caption: Vue page showing a map via the Demap component
---
<template>
  <v-container
    style="margin-bottom: 35px; padding-top: 100px; padding-bottom: 20px"
  >
    <v-card :loading="dataPending">
      <v-card-title>Spatio-Temporal Data Example</v-card-title>
      <demap
        ref="demap"
        show-osm
        legend-collapsed
        :center="[13.064923, 52.379539]"
        :zoom="16"
        style="height: 50vh; min-height: 300px;"/>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue, Ref } from 'vue-property-decorator'
import Demap from 'dasf-web/lib/map/Demap.vue'
import SpatioTemporalClient from '~/lib/SpatioTemporalClient'
import TemporalImageLayer from 'dasf-web/lib/map/model/TemporalImageLayer'

@Component({
  components: { Demap }
})
export default class SpatioTemporal extends Vue {
  @Ref('demap')
  private demap!: Demap

  private dataPending = true

  protected created (): void {
    const backend: SpatioTemporalClient = new SpatioTemporalClient()
 
    backend.getData().then((dataLayer: TemporalImageLayer) => {
      this.demap.addLayer(dataLayer)
      this.dataPending = false
    }).catch((reason) => {
      console.warn(reason)
    }
    )
  }
}
</script>
```

Note that we create an object reference to the map via the `@Ref` annotation in line 28. We will use this reference later to programatically interact with the map. Event without the backend part (lines 34-43) the map component is fully functional. Since the `show-osm` property is set the map shows an OpenStreetMap base layer. User can add new layers either via drag'n'drop or via the built-in legend menu. 

### Backend providing spatio-temporal data
Now that we created the front-end part, let's create a backend module providing the data that the front-end will visualize later on. We keep it simple and expose a `get_data()` function returning a `xarray.Dataset` that we load from a local netcdf file. In general the data could also be a result of some algorithm or loaded from an URL, depending on you use case.

```{code-block} python
---
lineno-start: 1
emphasize-lines: 2
caption: spatio-temporal Dataset exposed via get_data function
---
from demessaging import main
from demessaging.types.xarray import Dataset
import xarray as xr

__all__ = ["get_data"]


def get_data() -> Dataset:
    ds = xr.load_dataset('sample_data.nc')
    return ds


if __name__ == "__main__":
    main(
        messaging_config=dict(topic="spatio-temporal")
    )
```

Note that the function returns `demessaging.types.xarray.Dataset` instead of `xarray.Dataset`. The former one extends the latter with additional methods needed for pydantic and also defines how the object is serialized. In case you would like to define your own data type extension, you might use this one as a template.

For most websocket based message brokers there is a maximum message size of 1MB configured. So, depending on the size of your data, we might exceed this size. DASF automatically fragments messages that are too big. In case you want to avoid fragmented messages you need to increase message brokers message size as well as DASF payload size.

```{admonition} WebSocket Message Size
:class: warning

WebSocket connections define a maximum message size (usually: 1MB). DASF will fragment all messages exceeding a given threshold called `max_payload_size`. The current default is 500kb. 
In order to work, the `max_payload_size` must be smaller than the maximum message size of the used message broker. 
e.g. Apache Pulsars message size can be configured in the `standalone.conf` via the `webSocketMaxTextFrameSize` parameter. 
The `max_payload_size` for a backend module can be configured in the config passed to the `main()` function (see: {func}`demessaging.config.WebsocketURLConfig`).
```

### The spatio-temporal client stub
In order connect the backend and the `Demap` visualization, we are going to the need the typescript client stub for the backend module. This looks almost identical as our hello world client stub (see {ref}`clientstub`), except that we don't return the payload string, but convert it to a `TemporalImageLayer` based on a `NetcdfRasterSource`.

```{code-block} typescript
---
lineno-start: 1
emphasize-lines: 29-37
caption: Typescript client stub for the spatio-temporal backend module.
---
import PulsarConnection from 'dasf-web/lib/messaging/PulsarConnection'
import { PulsarModuleResponse, PulsarModuleRequest, PulsarModuleRequestReceipt } from 'dasf-web/lib/messaging//PulsarMessages'
import { DefaultPulsarUrlBuilder } from 'dasf-web/lib/messaging//PulsarUrlBuilder'
import TemporalImageLayer from 'dasf-web/lib/map/model/TemporalImageLayer'
import NetcdfRasterSource from 'dasf-web/lib/map/model/NetcdfRasterSource'
import b64a from 'base64-arraybuffer'

export default class SpatioTemporalClient {
  private pulsarConnection: PulsarConnection

  public constructor () {
    this.pulsarConnection = new PulsarConnection(new DefaultPulsarUrlBuilder('localhost', '8080', 'default', 'spatio-temporal'))
  }

  private createGetDataRequest (): PulsarModuleRequest {
    const request = PulsarModuleRequest.createRequestMessage()
    request.payload = btoa(JSON.stringify({ func_name: 'get_data' }))

    return request
  }

  public getData (): Promise<TemporalImageLayer> {
    return new Promise((resolve: (value: TemporalImageLayer) => void, reject: (reason: string) => void) => {
      this.pulsarConnection.sendRequest(this.createGetDataRequest(),
        (response: PulsarModuleResponse) => {
          if (response.properties.status === 'success') {
            // parse the payload
            const netcdfB64 = JSON.parse(atob(response.payload))
            // convert the b64 into an arraybuffer and parse the buffer into an ol.Source object
            NetcdfRasterSource.create({
              data: b64a.decode(netcdfB64)
            }).then((src: NetcdfRasterSource) => {
              // wrap ntcdf source into a layer
              const imageLayer = new TemporalImageLayer({
                title: 'spatio-temporal data',
                source: src
              })

              resolve(imageLayer)
            })
          } else {
            reject(atob(response.payload))
          }
        },
        null,
        (receipt: PulsarModuleRequestReceipt) => {
          reject(receipt.errorMsg)
        })
    })
  }
}

``` 

Finally we can add the `TemporalImageLayer` returned by the client stub to our `Demap` via the `addLayer` method (line 37 of {ref}`demap`).
The resulting visualization will look like the following:

![Spatio-Temporal Example](/_static/spatio_temporal.png)

While you can explore the spatial dimension with the maps pan&zoom functionality, the selection of the rendered data variable and the used color scale are possible through the legend component. In order to browse through the temporal dimension, the legend component provides an intuitive time-slider.
