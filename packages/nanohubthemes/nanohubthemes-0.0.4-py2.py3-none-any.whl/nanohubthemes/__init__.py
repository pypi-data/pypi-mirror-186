from __future__ import print_function
import os
import sys
from argparse import ArgumentParser
from glob import glob
from . import stylefx
from ._version import __version__, version_info
import sys
import os
import glob
import shutil
import signal
import argparse
import json
import binascii
from subprocess import call, Popen, check_output
from jupyter_contrib_nbextensions.application import InstallContribNbextensionsApp, UninstallContribNbextensionsApp
from jupyter_contrib_core.notebook_compat import nbextensions

from string import Template
import time

try:
    import matplotlib as mpl
    from jupyter_core.paths import jupyter_config_dir
    from . import jtplot
except ModuleNotFoundError:
    pass


def get_hidden_extensions():
    return [
        ("notebook","nbextensions_configurator/config_menu/main"),
        ("notebook","contrib_nbextensions_help_item/main"),
        ("tree","nbextensions_configurator/tree_tab/main")
    ] 

def get_theme_extensions():
    return [
        ("notebook","codefolding/main"), #Code Folding
        ("notebook","code_prettify/code_prettify"), #Code prettify
        ("notebook","varInspector/main"), # Variable inspector
        #("notebook","cell_filter/cell_filter"),
        #("notebook","scratchpad/main"): true,
        ("notebook","toc2/main"), #Table of content icon
        ("notebook","freeze/main"), # freeze cells
        ("notebook","execute_time/ExecuteTime"), # execution time
        ("notebook","highlight_selected_word/main"), #Higllight selecte word
        ("notebook","ruler/main"), # ruler
        ("notebook","toggle_all_line_numbers/main"), # line number icon
        ("notebook","printview/main"), # print icon
        ("notebook","table_beautifier/main"), # Beatufy tables
        ("notebook","addbefore/main"), #Add cell before
        ("notebook","livemdpreview/livemdpreview"), #MarkDown Preview
        ("notebook","skip-traceback/main"), #Hide traces
        ("tree","tree-filter/index"), #Filter tree
        ("edit","codefolding/edit"), #Code Edit
        ("notebook","ruler/main"), #Ruler norebook
        ("edit","ruler/edit"), #Ruler Editor
        ("notebook","execute_time/ExecuteTime"), #Add execution request time
    ]

def get_current_theme():
    return stylefx.getCurrentTheme()

def get_themes():
    return stylefx.getThemes()


def reset_theme():
    stylefx.reset_default(False)
    print("Theme  has been Updated");

