from pydantic import BaseModel, root_validator
from typing import List, Dict, Optional, Union
from pathlib import Path
import pandas as pd
import numpy as np
import tempfile
from enum import Enum
import zlib
from pdf2image import convert_from_path
from PIL import ImageDraw, ImageFont
import matplotlib.pyplot as plt
import copy
import msgpack
import uuid as uuid_lib
from functools import partial


PDF_SCALE = 1.5
DPI = 72


class EntityTypeMapping(BaseModel):
    id: int
    db_id: Optional[int] = None
    name: str
        
    @root_validator(pre=False)
    def set_db_id(cls, values):
        if 'db_id' not in values or not values['db_id']:
            values['db_id'] = values['id']
        return values


        
class GroupTypeMapping(BaseModel):
    id: int
    name: str
    

class Coordinates(BaseModel):
    x: float
    y: float
    
    def to_list(self):
        return self.y, self.x
        

class BoundingBox(BaseModel):
    top_left: Coordinates
    bottom_right: Coordinates
    
    def to_list(self, coordinates_scale=1, order='ltbr'):
        output = []
        for location in order:
            if location == 'l':
                output.append(self.top_left.x / coordinates_scale)
            if location == 't':
                output.append(self.top_left.y / coordinates_scale)
            if location == 'b':
                output.append(self.bottom_right.y / coordinates_scale)
            if location == 'r':
                output.append(self.bottom_right.x / coordinates_scale)
        return output

    def get_horizontal_center(self):
        return self.top_left.x + self.get_width() / 2

    def get_vertical_center(self):
        return self.top_left.y + self.get_height() / 2

    def get_center(self):
        return Coordinates(x=self.get_horizontal_center(), y=self.get_vertical_center())

    def get_width(self):
        return self.bottom_right.x - self.top_left.x

    def get_height(self):
        return self.bottom_right.y - self.top_left.y
    
    
class TextLayerSource(Enum):
    PDF_TEXT_LAYER = 'PDF_TEXT_LAYER'
    OCR_OUTPUT = 'OCR_OUTPUT'
    
    @staticmethod
    def parse(input_string):
        if input_string in ['TEXT_LAYER', 'PDF_TEXT_LAYER']:
            return TextLayerSource.PDF_TEXT_LAYER
        if input_string in ['OCR', 'OCR_OUTPUT']:
            return TextLayerSource.OCR_OUTPUT
        raise ValueError(f'input "{input_string}" could not be converted to a TextLayerSource')
    

class TokenInformation(BaseModel):
    text: str
    token_id: int
    bounding_box: BoundingBox
    

class TextLayer(BaseModel):
    page_nr: int
    text_layer_source: TextLayerSource
    scaling_factor: float
    page_width: float
    page_height: float
    max_dimension: Optional[float]
    tokens_information: List[TokenInformation]

    @root_validator(pre=False)
    def _set_max_dimension(cls, values):
        values['max_dimension'] = max(values['page_width'], values['page_height'])
        return values

    def _normalize_token_information(self, token_information, max_dimension):
        token_information.bounding_box.top_left.x = token_information.bounding_box.top_left.x / max_dimension
        token_information.bounding_box.top_left.y = token_information.bounding_box.top_left.y / max_dimension
        token_information.bounding_box.bottom_right.x = token_information.bounding_box.bottom_right.x / max_dimension
        token_information.bounding_box.bottom_right.y = token_information.bounding_box.bottom_right.y / max_dimension

    def normalize_coordinates(self, max_dimension=0):
        if not max_dimension:
            max_dimension = self.max_dimension
        for token_information in self.tokens_information:
            self._normalize_token_information(token_information, max_dimension)
        self.page_width = self.page_width / max_dimension
        self.page_height = self.page_height / max_dimension

    def sort_tokens_information(self):
        self.tokens_information.sort(key=lambda token_information: token_information.token_id)


