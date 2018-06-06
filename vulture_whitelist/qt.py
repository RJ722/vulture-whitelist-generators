import itertools
import os
import subprocess
import tempfile

from .utils import log

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


class QtWhitelistCreator:
    """
    Takes in sip files and emits a whitelist.
    """

    def __init__(self, args):
        self.sip = args.sip[0]
        self.whitelist_name = args.name[0]

    def _write_mod_whitelist(self, f, module, name_set):
        f.write('# {}\n'.format(module))
        for name in sorted(name_set):
            f.write('{}.{}\n'.format(module, name))
        f.write('\n')
        f.flush()

    def _prepare_sip_command(self, module, outdir, sip_executable):
        for exclusive_tags in itertools.product(TIMELINE, PLATFORMS):
            filename = '{}-{}.xml'.format(module, '-'.join(exclusive_tags))
            outfile = os.path.join(outdir, filename)
            cmdline = [sip_executable, '-m', outfile]
            for tag in list(exclusive_tags) + FEATURES:
                cmdline += ['-t', tag]
            cmdline.append(
                os.path.join(module, '{}mod.sip'.format(module)))
            log('  {} -> {}'.format(', '.join(exclusive_tags), outfile))
            yield cmdline

    def create_xml(self, module, outdir, sip_executable):
        log("Running sip for {}...".format(module))
        for sipcmd in self._prepare_sip_command(
                module, outdir, sip_executable):
            subprocess.call(sipcmd)

    def get_modules(self):
        for filename in os.listdir():
            filepath = os.path.abspath(filename)
            if os.path.isdir(filepath):
                yield filename

    def parse_xmls(self, xmldir):
        for basename in os.listdir(xmldir):
            xmlfile = os.path.join(xmldir, basename)
            with open(xmlfile, 'r') as f:
                tree = etree.parse(f)
            yield from tree.xpath('/Module/Class/Function[@virtual="1"]/@name')

    def name_set(self, xmldir):
        log("Parsing and merging XML files for {}\n".format(xmldir))
        name_set = set()
        for name in self.parse_xmls(xmldir):
            name_set.add(name)
        return name_set

    def create_mod_whitelist(self, module, outfile):
        with tempfile.TemporaryDirectory() as tmpdir:
            self.create_xml(module, tmpdir, self.sip)
            self._write_mod_whitelist(outfile, module, self.name_set(tmpdir))

    def create(self):
        with open(self.whitelist_name, 'w') as outfile:
            for module in self.get_modules():
                self.create_mod_whitelist(module, outfile)