def install_theme(theme=None,
                monofont=None,
                monosize=11,
                nbfont=None,
                nbfontsize=13,
                tcfont=None,
                tcfontsize=13,
                dffontsize=93,
                outfontsize=85,
                mathfontsize=100,
                margins='auto',
                cellwidth='980',
                lineheight=170,
                cursorwidth=2,
                cursorcolor='default',
                altprompt=False,
                altmd=False,
                altout=False,
                hideprompt=False,
                vimext=False,
                toolbar=False,
                nbname=False,
                kernellogo=False,
                dfonts=False,
                keepcustom=False):

    """ Install theme to jupyter_customcss with specified font, fontsize,
    md layout, and toolbar pref
    """
    # get working directory
    wkdir = os.path.abspath('./')

    if keepcustom:
        stylefx.save_customizations()

    stylefx.reset_default(False)
    stylefx.check_directories()

    doc = '\nConcatenated font imports, .less styles, & custom variables\n'
    s = '*' * 65
    style_less = '\n'.join(['/*', s, s, doc, s, s, '*/'])
    style_less += '\n\n\n'
    style_less += '/* Import Notebook, Markdown, & Code Fonts */\n'

    # initialize style_less & style_css
    style_less = stylefx.set_font_properties(
        style_less=style_less,
        monofont=monofont,
        monosize=monosize,
        nbfont=nbfont,
        nbfontsize=nbfontsize,
        tcfont=tcfont,
        tcfontsize=tcfontsize,
        dffontsize=dffontsize,
        outfontsize=outfontsize,
        mathfontsize=mathfontsize,
        dfonts=dfonts)

    if theme is not None:
        # define some vars for cell layout
        cursorcolor = stylefx.get_colors(theme=theme, c=cursorcolor)
        style_less = stylefx.style_layout(
            style_less,
            theme=theme,
            cellwidth=cellwidth,
            margins=margins,
            lineheight=lineheight,
            altprompt=altprompt,
            altmd=altmd,
            altout=altout,
            hideprompt=hideprompt,
            cursorwidth=cursorwidth,
            cursorcolor=cursorcolor,
            vimext=vimext,
            toolbar=toolbar,
            nbname=nbname,
            kernellogo=kernellogo)

    # compile tempfile.less to css code and append to style_css
    style_css = stylefx.less_to_css(style_less)

    # append mathjax css & script to style_css
    style_css = stylefx.set_mathjax_style(style_css, mathfontsize)

    # install style_css to .jupyter/custom/custom.css
    stylefx.write_final_css(style_css)

    # change back to original working directory
    os.chdir(wkdir)

    # restore customization from custom.js
    if keepcustom:
        stylefx.restore_customizations()

    print("Theme  " + str(theme) + " Updated");

def handler(signum, frame):
    global notebookProcess
    print("%s Signal %d received.\n" % (time.ctime(),signum))
    sys.stdout.flush()  # make sure this gets displayed now.
    if notebookProcess:
        try:
            print("%s killing notebookProcess = %d" % (time.ctime(),notebookProcess.pid))
            sys.stdout.flush()  # make sure this gets displayed now.
#           os.kill(notebookProcess.pid,signal.SIGTERM)
            notebookProcess.terminate()
        except:
            print("%s killing notebookProcess = %d failed" % (time.ctime(),notebookProcess.pid))
            sys.stdout.flush()  # make sure this gets displayed now.

def completeHandler(signum, frame):
    global notebookProcess

    print("%s child process killed(%d)" % (time.ctime(),signum))
    sys.stdout.flush()  # make sure this gets displayed now.


signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGHUP, handler)
signal.signal(signal.SIGTERM, handler)
signal.signal(signal.SIGCHLD, completeHandler)

def parse_cmd_line():
    prog = "start_jupyter"

    parser = argparse.ArgumentParser(
        usage="""usage: %(prog)s [-h] [-t] [-c] [-d] [-A] [-T dir] [name]

Start a Jupyter notebook-based tool

positional arguments:
  name        Name of notebook to run.  The terminal and
              dashboard (tree view of files) will de disabled.

              If no name is given, a notebook server will
              be started in the current directory.  Terminal
              and dashboard will be enabled.

optional arguments:
  -h, --help  show this help message and exit.
  -d          Show debug (verbose) output.
  -t          Run as a Tool with no notebook controls.
  -c          Copy instead of link notebook files.
  -A          Run in AppMode.
  -T dir      Search for notebook starting in dir.
""",
        prog=prog,
        add_help=False)
    parser.add_argument('-t', dest='tool', action='store_true')
    parser.add_argument('-A', dest='app', action='store_true')
    parser.add_argument('-d', dest='debug', action='store_true')
    parser.add_argument('-c', dest='copyNotebooks', action='store_true')
    parser.add_argument('-T')
    parser.add_argument('-h', '--help', dest='help', action='store_true')
    parser.add_argument('name', nargs='?')
    return parser