class EntityAnnotation(BaseModel):
    page_nr: int
    token_id: int
    entity_type: Optional[int] = 0
    group_type: Optional[int] = None
    group_instance_index: Optional[int] = None
    bounding_box: BoundingBox 

    def normalize_coordinates(self, max_dimension):
        self.bounding_box.top_left.x = self.bounding_box.top_left.x / max_dimension
        self.bounding_box.top_left.y = self.bounding_box.top_left.y / max_dimension
        self.bounding_box.bottom_right.x = self.bounding_box.bottom_right.x / max_dimension
        self.bounding_box.bottom_right.y = self.bounding_box.bottom_right.y / max_dimension


class EncodedPDF(BaseModel):
    filename: str
    compressed_data: bytes


class KDDBuilder(BaseModel):
    kdd_parts: Dict = {}
    
    def build_kdd(self):
        return KDD(**self.kdd_parts)


class KDD(BaseModel): # Klassif.ai Data Document
    version: str = '1.1'
    uuid: uuid_lib.UUID = uuid_lib.uuid4()
    project_id: str
    creation_timestamp: int
    details: Dict = {}
    entity_type_mappings: List[EntityTypeMapping] = [EntityTypeMapping(id=0, name='NO_ENTITY')]
    entity_annotations: Optional[List[EntityAnnotation]] = []
    text_layers: List[TextLayer]
    encoded_pdf: EncodedPDF = EncodedPDF(filename='', compressed_data=b'')

    @staticmethod
    def _serialize_kdd(obj):
        if isinstance(obj, KDD):
            return {
                '__object_type__': 'KDD',
                'version': obj.version,
                'project_id': obj.project_id,
                'creation_timestamp': obj.creation_timestamp,
                'details': obj.details,
                'entity_type_mappings': obj.entity_type_mappings,
                'entity_annotations': obj.entity_annotations,
                'text_layers': obj.text_layers,
                'encoded_pdf': obj.encoded_pdf
            }
        if isinstance(obj, EntityTypeMapping):
            return {
                '__object_type__': 'EntityTypeMapping',
                'id': obj.id,
                'db_id': obj.db_id,
                'name': obj.name
            }
        if isinstance(obj, EntityAnnotation):
            return {
                '__object_type__': 'EntityAnnotation',
                'page_nr': obj.page_nr,
                'token_id': obj.token_id,
                'entity_type': obj.entity_type,
                'group_type': obj.group_type,
                'group_instance_index': obj.group_instance_index,
                'bounding_box': obj.bounding_box
            }
        if isinstance(obj, TextLayer):
            return {
                '__object_type__': 'TextLayer',
                'page_nr': obj.page_nr,
                'text_layer_source': obj.text_layer_source,
                'scaling_factor': obj.scaling_factor,
                'page_width': obj.page_width,
                'page_height': obj.page_height,
                'tokens_information': obj.tokens_information
            }
        if isinstance(obj, EncodedPDF):
            return {
                '__object_type__': 'EncodedPDF',
                'filename': obj.filename,
                'compressed_data': obj.compressed_data
            }
        if isinstance(obj, Coordinates):
            return {
                '__object_type__': 'Coordinates', 
                'x': obj.x,
                'y': obj.y
            }
        if isinstance(obj, BoundingBox):
            return {
                '__object_type__': 'BoundingBox', 
                'top_left': obj.top_left,
                'bottom_right': obj.bottom_right
            }
        if isinstance(obj, TextLayerSource):
            return {
                '__object_type__': 'TextLayerSource', 
                'text_layer_source': obj.name
            }
        if isinstance(obj, TokenInformation):
            return {
                '__object_type__': 'TokenInformation',
                'text': obj.text,
                'token_id': obj.token_id,
                'bounding_box': obj.bounding_box
            }

    @staticmethod
    def _deserialize_kdd(obj, uuid=None):
        if '__object_type__' not in obj:
            return obj
        if obj['__object_type__'] == 'KDD':
            if uuid is None:
                uuid = obj['encoded_pdf'].filename.split('.')[0]
            return KDD(version=obj['version'], 
                       uuid=uuid,
                       project_id=obj['project_id'], 
                       creation_timestamp=obj['creation_timestamp'], 
                       details=obj['details'],
                       entity_type_mappings=obj['entity_type_mappings'], 
                       entity_annotations=obj['entity_annotations'], 
                       text_layers=obj['text_layers'], 
                       encoded_pdf=obj['encoded_pdf'])
        if obj['__object_type__'] == 'EntityTypeMapping':
            return EntityTypeMapping(id=obj['id'],
                                     db_id=obj['db_id'],
                                     name=obj['name'])
        if obj['__object_type__'] == 'EntityAnnotation':
            return EntityAnnotation(page_nr=obj['page_nr'], 
                                    token_id=obj['token_id'], 
                                    entity_type=obj['entity_type'],
                                    group_type=obj['group_type'],
                                    group_instance_index=obj['group_instance_index'],
                                    bounding_box=obj['bounding_box'])
        if obj['__object_type__'] == 'TextLayer':
            return TextLayer(page_nr=obj['page_nr'], 
                             text_layer_source=obj['text_layer_source'], 
                             scaling_factor=obj['scaling_factor'], 
                             page_width=obj['page_width'], 
                             page_height=obj['page_height'], 
                             tokens_information=obj['tokens_information'])
        if obj['__object_type__'] == 'EncodedPDF':
            return EncodedPDF(filename=obj['filename'], 
                              compressed_data=obj['compressed_data'])
        if obj['__object_type__'] == 'Coordinates':
            return Coordinates(x=obj['x'], 
                               y=obj['y'])
        if obj['__object_type__'] == 'BoundingBox':
            return BoundingBox(top_left=obj['top_left'], 
                               bottom_right=obj['bottom_right'])
        if obj['__object_type__'] == 'TextLayerSource':
            return TextLayerSource.parse(obj['text_layer_source'])
        if obj['__object_type__'] == 'TokenInformation':
            return TokenInformation(text=obj['text'], 
                                    token_id=obj['token_id'], 
                                    bounding_box=obj['bounding_box'])

    @staticmethod
    def from_file(path, load_encoded_pdf=False):
        if not isinstance(path, Path):
            path = Path(path)
        if not path.is_file():
            raise ValueError('file does not exist at path')
        if not path.suffix == '.kdd':
            raise ValueError('not a .kdd path')
        try:
            uuid = uuid_lib.UUID(path.stem)
        except ValueError as e:
            raise ValueError('filename project incorrect uuid')
        with path.open('rb') as file:
            if load_encoded_pdf:
                return msgpack.load(file, object_hook=KDD._deserialize_kdd)
            unpacker = msgpack.Unpacker(file, object_hook=KDD._deserialize_kdd)
            kdd_segments_amount = unpacker.read_map_header()
            kdd_builder = KDDBuilder()
            kdd_builder.kdd_parts['uuid'] = uuid
            for i in range(kdd_segments_amount):
                object_key = unpacker.unpack()
                if not load_encoded_pdf and object_key == 'encoded_pdf':
                    continue
                object_data = unpacker.unpack()
                kdd_builder.kdd_parts[object_key] = object_data
            return kdd_builder.build_kdd()

    def to_file(self, output_dir_path, overwrite=False):
        if not isinstance(output_dir_path, Path):
            output_dir_path = Path(output_dir_path)
        output_path = output_dir_path / f'{self.uuid}.kdd'
        if output_path.is_file():
            print(f'file {output_path.name} already exists on path', end=', ')
            if not overwrite:
                print('ignoring...')
                return
            print('overwriting...')
        if not output_dir_path.joinpath('_meta_data.csv').is_file():
            print('no metadata file exists, creating...')
            kdm_table = pd.DataFrame(columns=['kdd_id',
                                              'kdd_version', 
                                              'project_id', 
                                              'creation_timestamp', 
                                              'is_annotated',
                                              'has_encoded_pdf',
                                              'entity_type_mapping_hash',
                                              'details'])
            kdm_table.to_csv(output_dir_path.joinpath('_meta_data.csv'), index=False)
        try:
            with output_path.open('wb') as file:
                msgpack.dump(self, file, default=KDD._serialize_kdd)
            kdm_table = pd.read_csv(output_dir_path.joinpath('_meta_data.csv'))
            if self.uuid in kdm_table.kdd_id.to_list():
                kdm_table = kdm_table[kdm_table.kdd_id != self.uuid]
            kdm_table = kdm_table.append({
                'kdd_id': self.uuid,
                'kdd_version': self.version, 
                'project_id': self.project_id, 
                'creation_timestamp': self.creation_timestamp, 
                'is_annotated': len(self.entity_annotations) > 0,
                'has_encoded_pdf': self.has_encoded_pdf(),
                'entity_type_mapping_hash': self.get_entity_type_mapping_hash(),
                'details': self.details
            }, ignore_index=True)
            kdm_table.to_csv(output_dir_path.joinpath('_meta_data.csv'), index=False)
        except Exception as e:
            raise Exception(f'an exception occured while writing kdd to file:\n{e}')

    @staticmethod
    def from_gcp_blob(blob, load_encoded_pdf=False):
        # TODO: In progress
        # TODO: test this with pdf and without (KDD_manager makes the google cloud connection)
        path = Path(blob.name)
        if not path.suffix == '.kdd':
            raise ValueError('not a .kdd path')
        try:
            uuid = uuid_lib.UUID(path.stem)
        except ValueError as e:
            raise ValueError('filename project incorrect uuid')

        kddfile = msgpack.unpackb(blob.download_as_bytes(), object_hook=partial(KDD._deserialize_kdd, uuid=uuid))
        return kddfile

    def encode_pdf(self, pdf_path):
        if not isinstance(pdf_path, Path):
            pdf_path = Path(pdf_path)
        try:
            uuid_lib.UUID(pdf_path.stem)
        except ValueError as e:
            raise Exception(f'filename "{pdf_path.stem}" is not a valid UUID. The filename should be the document UUID.')
        with pdf_path.open('rb') as pdf_file:
            self.encoded_pdf = EncodedPDF(filename=pdf_path.name, 
                                          compressed_data=zlib.compress(pdf_file.read()))

    def decode_pdf(self, output_dir):
        if not isinstance(output_dir, Path):
            output_dir = Path(output_dir)
        if not self.encoded_pdf:
            raise Exception('no encoded pdf present')
        if not self.has_encoded_pdf():
            raise Exception('encoded pdf data was not loaded')
        decompressed_data = zlib.decompress(self.encoded_pdf.compressed_data)
        if not output_dir:
            return decompressed_data
        if not isinstance(output_dir, Path):
            output_dir = Path(output_dir)
        if not output_dir.is_dir():
            raise ValueError('not a directory path')
        with output_dir.joinpath(self.encoded_pdf.filename).open('wb') as output_file:
            output_file.write(decompressed_data)
        return output_dir.joinpath(self.encoded_pdf.filename)

    def has_encoded_pdf(self):
        if not self.encoded_pdf:
            return False
        if not self.encoded_pdf.filename or not self.encoded_pdf.compressed_data:
            return False
        return True

    def _sort_entity_type_mappings(self):
        self.entity_type_mappings.sort(key=lambda entity_type_mapping: entity_type_mapping.id)

    def _sort_entity_annotations(self):
        self.entity_annotations.sort(key=lambda entity_annotation: (entity_annotation.page_nr, entity_annotation.token_id))

    def _sort_text_layers(self):
        for text_layer in self.text_layers:
            text_layer.sort_tokens_information()
        self.text_layers.sort(key=lambda text_layer: text_layer.page_nr)

    def full_sort(self):
        self._sort_text_layers()
        self._sort_entity_annotations()
        self._sort_entity_type_mappings()

    def normalize_internal_coordinates(self):
        for text_layer in self.text_layers:
            page_nr = text_layer.page_nr
            max_dimension = text_layer.max_dimension
            text_layer.normalize_coordinates()

            for ea in self.entity_annotations:
                if ea.page_nr == page_nr:
                    ea.normalize_coordinates(max_dimension)
                    
    def get_internal_entity_id(self, db_entity_id):
        for mapping in self.entity_type_mappings:
            if mapping.db_id == db_entity_id:
                return mapping.id
        raise ValueError('No entity type mapping found for the given database entity id')

    def get_db_entity_id(self, internal_entity_id):
        for mapping in self.entity_type_mappings:
            if mapping.id == internal_entity_id:
                return mapping.db_id
        raise ValueError('No entity type mapping found for the given internal entity id')

    def get_entity_type_mapping_hash(self):
        self.full_sort()
        return hash(''.join([entity_mapping.name for entity_mapping in self.entity_type_mappings]))

    def display(self,
                font_size=10,
                font="/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
                color_mappings={},
                dpi=DPI,
                coordinates_scale=1,
                display_annotations=False,
                group_types=[],
                print_entity_mappings=False):
        if print_entity_mappings:
            print('\nentity mappings:')
            for mapping in self.entity_type_mappings:
                print(f'   {mapping.id}\t-->\t{mapping.name}')
                
        font = ImageFont.truetype(font, font_size, encoding="unic")
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_pdf_path = self.decode_pdf(temp_dir)
            page_images = convert_from_path(temp_pdf_path, dpi=dpi)
            for page_index, page_image in enumerate(page_images):
                page_image.putalpha(120)
                page_nr = page_index + 1
                if display_annotations:
                    page_annotations = [annotation for annotation in self.entity_annotations if annotation.page_nr == page_nr]
                    entity_group_boxes = {}
                    for annotation in page_annotations:
                        if annotation.entity_type == 0:
                            continue
                        if annotation.entity_type in color_mappings:
                            color = color_mappings[annotation.entity_type]
                        else: 
                            color = tuple(np.random.choice(range(200), size=3))
                            color_mappings[annotation.entity_type] = color
                        if annotation.group_type in group_types:
                            top = annotation.bounding_box.top_left.y
                            left = annotation.bounding_box.top_left.x
                            bottom = annotation.bounding_box.bottom_right.y
                            right = annotation.bounding_box.bottom_right.x
                            key = (annotation.group_type, annotation.group_instance_index)
                            if key not in entity_group_boxes:
                                entity_group_boxes[key] = {'top': top, 'left': left, 'bottom': bottom, 'right': right}
                            else:
                                entity_group_boxes[key]['top'] = min(entity_group_boxes[key]['top'], top)
                                entity_group_boxes[key]['left'] = min(entity_group_boxes[key]['left'], left)
                                entity_group_boxes[key]['bottom'] = max(entity_group_boxes[key]['bottom'], bottom)
                                entity_group_boxes[key]['right'] = max(entity_group_boxes[key]['right'], right)
                        drawn = ImageDraw.Draw(page_image)  
                        drawn.rectangle(annotation.bounding_box.to_list(coordinates_scale=coordinates_scale, order='ltrb'),
                                        fill=None,
                                        outline=color)
                        drawn.text((annotation.bounding_box.top_left.x / coordinates_scale,
                                    annotation.bounding_box.top_left.y / coordinates_scale - font_size),
                                   str(annotation.entity_type),
                                   font=font,
                                   fill=color)
                    for box in entity_group_boxes:
                        drawn = ImageDraw.Draw(page_image)  
                        drawn.rectangle(((entity_group_boxes[box]['left'] - 1) / coordinates_scale, 
                                         (entity_group_boxes[box]['top'] - 1) / coordinates_scale,
                                         (entity_group_boxes[box]['right'] + 1) / coordinates_scale,
                                         (entity_group_boxes[box]['bottom'] + 1) / coordinates_scale),
                                        outline=(0, 0, 0),
                                        fill=None)
                figure, axis = plt.subplots(1, 1, figsize=(20, 20))
                axis.set_title(f'project: {self.project_id}\nfilename: {self.encoded_pdf.filename}\npage: {page_nr}', 
                               loc='left')
                axis.imshow(page_image)
                figure.show()