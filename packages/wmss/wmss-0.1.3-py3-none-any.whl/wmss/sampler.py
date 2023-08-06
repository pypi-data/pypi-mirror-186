import json
import os
import xml.dom.minidom

import easygui
import owslib.wms
import pyproj
import shapefile

class WMSS():

    _home_directory = None
    
    def __init__(self, name, url=None):

        self._name = name.lower()
        self._url = url

        self._project_directory = None

        self._service = None
        self._xml = None
        self._contents = None

        self._xml_layers_index = None
        self._xml_layers = None

        self._layer = None
        self._layer_name = None
        self._layer_epsg = None
        self._metadata = None

        self._vector = None
        self._vector_format = None
        self._vector_points = None
        self._vector_blocks = None
        self._vector_epsg = None
        
        self._sample_size = None
        self._sample_format = None
        self._block_size = 100

        self._sample_points = None
        self._sample_points_transform = None

        self._build_home_directory()
        self._build_project_directory()
        
        if url is not None:
            pass
            # Check JSON of previous visited URLs, append if necessary

            # Get XML and contents


    def __repr__(self):

        if self._url is None:
            return json.dumps({})

        description = {}

        description['wms'] = {
                'id': self._name,
                'title': self._xml_layers_index['title'],
                'url': self._url
        }
        
        if self._layer is not None:

            description['layer'] = {
                'name': self._layer_name,
                'epsg': self._layer_epsg
            }

        if self._vector is not None:
            
            description['vector'] = {
                'filename': self._vector,
                'format': self._vector_format,
                'epsg': self._vector_epsg,
                'points': self._vector_points,
                'blocks': self._vector_blocks
            }

        if self._vector is not None and self._sample_size is not None:
            description['sample'] = {
                'size': self._sample_size,
                'format': self.formats()[self._sample_format],
                'block': self._block_size
            }

        return json.dumps(description, indent=4)


    def _build_home_directory(self):
        
        home_directory = None

        if os.name == 'nt':
            home_directory = os.path.join(os.getenv('APPDATA'), '.wmss')
        elif os.name == 'posix':
            home_directory = os.path.join(os.getenv('HOME'), '.wmss')

        __class__._home_directory = home_directory

        if not os.path.isdir(home_directory):
            os.mkdir(home_directory)


    def _build_project_directory(self):
        
        project_directory = os.path.join(
            __class__._home_directory,
            self._name
        )

        if not os.path.isdir(project_directory):
            try:
                os.mkdir(project_directory)
            except:
                return

        self._project_directory = project_directory


    def _get_xml_layers_index(self, layer):
        
        xml_layers_index = {
            'title': None,
            'srs': None,
            'extent': None,
            'layers': None
        }

        for child in layer.childNodes:

            if child.__class__.__name__ != 'Element':
                continue

            if child.tagName == 'Title':
                xml_layers_index['title'] = child.firstChild.nodeValue
            elif child.tagName == 'SRS':
                if xml_layers_index['srs'] is None:
                    xml_layers_index['srs'] = []
                
                xml_layers_index['srs'].append(
                    int(child.firstChild.nodeValue.split(':')[-1])
                )
            elif child.tagName == 'BoundingBox':
                
                if not child.hasAttribute('SRS'):
                    continue
                
                if not child.hasAttribute('minx') or not child.hasAttribute('miny') or \
                   not child.hasAttribute('maxx') or not child.hasAttribute('maxy'):
                    continue
                
                bbox_srs = int(child.getAttribute('SRS').split(':')[-1])
                
                bbox_extent = [
                    float(child.getAttribute('minx')),
                    float(child.getAttribute('miny')),
                    float(child.getAttribute('maxx')),
                    float(child.getAttribute('maxy'))
                ]

                if child.hasAttribute('resx') and child.hasAttribute('resy'):

                    bbox_cell = [
                        float(child.getAttribute('resx')),
                        abs(float(child.getAttribute('resy')))
                    ]
                else:
                    bbox_cell = None

                if xml_layers_index['extent'] is None:
                    xml_layers_index['extent'] = {}
                    
                xml_layers_index['extent'][bbox_srs] = {
                    'bbox': bbox_extent,
                    'cell': bbox_cell
                }

            elif child.tagName == 'Layer':
                for grand_child in child.childNodes:
                    if grand_child.__class__.__name__ != 'Element':
                        continue
                    if grand_child.tagName == 'Name':
                        if xml_layers_index['layers'] is None:
                            xml_layers_index['layers'] = []
                        xml_layers_index['layers'].append(grand_child.firstChild.nodeValue)
                        
        self._xml_layers_index = xml_layers_index


    def _get_xml_layer(self, layer):
        
        xml_layer_attributes = {'srs': None, 'extent': None}
        
        for child in layer.childNodes:

            if child.__class__.__name__ != 'Element':
                continue

            if child.tagName == 'Name':
                xml_layer_name = child.firstChild.nodeValue
            elif child.tagName == 'SRS':
                if xml_layer_attributes['srs'] is None:
                    xml_layer_attributes['srs'] = []
                xml_layer_attributes['srs'].append(
                    int(child.firstChild.nodeValue.split(':')[-1])
                )
            elif child.tagName == 'BoundingBox':
                
                if not child.hasAttribute('SRS'):
                    continue
                
                if not child.hasAttribute('minx') or not child.hasAttribute('miny') or \
                   not child.hasAttribute('maxx') or not child.hasAttribute('maxy'):
                    continue
                
                bbox_srs = int(child.getAttribute('SRS').split(':')[-1])
                
                bbox_extent = [
                    float(child.getAttribute('minx')),
                    float(child.getAttribute('miny')),
                    float(child.getAttribute('maxx')),
                    float(child.getAttribute('maxy'))
                ]

                if child.hasAttribute('resx') and child.hasAttribute('resy'):

                    bbox_cell = [
                        float(child.getAttribute('resx')),
                        abs(float(child.getAttribute('resy')))
                    ]
                else:
                    bbox_cell = None

                if xml_layer_attributes['extent'] is None:
                    xml_layer_attributes['extent'] = {}
                    
                xml_layer_attributes['extent'][bbox_srs] = {
                    'bbox': bbox_extent,
                    'cell': bbox_cell
                }

        if self._xml_layers is None:
            self._xml_layers = {}
            
        self._xml_layers[xml_layer_name] = xml_layer_attributes


    def _get_xml_layers(self):
        
        wms_xml_dom = xml.dom.minidom.parseString(
            self._xml #.replace('\n', '').replace('\t', '')
        )


        for layer in wms_xml_dom.getElementsByTagName('Layer'):
            
            if layer.hasAttribute('queryable'):
                self._get_xml_layer(layer)
            else:
                self._get_xml_layers_index(layer)



    def _xml_contents(self):

        self._xml = self._service.getServiceXML().decode('utf-8') ########## ??
        self._contents = self._service.contents


    def _shapefile_to_epsg(self):

        try:
            prj_filename = self._vector.replace('.shp', '.prj')

            with open(prj_filename, 'rt') as prj_file:
                wkt = prj_file.read()
        except:
            return
        
        try:
            shapefile_crs = pyproj.CRS.from_wkt(wkt)
        except:
            return
        
        self._vector_epsg = shapefile_crs.to_epsg()


    def _get_shapefile_points(self):

        try:
            shapefile_reader = shapefile.Reader(self._vector)
        except:
            return

        sample_points = {}

        for count, shape in enumerate(shapefile_reader.shapes()):

            x, y = shape.points[0]

            if self._sample_points_transform is not None:
                x, y = self._sample_points_transform.transform(x, y)

            if self._sample_points is None:
                self._sample_points = {}

            self._sample_points[count] = [x, y]


    def _get_geojson_points(self):
        pass

    
    def _get_points(self):

        if self._layer_epsg != self._vector_epsg:
            try:
                vector_crs = pyproj.CRS.from_epsg(self._vector_epsg)
                layer_crs = pyproj.CRS.from_epsg(self._layer_epsg)

                self._sample_points_transform = pyproj.Transformer.from_crs(
                    vector_crs, layer_crs, always_xy=True
                )
            except:
                # TODO: Warning
                return

        if self._vector_format == 'Shapefile':
            self._get_shapefile_points()
        elif self._vector_format == 'GeoJSON':
            self._get_geojson_points()
        else:
            return


    def _get_image_extensions(self):

        """Returns image file and world file extensions given the output format"""

        extensions = {
            'image/jpeg': ['.jpg', '.jgw'],
            'image/jpegxr': ['.jpg', '.jgw'],
            'image/jpgpng': ['.jpg', '.jgw'],
            'image/png8': ['.png', '.pgw'],
            'image/png': ['.png', '.pgw'],
            'image/tiff': ['tif', 'tfw'],
            'image/webp': ['.webp', '.webpw']
        }

        try:
            image_extensions = extensions[self.formats()[self._sample_format]]
        except:
            image_extensions = None

        return image_extensions

        
    def _get_samples(self, index_range, block_id, geojson=False):
        
        """Extracts WMS samples from one or more blocks"""
        
        try:
            image_extension, world_extension = self._get_image_extensions()
        except:
            return

        layer = self.layers(True)[self._layer_name]['extent'][self._layer_epsg]

        x_min, y_min, x_max, y_max = layer['bbox']
        x_cell_size, y_cell_size = layer['cell']

        sample_y_size, sample_x_size = self._sample_size
        
        for sample in range(*index_range):

            try:
                x_center, y_center = self._sample_points[sample]
            except:
                continue
            
            filename = os.path.join(
                self._project_directory, f'sample_{sample:05d}_{block_id:04d}'
            )

            image_filename = filename + image_extension
            world_filename = filename + world_extension
            
            # TODO: check [x_Center, y_center] is within bbox
            
            delta_x = x_center - x_min
            delta_y = y_center - y_min

            x_center_cell = int(divmod(delta_x, x_cell_size)[0]) # column
            y_center_cell = int(divmod(delta_y, y_cell_size)[0]) # row

            x_min_cell = x_min + (x_center_cell * x_cell_size)
            y_min_cell = y_min + (y_center_cell * y_cell_size)

            x_min_sample = x_min_cell - (sample_x_size / 2) * x_cell_size
            y_min_sample = y_min_cell - (sample_y_size / 2) * y_cell_size

            x_max_sample = x_min_sample + sample_x_size * x_cell_size
            y_max_sample = y_min_sample + sample_y_size * y_cell_size

            sample_image = self._service.getmap(
                layers=[self._layer_name],
                srs=f'EPSG:{self._layer_epsg}',
                bbox=(x_min_sample, y_min_sample, x_max_sample, y_max_sample),
                size=(sample_x_size, sample_y_size),
                format=self.formats()[self._sample_format]
            )

            with open(image_filename, 'wb') as sample_file:
                sample_file.write(sample_image.read())
                #sample_file.close()

            with open(world_filename, 'wt') as world_file:
                world_file.write(f'{layer["cell"][0]}\n')
                world_file.write(f'0.0\n')
                world_file.write(f'0.0\n')
                world_file.write(f'-{layer["cell"][1]}\n')
                world_file.write(f'{x_min_sample + 0.5 * layer["cell"][0]}\n')
                world_file.write(f'{y_max_sample - 0.5 * layer["cell"][1]}\n')         


            if geojson:
                
                geojson_filename = filename + '.geojson'

                sample_box = [
                    [x_min_sample, y_min_sample],
                    [x_max_sample, y_min_sample],
                    [x_max_sample, y_max_sample],
                    [x_min_sample, y_max_sample],
                    [x_min_sample, y_min_sample]
                ]

                feature = {
                    'type': 'Feature',
                    'geometry': {
                        'type': 'Polygon',
                        'coordinates': [sample_box]
                    },
                    'properties': {
                        'id': f'sample_{sample:05d}_{block_id:04d}'
                    }
                }

                with open(geojson_filename, 'wt') as geojson_file:
                    geojson_file.write(
                        json.dumps(feature, indent=4)
                    )
            