def get_session():
    try:
        session = os.environ['SESSION']
        sessiondir = os.environ['SESSIONDIR']
    except:
        session = ""

    if session != "":
        return session, sessiondir

    # something went wrong. restore environment variables
    psout = check_output(['ps', 'auxwwe']).split('\n')
    for line in psout:
        ind = line.find('SESSIONDIR')
        if ind > 0:
            sessiondir = line[ind:].split(' ')[0]
            display = line[line.find('DISPLAY'):].split(' ')[0]
            break
    session = sessiondir.split('/')[-1]
    sessiondir = sessiondir.split('=')[1]
    display = display.split('=')[1]
    os.environ['SESSION'] = session
    os.environ['SESSIONDIR'] = sessiondir
    os.environ['DISPLAY'] = display
    return session, sessiondir

def get_proxy_addr():
    session, sessiondir = get_session()
    fn = os.path.join(sessiondir, 'resources')
    with open(fn, 'r') as f:
        res = f.read()
    for line in res.split('\n'):
        if line.startswith('hub_url'):
            url = line.split()[1]
        elif line.startswith('filexfer_port'):
            fxp = str(int(line.split()[1]) % 1000)
        elif line.startswith('filexfer_cookie'):
            fxc = line.split()[1]
    url_path = "/weber/%s/%s/%s/" % (session, fxc, fxp)
    proxy_url = "https://proxy." + url.split('//')[1] + url_path
    return url_path, proxy_url


def get_cookie():
    cookie_name = ""
    try:
        session = int(os.environ['SESSION'])
        pwfile = glob.glob('/var/run/Xvnc/passwd-*')[0]
        with open(pwfile, 'rb') as f:
            pwd = binascii.hexlify(f.read()).decode('utf-8')
            token = "%d:%s" % (session, str(pwd))

        fn = os.path.join(os.environ['SESSIONDIR'], 'resources')
        with open(fn, 'r') as f:
            res = f.read()
        for line in res.split('\n'):
            if line.startswith('hub_url'):
                url = line.split()[1]
                host = url[url.find('//') + 2:]
                cookie_name = 'weber-auth-' + host.replace('.', '-')
                break
    except:
        # not running on a hub
        return "", ""
    return cookie_name, token


def find_notebook(name, tool, copyNotebooks, arglist):
    if tool is None:
        if not os.path.isfile(name):
            print("Cannot find %s." % name, file=sys.stderr)
            sys.exit(1)
        return os.path.split(name)

    # We are running a published notebook.
    # symlink copy it to RESULTSDIR
    tname = os.path.basename(os.path.dirname(tool))
    tdest = os.path.join(os.environ['RESULTSDIR'], tname)

    # remove and make tdest
    if os.path.exists(tdest):
        shutil.rmtree(tdest)
    os.makedirs(tdest)

    realPath = os.path.realpath(os.path.abspath(tool))
    call("cp -sRf %s/* %s" % (realPath,tdest), shell=True)
    if copyNotebooks:
        call("""( cd %s; find ./ -name "*.ipynb" -exec /bin/cp --remove-destination {} %s/{} \; )""" % (realPath,tdest),shell=True)

    # notebook will be either relative to the tool
    # directory or in the bin directory
    nb_name = os.path.abspath(os.path.join(tdest, name))
    if not os.path.isfile(nb_name):
        # look in bin dir
        nb_name = os.path.abspath(os.path.join(tdest, 'bin', name))
        if not os.path.isfile(nb_name):
            print("Cannot find %s." % name, file=sys.stderr)
            sys.exit(1)

    return os.path.split(nb_name)



def install_contrib():
    #Install Contrib extensions
    app = InstallContribNbextensionsApp()
    app.user = True
    app.symlink = True
    app.start()

    #Enable Default  extensions
    for e in get_theme_extensions():
        nbextensions._set_nbextension_state(e[0], e[1],True, user=True)

    #Disable references to Contrib Extensions
    for e in get_hidden_extensions():
        nbextensions._set_nbextension_state(e[0], e[1],False, user=True)

def uninstall_contrib():
    #Disable references to Contrib Extensions
    for e in get_theme_extensions()+get_hidden_extensions():
        nbextensions._set_nbextension_state(e[0], e[1],False, user=True)

    #Unnstall Contrib extensions
    app = UninstallContribNbextensionsApp()
    app.user = True
    app.symlink = True
    app.start()

