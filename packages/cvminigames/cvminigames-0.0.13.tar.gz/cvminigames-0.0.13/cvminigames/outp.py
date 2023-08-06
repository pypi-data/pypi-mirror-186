# Export your notebooks to a python script.

def main():
    """
    For Testing
    """
    print("Hello.")

import re
import marko
import json
import codecs

def cv_cli_nbs2html(): 
    import sys
    pathto, pages, saveto = sys.argv[1], sys.argv[2], sys.argv[3]
    generate_sitemap([pathto+page for page in pages.split(',')], saveto)

def generate_sitemap(pages, saveto = "../src/posts/"):
    """ 
    0. Publish a set of pages and create a table of contents json file for em.
    Checks or creates sitemap.json and uses it to generate and update pages from the cmd line.
    """
    links = []
    try:
        with open(saveto+"sitemap.json", "r") as json_file: 
            pages += [obj['filename'] for obj in json.load(json_file) if obj['filename'] not in pages]
            json_file.close()
    except: ''

    for page in pages: 
        r = ipynb_publish(page, saveto) 
        if( r['meta']['hide'] == 'false'):
            delist = ['badges', 'keywords', 'comments', 'hide', 'image', 'toc', 'title']
            links.append({key: val for key, val in r['meta'].items() if key not in delist})

    try:
        with open(saveto+"sitemap.json", "w") as json_file:
            json_file.write(str(json.dumps(links)))
            json_file.close()
    except:
        with open(saveto+"sitemap.json", "w") as json_file:
            json_file.write("{}")

def ipynb_publish(fname='index', saveto="../src/posts/", type='json'): 
    '''
    1. Publish ipynb to json or html.
    '''
    if (type=='html'): raw = nb2html(fname); r=raw
    if (type=='json'): 
        raw = nb2json(fname);  
        fname = raw['meta']['filename'].lower().replace(' ', '_')
        r = str(json.dumps(raw))
    t = saveto+fname+"."+type
    f = open(t, "w") 
    f.write( r )
    f.close() 
    return raw

def nb2json(fname): 
    """ 
    1a. Must be in directory of ipynb you want to convert to html.
    """
    # sys.path.pop()
    # sys.path.append('workspaces/3Diot.github.io/ipynb')
    # from blog import core 
    # %cd ../ipynb 
    nb = json.loads( codecs.open(fname+'.ipynb', 'r').read() )
    meta = get_metadata(nb['cells'][0])
    outp = convertNb(nb['cells'][1:])
    # print(outp)
    # print(len(outp))
    p1 = [''.join(c) for c in outp]
    outp = ''.join( p1 ) 
    resp = ''.join( [''.join(c) for c in outp] )
    resp = replaceEmojis(resp)
    return {"meta":meta,"content":resp}

def get_metadata(data):
    """ 
    2. Get markdown (title, summary) and yaml from 1st cell in ipynb.
    """
    y = {}
    for x in data['source']: 
        # starts with #
        if(x[0] == '#'):
            y['title'] = x.replace('\n', '').replace('# ', '', 2)
        elif(x[0] == '>'):
            y['summary'] = x.replace('\n', '').replace('> ', '', 1)
        elif(x[0] == '-'):
            key = (x[x.index('- ')+2:x.index(': ')])
            val = (x[x.index(': ')+2:].replace('\n', ''))
            # print('key', key); print('value', val)            
            y[key] = val
    return y

def convertNb(cells): 
    """ 
    3. passes each cell to decision fn.
    """
    return [cleanCell(c) for c in cells]

def cleanCell(cell):
    """ 
    4. returns text or passes cell to 'code cell' processor
    """
    return marko.convert(' '.join(cell['source'])) if cell['cell_type'] == 'markdown' else processCode(cell)

def processCode(cell): 
    """ 
    5. Calls getFlags, processSource, processOutput 
    """
    x = []
    # source 
    if ( len(cell['source']) ):
        source = cell['source']
        flags = getFlags(source[0])
        # print('Flags: ', flags)

        source = processSource( ' '.join(source[1:]), flags )
        # print('Processed Source')
        x.append(source)
    # output
    if ( len(cell['outputs']) ):
        for o in cell['outputs']: x.append( processOutput(o, flags) )
        # print('Processed Output')
        #clear_output()
    return x

def getFlags(source):
    """ 
    6a. Detect and stripout and handle flags.
    """
    input_aug = ['#collapse_input_open', '#collapse_input', '#collapse_output_open', '#collapse_output',
                '#hide_input', '#hide_output', '#hide ', '%%capture', '%%javascript', '%%html']
    return [ x for x in input_aug if re.search(x, source) ]

