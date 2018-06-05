import itertools
import os
import subprocess
import tempfile

from lxml import etree


FEATURES = ['PyQt_Accessibility', 'PyQt_SessionManager', 'PyQt_SSL',
            'PyQt_qreal_double', 'Py_v3', 'PyQt_PrintDialog', 'PyQt_Printer',
            'PyQt_PrintPreviewWidget', 'PyQt_PrintPreviewDialog',
            'PyQt_RawFont', 'PyQt_OpenGL', 'PyQt_Desktop_OpenGL',
            'PyQt_NotBootstrapped']
PLATFORMS = ['WS_X11', 'WS_WIN', 'WS_MACX']
TIMELINE = ['Qt_5_0_0', 'Qt_5_0_1', 'Qt_5_0_2', 'Qt_5_1_0', 'Qt_5_1_1',
            'Qt_5_2_0', 'Qt_5_2_1', 'Qt_5_3_0', 'Qt_5_3_1', 'Qt_5_3_2',
            'Qt_5_4_0', 'Qt_5_4_1', 'Qt_5_4_2', 'Qt_5_5_0']


def run_sip(module, outdir, sip_executable):
    for exclusive_tags in itertools.product(TIMELINE, PLATFORMS):
        filename = '{}-{}.xml'.format(module, '-'.join(exclusive_tags))
        outfile = os.path.join(outdir, filename)
        cmdline = [sip_executable, '-m', outfile]
        for tag in list(exclusive_tags) + FEATURES:
            cmdline += ['-t', tag]
        cmdline.append(
            os.path.join(module, '{}mod.sip'.format(module)))
        print('  {} -> {}'.format(', '.join(exclusive_tags), outfile))
        subprocess.call(cmdline)


def parse_xmls(xmldir):
    for basename in os.listdir(xmldir):
        xmlfile = os.path.join(xmldir, basename)
        with open(xmlfile, 'r') as f:
            tree = etree.parse(f)
        yield from tree.xpath('/Module/Class/Function[@virtual="1"]/@name')


def get_modules():
    for filename in os.listdir('.'):
        filepath = os.path.abspath(filename)
        if os.path.isdir(filepath):
            yield filename


def create_whitelist(args):
    print(args)
    with open('whitelist.py', 'w') as outfile:
        for module in get_modules():
            with tempfile.TemporaryDirectory() as tmpdir:
                outfile.write('# {}\n'.format(module))
                name_set = set()
                print("Running sip for {}...".format(module))
                run_sip(module, tmpdir, args.sip[0])
                print("Parsing and merging XML files...")
                print()
                for name in parse_xmls(tmpdir):
                    name_set.add(name)
                for name in sorted(name_set):
                    outfile.write('{}.{}\n'.format(module, name))
                outfile.write('\n')
                outfile.flush()
