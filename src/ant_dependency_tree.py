from xml.etree import ElementTree


def main():
    build_file_path = r'/path/to/build.xml'
    root = ElementTree.parse(build_file_path)

    # target name to list of names of dependencies
    target_deps = {}

    for t in root.iter('target'):
        if 'depends' in t.attrib:
            deps = [d.strip() for d in t.attrib['depends'].split(',')]
        else:
            deps = []
        name = t.attrib['name']
        target_deps[name] = deps

    def print_target(target, depth=0):
        indent = '  ' * depth
        print
        indent + target
        for dep in target_deps[target]:
            print_target(dep, depth + 1)

    for t in target_deps:
        print
        print_target(t)


if __name__ == "__main__":
    main();