def processSource (source, flags):
    """ 
    6b. Strip Flags from text, make details, hide all.
    """
    # print('processSource... ', source)
    for lbl in flags:
        # print('processSource... ', lbl)
        source = source.replace(lbl+'\r\n', "")
        source = source.replace(lbl+'\n', "") # Strip the Flag
        if (lbl == '#collapse_input_open'): source = makeDetails( source, True )
        if (lbl == '#collapse_input'): source = makeDetails( source, False )
        if (lbl == '#hide '): source = ''
        if (lbl == '#hide_input'): source = ''
        if (lbl == '%%javascript'): source = ''
        if (lbl == '%%html'): source = ''
        if (lbl == '%%capture'): source = ''
    return source

def processOutput(source, flags):
    """ 
    6c. Strip Flags from output, make details, hide all.
    """
    if(source['output_type']=='error'):  return ''
    if(source['output_type']=='stream'):
        if(source['name']=='stderr'): return ''
        source['data'] = {'text/html': source['text']} # This will have the stream process as text/html. 

    keys = source['data'].keys()
    if ( 'text/html' in keys ): source=source['data']['text/html']; source = ''.join( source )
    elif ( 'application/javascript' in keys ): source='<script>'+source['data']['application/javascript']+'</script>'
    elif ( 'image/png' in keys ): source= "<img src=\"data:image/png;base64," + source['data']['image/png'] + "\" alt='Image Alt Text'>"
    elif ( 'text/plain' in keys ): source = '' if re.search("<Figure", source['data']['text/plain']) else source['data']['text/plain'];

    for lbl in flags:
        source = source.replace(lbl+'\r\n', "")
        source = source.replace(lbl+'\n', "")
        if (lbl == '#collapse_output_open'): source = makeDetails( source, True )
        if (lbl == '#collapse_output'): source = makeDetails( source, False )
        if (lbl == '#hide_output'): source = ''
        if (lbl == '#hide '): source = ''

    return source
    #output_type == 'stream' ==> text
    #output_type == 'display_data' ==> data{'application/javascript' or 'text/html' or 'execute_result'}

def makeDetails( content, open ):
    """ 
    7. Called by processOutput and processSource.
    """
    return "<details "+('open' if open else '')+"> <summary>Click to toggle</summary> "+content+"</details>"

def replaceEmojis(text):
    """ 
    8. Convert emojis to html entities
    """
    text = text.replace('🙂', '&#1F642')
    text = text.replace('😳', '&#128563')
    text = text.replace('\u2003', '&#8195')
    text = text.replace('👷', '&#128119')
    text = text.replace('🧡', '&#129505')
    text = text.replace('💖', '&#128150')
    # Dec => Code => https://apps.timwhitlock.info/unicode/inspect/hex/1F633
    return text

def filterCells(cell):
    """
    2nd fn. returns text or passes cell to 'code cell' processor
    """
    return '' if cell['cell_type'] == 'markdown' else getCode(cell)

def getCode(cell):
    """
    3rd fn. passes each cell to decision fn.
    """
    # print(cell['source'], '\n')
    flags = [ x for x in ['#export '] if re.search(x, cell['source'][0]) ]
    x = ''.join(cell['source'][1:]) if len(flags)>=1 else ''
    return x

def nb2py(infile, outfile):
    """
    1st fn. passes each cell to decision fn.
    """
    links = []
    nb = json.loads( codecs.open(infile, 'r').read() )
    nb2 = [filterCells(c) for c in nb['cells']]
    while("" in nb2):
        nb2.remove("")
    outp = '\n\n'.join(nb2)
    f = open(outfile, "w") 
    f.write(outp)
    f.close()

def bump_version(path):
    with open(path+'__init__.py', 'r') as f:
        lines = f.readlines()
        f.close()
    for i, line in enumerate(lines): 
        if line.startswith('__version__'):
            version = re.findall(r'\d+\.\d+\.\d+', line)[0].split('.')
            if(version[2] != '99'):
                version[2] = str(int(version[2])+1)
            else:
                version[2] = '0'
                if(version[1] != '99'):
                    version[1] = str(int(version[1])+1)
                else:
                    version[1] = '0'
                    version[0] = str(int(version[0])+1)
            f = open(path+'__init__.py', "w")
            f.write('__version__ = "' +'.'.join(version) + '"')
            f.close()

def cv_cli_bump_version():
    import sys
    path = sys.argv[1]
    bump_version(path)

def cv_cli_nb2py(): 
    import sys
    infile, outfile = sys.argv[1], sys.argv[2]
    nb2py(infile, outfile)