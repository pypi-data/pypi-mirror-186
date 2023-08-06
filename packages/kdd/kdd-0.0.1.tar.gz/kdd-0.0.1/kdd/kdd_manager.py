from pydantic import BaseModel
import pandas as pd
from pathlib import Path
from kdd import KDD
import json
from ast import literal_eval

class KDDManager(BaseModel):
    def load_kdd_files(self,
                             kdd_directory, 
                             meta_data_filename='_meta_data.csv',
                             path_as_string=False,
                             kdd_version=None, 
                             project_id=None, 
                             before_timestamp=None, 
                             after_timestamp=None, 
                             is_annotated=None, 
                             has_encoded_pdf=None,
                             entity_type_mapping_hash=None,
                             details_filter=None):
        output_list = []
        if not isinstance(kdd_directory, Path):
            kdd_directory = Path(kdd_directory)
        try:
            meta_data = pd.read_csv(kdd_directory / meta_data_filename)
        except Exception as e:
            print(f'could not read {meta_data_filename}')
            return
        for kdd_path in kdd_directory.iterdir():
            try:
                if kdd_path.suffix != '.kdd':
                    continue
                if kdd_version != None:
                    if str(kdd_version) != str(meta_data[meta_data.kdd_id == kdd_path.stem].kdd_version.iloc[0]):
                        continue
                if project_id != None:
                    if str(project_id) != str(meta_data[meta_data.kdd_id == kdd_path.stem].project_id.iloc[0]):
                        continue
                if before_timestamp != None:
                    if int(before_timestamp) < int(meta_data[meta_data.kdd_id == kdd_path.stem].creation_timestamp.iloc[0]):
                        continue
                if after_timestamp != None:
                    if int(after_timestamp) > int(meta_data[meta_data.kdd_id == kdd_path.stem].creation_timestamp.iloc[0]):
                        continue
                if is_annotated != None:
                    if bool(is_annotated) != bool(meta_data[meta_data.kdd_id == kdd_path.stem].is_annotated.iloc[0]):
                        continue
                if has_encoded_pdf != None:
                    if bool(has_encoded_pdf) != bool(meta_data[meta_data.kdd_id == kdd_path.stem].has_encoded_pdf.iloc[0]):
                        continue
                if entity_type_mapping_hash != None:
                    if int(entity_type_mapping_hash) != int(meta_data[meta_data.kdd_id == kdd_path.stem].entity_type_mapping_hash.iloc[0]):
                        continue
                if details_filter != None:
                    if not isinstance(details_filter, dict) or len(details_filter) == 0:
                        raise ValueError('details_filter: provide a dictionary to filter on')
                    details = literal_eval(meta_data[meta_data.kdd_id == kdd_path.stem].details.iloc[0])
                    details_filter_checked_out = True
                    for key in details_filter:
                        if key not in details:
                            details_filter_checked_out = False
                            break
                        if isinstance(details_filter[key], list):
                            for value in details_filter[key]:
                                if details[key] == value:
                                    details_filter_checked_out = True
                                    break
                                details_filter_checked_out = False
                        elif details[key] != details_filter[key]:
                            details_filter_checked_out = False
                    if not details_filter_checked_out:
                        continue
                if path_as_string:
                    kdd_path = str(kdd_path)
                output_list.append(kdd_path)
            except IndexError as e:
                print(f'{meta_data_filename} is corrupt, please rebuild it')
        return output_list

    def rebuild_meta_data(self, kdd_directory, meta_data_filename='_meta_data.csv'):
        if not isinstance(kdd_directory, Path):
            kdd_directory = Path(kdd_directory)
        kdm_table = pd.DataFrame(columns=['kdd_id',
                                          'kdd_version', 
                                          'project_id', 
                                          'creation_timestamp', 
                                          'is_annotated',
                                          'has_encoded_pdf',
                                          'entity_type_mapping_hash',
                                          'details'])
        kdm_table.to_csv(kdd_directory.joinpath(meta_data_filename), index=False)
        for kdd_path in kdd_directory.iterdir():
            if kdd_path.suffix != '.kdd':
                continue
            kdd = KDD.from_file(kdd_path)
            kdm_table = pd.read_csv(kdd_directory.joinpath(meta_data_filename))
            if kdd_path.stem in kdm_table.kdd_id.to_list():
                kdm_table = kdm_table[kdm_table.kdd_id != kdd_path.stem]
            kdm_table = kdm_table.append({
                'kdd_id': kdd_path.stem,
                'kdd_version': kdd.version, 
                'project_id': kdd.project_id, 
                'creation_timestamp': kdd.creation_timestamp, 
                'is_annotated': len(kdd.entity_annotations) > 0,
                'has_encoded_pdf': kdd.has_encoded_pdf(),
                'entity_type_mapping_hash': kdd.get_entity_type_mapping_hash(),
                'details': kdd.details
            }, ignore_index=True)
            kdm_table.to_csv(kdd_directory.joinpath(meta_data_filename), index=False)

    def get_kdd_creation_history(self, kdd_directory, meta_data_filename='_meta_data.csv', path_as_string=False):
        if not isinstance(kdd_directory, Path):
            kdd_directory = Path(kdd_directory)
        try:
            meta_data = pd.read_csv(kdd_directory / meta_data_filename)
        except Exception as e:
            print(f'could not read {meta_data_filename}')
            return

        meta_data['creation_timestamp'] = (
            pd.to_datetime(meta_data['creation_timestamp'], unit='s').dt.floor('d').dt.strftime('%Y-%m-%d'))

        df = meta_data.groupby(meta_data["creation_timestamp"])['kdd_id'].apply(list)

        if path_as_string:
            df = df.apply(lambda x: [str(kdd_directory.resolve() / (_id + '.kdd')) for _id in x])
        else:
            df = df.apply(lambda x: [kdd_directory.resolve() / (_id + '.kdd') for _id in x])

        return df.to_dict()

    def remove_kdd_files(self, kdd_directory, kdd_paths_to_remove, meta_data_filename='_meta_data.csv'):
        if not isinstance(kdd_directory, Path):
            kdd_directory = Path(kdd_directory)
        try:
            meta_data = pd.read_csv(kdd_directory / meta_data_filename)
        except Exception as e:
            print(f'could not read {meta_data_filename}', e)
            return

        kdd_ids_to_remove = []
        for kdd_to_remove in kdd_paths_to_remove:
            if isinstance(kdd_to_remove, str):
                kdd_to_remove = Path(kdd_to_remove)
            kdd_to_remove.unlink()
            kdd_ids_to_remove.append(kdd_to_remove.stem)

        meta_data = meta_data[~ meta_data['kdd_id'].isin(kdd_ids_to_remove)]
        meta_data.to_csv(kdd_directory.joinpath(meta_data_filename), index=False)