##            break
        

    def _read_project_index(self):
        
        index_filename = os.path.join(self._project_directory, 'index.json')

        try:
            with open(index_filename, 'rt') as index_file:
                json_index = json.loads(index_file.read())
        except:
            json_index = {}

        return json_index


    def _update_project_index(self, contents):

        index_filename = os.path.join(self._project_directory, 'index.json')

        with open(index_filename, 'wt') as index_file:
            index_file.write(json.dumps(contents, indent=4))

    
    def set_url(self, url):

        self._url = url

        try:
            self._service = owslib.wms.WebMapService(url)
        except:
            # TODO: Warning to users
            print('Warning: WMS not found')
            self._url = None
            self._service = None
            return

        try:
            self._xml_contents()
        except:
            # TODO: Warning to users
            print('Warning: XML contents not available')
            self._url = None
            self._service = None
            self._metadata = None
            self._xml = None
            return

        try:
            self._get_xml_layers()
        except:
            # TODO: Warning to users
            print('Warning: XML layer details not found')
            self._url = None
            self._service = None
            self._metadata = None
            self._xml = None
            self._xml_layers = None
            return


    def set_layer(self, layer_name):

        if self._url is None:
            return
        
        try:
            self._layer = self.layers().index(layer_name)
            self._layer_name = layer_name
        except:
            # TODO: Show warning
            print(f'Warning: Layer named {layer_name} not found.')
            return

        try:
            layer_default_epsg = list(
                    self._xml_layers[layer_name]['extent'].keys()
            )[0]
            
            self._layer_epsg = layer_default_epsg
        except:
            pass

        if self._layer_epsg is not None:
            return

        try:
            layer_default_epsg = list(
                self._xml_layers_index['extent'].keys()
            )[0]

            self._layer_epsg = layer_default_epsg
        except:
            print('Warning: SRS info not found. Set SRS manually using method set_epsg()')


    def set_format(self, format_name):

        if self._url is None:
            return

        if 'image/' not in format_name:
            format_name = f'image/{format_name}'
            
        try:
            self._sample_format = self.formats().index(format_name.lower())
        except:
            # TODO: Show warning
            pass

    def set_epsg(self, epsg):

        if self._layer is None:
            return

        try:
            user_epsg = pyproj.CRS.from_epsg(epsg)
        except:
            # TODO: Warning: wrong EPSG code
            return

        self._layer_epsg = epsg

        pass


    def set_shapefile(self, shapefilename=None):
        
        if self._url is None:
            return

        if shapefilename is None:
            shapefilename = easygui.fileopenbox(
                default='*.shp', filetypes=['*.shp']
            )

        if shapefilename is None:
            return

        try:
            shapefile_reader = shapefile.Reader(shapefilename)
            
            if shapefile_reader.shapes()[0].shapeType != 1:
                return

            self._vector_points = len(shapefile_reader.shapes())
            self._vector_blocks = int(self._vector_points / self._block_size) + 1

        except:
            return

        self._vector = shapefilename
        self._vector_format = 'Shapefile'

        self._shapefile_to_epsg()


    def set_vector_epsg(self, epsg):

        try:
            vector_crs = pyproj.CRS.from_epsg(epsg)
        except:
            return

        self._vector_epsg = vector_crs

    
    def set_geojson(self, geojson=None):

        # TODO: everything

        self._vector_epsg = 4326
        
        return

    
    def set_sample_size(self, rows, columns=None):
        
        try:
            number_of_rows = int(rows)

            if columns is None:
                number_of_columns = number_of_rows
            else:
                number_of_columns = int(columns)
                
        except:
            return

        self._sample_size = [number_of_rows, number_of_columns]


    def set_block_size(self, block_size):

        if not isinstance(block_size, int):
            return

        self._block_size = block_size

        if self._vector is not None:
            self._vector_blocks = int(self._vector_points / self._block_size) + 1

        self._update_project_json({})

        
    def layers(self, verbose=False):

        if self._url is None:
            return

        list_of_layers = []

        if verbose is False:
            list_of_layers = self._xml_layers_index['layers']
        elif verbose is True:
            list_of_layers = self._xml_layers
        
        return list_of_layers 


    def index(self):
        pass

    
    def formats(self):

        if self._service is None:
            return

        if 'GetMap' not in self.operations():
            return

        return self._service.getOperationByName('GetMap').formatOptions


    def operations(self):

        if self._service is None:
            return

        operations = []

        for operation in self._service.operations:
            operations.append(operation.name)

        return operations


    def describe(self):
        
        if self._vector is None:
            return

        return {
            'points': self._vector_points,
            'blocks': self._vector_blocks,
            'format': self.formats()[self._sample_format]
        }


    def sampling(self, block=None, geojson=False):

        if self._service is None:
            return

        if self._url is None or self._layer is None or self._vector is None:
            return
        
        if 'GetMap' not in self.operations():
            # TODO: Warning message here !
            return

        if self._sample_format is None:
            return

        if block is None:
            blocks = range(self._vector_blocks)
        elif isinstance(block, list):
            blocks = [item - 1 for item in block]
        elif isinstance(block, int):
            blocks = [block - 1]
        else:
            return

        project_index = self._read_project_index()

        self._get_points()

        number_of_blocks = len(blocks)
        
        for count, block_id in enumerate(blocks):

            if block_id >= self._vector_blocks:
                continue

            print(f'Processing block {count + 1:04d}/{number_of_blocks:04d} [{block_id + 1}]\t\t', end='') #, block_start, block_end)

            block_start = block_id * self._block_size
            block_end = (block_id + 1) * self._block_size

            self._get_samples([block_start, block_end], block_id + 1, geojson)

            project_index[f'{block_id}'] = 'OK'

            print('[OK]')


        print(f'\n\nSamples stored in {self._project_directory}\n')

        self._update_project_index(project_index)
    