def run_notebook(args):
    global notebookProcess

    arglist = []

    if args.name is None:
        if args.tool:
            parser.error("ERROR: -t with no filename.\n")
        if args.T:
            os.chdir(os.environ['HOME'])

    else:
        nb_dir, nb_name = find_notebook(args.name, args.T, args.copyNotebooks, arglist)
        if nb_dir:
            print("Changing directory to", nb_dir)
            os.chdir(nb_dir)

        if args.app:
            arglist.append('--NotebookApp.default_url="apps/%s"' % nb_name)
        else:
            arglist.append('--NotebookApp.default_url="notebooks/%s"' % nb_name)
# disable ~/.local/lib/pythonX.Y/site-packages for tools
        os.environ['PYTHONNOUSERSITE'] = "yes"

    # Users probably want "bash"
    workspace = "SHELL" in os.environ
    os.environ['SHELL'] = "/bin/bash"

    p_path, p_url = get_proxy_addr()
    cmdlist = [
              "jupyter", "notebook", "--no-browser", "--port=8000",
              "--ip=0.0.0.0",
              '--NotebookApp.base_url="%s"' % p_path
              ]

    token = get_cookie()[1]
    if token:
        cmdlist.append('--NotebookApp.token=%s' % token)

    if args.debug:
        cmdlist.append('--Application.log_level="DEBUG"')
    cmdlist += arglist

    urlstring = "%s?token=%s" % (p_url, token)
    print("=" * len(urlstring))
    print("URL is\n%s" % urlstring)
    print("=" * len(urlstring))
    sys.stdout.flush()  # make sure this gets displayed now.

    install_contrib();
    # If invoked by system, display logo for screenshots
    if not workspace:
        try:
            Popen(['xview', '-fit', '-fullscreen',
                  '/apps/jupyterexamples/current/images/jupyter.gif'])
        except:
            pass

    # having DISPLAY set breaks notebook terminals
    os.environ['DISPLAY'] = ""
    if args.debug:
        print("cmdlist:", cmdlist)
    notebookProcess = Popen(cmdlist)
#   print("%s notebookProcess = %d" % (time.ctime(),notebookProcess.pid))
    returnCode = notebookProcess.wait()
    notebookProcess = None
    print("\n\n%s Notebook server terminated. returnCode = %d\n" % (time.ctime(),returnCode))
    sys.stdout.flush()  # make sure this gets displayed now.

    uninstall_contrib()

def write_custom():
    import nanohubthemes
    currentTheme = nanohubthemes.get_current_theme()
    if currentTheme == 'default':
        nanohubthemes.reset_theme()
    else:
        nanohubthemes.install_theme(
            theme=currentTheme,
            monofont="opensans",
            monosize=12,
            nbfont="opensans",
            nbfontsize=12,
            tcfont="opensans",
            tcfontsize=12,
            dffontsize=12,
            outfontsize=12,
            mathfontsize=12,
            margins='auto',
            cellwidth='100%',
            lineheight=170,
            cursorwidth=2,
            cursorcolor='default',
            altprompt=False,
            altmd=False,
            altout=False,
            hideprompt=False,
            vimext=False,
            toolbar=True,
            nbname=True,
            kernellogo=False,
            dfonts=False,
            keepcustom=True
        )

def cleanup():
    # this can break nglview
    ndir = os.path.expanduser("~/.local/share/jupyter/nbextensions/nglview-js-widgets")
    if os.path.isdir(ndir):
        call(['rm', '-rf', ndir])


def main():
    notebookProcess = None
    if os.getuid() == 0:
        print("Do not run this as root.", file=sys.stderr)
        sys.exit(1)

    parser = parse_cmd_line()
    args = parser.parse_args()
    if args.help:
        parser.print_usage()
        sys.exit(0)

    write_custom()
    cleanup()
    run_notebook(args)

