from extractors import extract_from_filepath

if __name__ == '__main__':
    json_file = "data/movies.json"
    xml_file = "data/person.xml"
    html_file = "data/something.html"

    for file_path in [json_file, xml_file, html_file]:
        extractor = extract_from_filepath(file_path)
        print(file_path, extractor.parsed_data())
