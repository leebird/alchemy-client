from submodules.annotation.readers import RlimsVerboseReader

def process(filepath):
    parser = RlimsVerboseReader()
    annotations_packed = {}

    # read annotation and text
    verbose_file = filepath + '.verbose'
    print(verbose_file)
    tuples = parser.parse_file(verbose_file)
    annotations = parser.to_ann(tuples)
    
    for doc_id, annotation in annotations.items():
        annotations_packed[doc_id] = annotation.pack()

    return annotations_packed