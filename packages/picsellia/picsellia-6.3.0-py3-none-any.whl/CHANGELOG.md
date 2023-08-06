
# Changelog

Picsellia SDK Python is a library that allows users to connect to Picsellia backend.

All notable changes to this project will be documented in this file.

## [6.3.0] - 2023-01-19
Happy new year from the Picsellia Team !
This minor version add some useful methods and fix specified COCOFile format.

### Added
- List public models with `list_public_models()` from the Picsellia Hub in Client.
- Find public model with `find_public_model()` from the Picsellia Hub in Client.
- Convert MultiAsset into MultiData with `as_multidata()` and `as_list_of_data()`
- Allow asset tags to be added when adding data to a dataset with `add_data()`
- Method `__repr__` has been added to MultiObjects
- Property `labels` in ModelVersion objects
- Add `get_dataset` in ModelContext to get DatasetVersion from its attached name

### Fix
- **breaking**: COCOFile was wrongly specified: in annotations, only one segmentation was allowed for each shape,
but COCOFile allows multiple polygons. Now you need to give a list of list of coordinates instead of only one list of coordinates.
`import_annotations_coco_file()` should now work fine with COCO files with segmentation.
- Add AuthenticationError again in exceptions, which was used by picsellia-tf2

### Changed
- **may be breaking**: Default value of force_create_label is now True in `import_annotations_coco_file` and `import_annotation_voc_file`.
- Rename `retrieve_experiment` into `get_experiment` in ModelContext
- `retrieve_datasets` in ModelContext now return a dict with attached name as key and dataset version as value
- `download()` a DatasetVersion is not calling assets extended endpoints which was taking a lot of time on huge datasets.
- Imports order with pre-commit cln tool
- Doc generation with all properties docstring

## [6.2.1] - 2022-27-12
### Fixed
- Fixed .predict() behavior by removing mandatory parameters tags and source


## [6.2.0] - 2022-27-12
### Added
- Add docker env variables support on ModelVersion
- Add an experiment.log_parameters() to use experiment.log() with parameters more easily
- Add possibility to attach base parameters when experiment.attach_model()
- Add feedbackloop method check status
- Add `__repr__` methods to DAO objects, for better UX representation
- Add possibility to set tags and source when sending a prediction to serving
- Add get_or_create_datasource() in client

### Changed
- Rename experiment.publish() into experiment.export_as_model()
- Some changes on feedbackloop methods
- Method list_data and list_assets can now use parameter `intersect_tags` to find objects that have all tags given
- Allow Path object in every method that accept path as string
- Some exceptions were renamed, some useless were removed

## [6.1.2] - 2022-01-10
### Fixed
- Use of typing.List instead of list to support python < 3.9

## [6.1.1] - 2022-01-10
### Added
- Add convert_tags_to_classification() in dataset version
- Add get_data_tags() on asset

### Changed
- Github workflow

## [6.1.0] - 2022-01-01
### Added
- Add ONXX in Framework enums
- Possibility to use strings instead of enums in methods

### Changed
- Make duration optional in annotation creation/update/overwrite
- Make duration int compatible
- log() method now create, update or append a log, in only one call to backend
- Remove create_log method
- Optional type hint is now used everywhere
- Prevent user from updating log image via log.update(), only experiment.log can be used for this case

### Fixed
- In log() method, image type data stored bad values

## [6.0.2] - 2022-10-17
### Added
- Logging File for an Experiment

### Changed
- A lot of typos, variable naming, minor formatting
- String .format() into f-strings
- Old package dependencies
- train_test_split() return MultiAsset instead of List[Asset]

### Fixed
- Regeneration of JWT when expired
- When downloading file, open file only if response is ok

## [6.0.1] - 2022-10-04
### Added
- CHANGELOG file.

### Changed
- Fixed test_train_split with breaking changes of query language in list assets.
- Documentation of core functions, minor typos fixes.
- Workflow for testing on staging when push on development and main.

## [6.0.0] - 2022-10-03
### Added
- Annotation are now objects storing Rectangle, Polygon, Classification, Point and Line for an Asset
- Artifact are now Experiment files stored
- DatasetVersion are now used as versions of Dataset
- Datalake objects
- Datasource objects
- Job objects, to wait for tasks to end
- ModelVersion are now used as versions of Model
- ScanFiles are now Scan files stored

### Changed
- Pictures renamed to Asset that are Data objects in a DatasetVersion
- Multithreading usage
- Tags
- Annotations with objects
