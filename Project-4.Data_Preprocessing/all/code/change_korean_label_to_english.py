#Make sure that you have matching table csv named `table.csv` with columns `original`, change_to`


import lxml.html   # check https://pypi.org/project/lxml/
from csv import reader
from os.path import exists
import glob


def update_xml(path: str) -> None:
    with open('./table.csv', 'r') as convertions, open(path, 'r') as annotation:  # noqa: E501
        tree = lxml.html.fromstring(annotation.read())
        csv_reader = reader(convertions)

        for idx, row in enumerate(csv_reader, start=1):
            if idx == 1:
                continue

            original, change_to = row

            find_class = tree.xpath(f".//name[text()='{original}']")

            for sub_class in find_class:
                sub_class.text = change_to

                print(f'Changed class {original} to {change_to} in {path}')

    with open(path, 'wb') as annotation:  #open xml file path
        new_content = lxml.html.tostring(tree)

        if new_content.strip():
            annotation.write(new_content)

    print(f'Processing on {path} done')


if __name__ == '__main__':
    for xml_file in glob.glob('./test/*.xml'):
        if exists(xml_file):
            update_xml(path=xml_file)

        #classes.append(row)
        #print(classes)

            #tags = tree.findall(f".//name[text()='{original_col}']")
            #print(tags)

        #     for tag in tags:
        #         tag.text = change_to

        #         print(f'Changed class {original_col} to {change_to}')


        #     new_content = lxml.html.tostring(tree)
        #     print(new_content)

        # if new_content.strip():
        #     tree.write(new_content)
