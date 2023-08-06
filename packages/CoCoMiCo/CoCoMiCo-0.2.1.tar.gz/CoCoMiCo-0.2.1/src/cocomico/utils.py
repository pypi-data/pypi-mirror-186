from clyngor.as_pyasp import TermSet, Atom
import time
import xml.etree.ElementTree as etree
import os
from cocomico import score



def write_metrics(path_to_write_vocab,path_to_write_metrics ,key):
    """   
    This function aims to write the metric files

    Args:
        path_to_write_vocab (str): Path of the vocabulary file
        path_to_write_metrics (str): Path of the metrics file
        key (str): Pattern to differenciate communities. Based on filename.

    """    

    if not os.path.isdir(path_to_write_metrics):
        os.mkdir(path_to_write_metrics)
        
    vocab_file= path_to_write_vocab+'vocab'+str(key)+'.json'
    metrics_file= path_to_write_metrics+'metrics'+str(key)+'.json'

    met_occ_com,met_occ,escope_org,redondante_limiting,rxn_occ,rxn_occ_com,bacteria=score.parsing_data(vocab_file)
    
    start=time.time()
    delta,delta_metric=score.compute_delta_score(met_occ_com,met_occ)
    rho,rho_metric=score.compute_rho_score(rxn_occ,rxn_occ_com)
    pi,pi_metric=score.compute_cooperation_score(escope_org)
    comp,comp_metric=score.compute_competition_score(redondante_limiting,len(bacteria))
    
    score.write_score_json_file(delta,rho,pi,delta_metric,rho_metric,pi_metric,metrics_file,comp,comp_metric,bacteria)
    td = round(time.time()-start,3)
    m, s = divmod(td, 60)
    h, m = divmod(m, 60)
    if h == 0.0 and m == 0.0:
            print('score file for community'+str(key),'(' , s,'s)',)
    elif h == 0.0 and m != 0.0:
        print('score file for community'+str(key),'(', m,'m ',s,'s)')
    else:
        print('score filefor community'+str(key),'(', h,'h ',m,'m ',s,'s)')

    print("done for community",key+'\n')

def get_model(sbml):
    """Get the model of a SBML
    Args:
        sbml (str): SBML file
    Returns:
        xml.etree.ElementTree.Element: SBML model
    """
    model_element = None
    model_id = None
    for e in sbml:
        model_id = e.attrib.get("id")
        if e.tag[0] == "{":
            uri, tag = e.tag[1:].split("}")
        else:
            tag = e.tag
        if tag == "model":
            model_element = e
            break
        
    return model_element,model_id

def get_listOfSpecies(model):
    """Get list of Species of a SBML model
    
    Args:
        model (xml.etree.ElementTree.Element): SBML model
    
    Returns:
        xml.etree.ElementTree.Element: list of species
    """
    listOfSpecies = None
    for e in model:
        if e.tag[0] == "{":
            uri, tag = e.tag[1:].split("}")
        else:
            tag = e.tag
        if tag == "listOfSpecies":
            listOfSpecies = e
            break
    return listOfSpecies

def get_listOfReactions(model):
    """Get list of reactions of a SBML model
    
    Args:
        model (xml.etree.ElementTree.Element): SBML model
    
    Returns:
        xml.etree.ElementTree.Element: list of reactions
    """
    listOfReactions = None
    for e in model:
        if e.tag[0] == "{":
            uri, tag = e.tag[1:].split("}")
        else:
            tag = e.tag
        if tag == "listOfReactions":
            listOfReactions = e
            break
    return listOfReactions


def get_listOfReactants(reaction):
    """Get list of reactants of a reaction
    
    Args:
        reaction (xml.etree.ElementTree.Element): reaction
    
    Returns:
        xml.etree.ElementTree.Element: list of reactants
    """
    listOfReactants = None
    for e in reaction:
        if e.tag[0] == "{":
            uri, tag = e.tag[1:].split("}")
        else:
            tag = e.tag
        if tag == "listOfReactants":
            listOfReactants = e
            break
    return listOfReactants

def get_listOfProducts(reaction):
    """Get list of porducts of a reaction
    
    Args:
        reaction (xml.etree.ElementTree.Element): reaction
    
    Returns:
        xml.etree.ElementTree.Element: list of products
    """
    listOfProducts = None
    for e in reaction:
        if e.tag[0] == "{":
            uri, tag = e.tag[1:].split("}")
        else:
            tag = e.tag
        if tag == "listOfProducts":
            listOfProducts = e
            break
    return listOfProducts

def read_MN(filename,all_atoms,lpfact):
    """ Convert SBML to LP file

    Args:
        filename (str): _description_
        all_atoms (set): _description_
        lpfact (termSet): _description_

    Returns:
        _type_: _description_
    """    
    tree = etree.parse(filename)
    sbml = tree.getroot()
    model,name = get_model(sbml)

    listofspecies = get_listOfSpecies(model)
    
    if 'seed' in filename:
        for e in listofspecies:
            if e.tag[0] == "{":
                uri, tag = e.tag[1:].split("}")
            else: 
                tag = e.tag
            if tag == "species":
                speciesId = e.attrib.get("id").replace('"','')
                all_atoms.add(Atom('seed', ["\""+speciesId+"\""]))
    
    else:
        if name == None:
            tmp_name=filename.split('/')
            name=tmp_name[-1].replace('.sbml','_'+tmp_name[1])
        all_atoms.add(Atom('target_species', ["\""+name+"\""]))
        all_atoms.add(Atom('bacteria', ["\""+name+"\""]))
        listOfReactions = get_listOfReactions(model)

        for e in listOfReactions:
            if e.tag[0] == "{":
                uri, tag = e.tag[1:].split("}")
            else: tag = e.tag
            if tag == "reaction":
                reactionId = e.attrib.get("id")
                all_atoms.add(Atom('reaction', ["\""+reactionId+"\"", "\""+name+"\""])) 
                if(e.attrib.get("reversible")=="true"):
                    all_atoms.add(Atom('reaction', ["\""+reactionId+"rev\"","\""+name+"\""]))

                listOfReactants = get_listOfReactants(e)
                if listOfReactants != None:
                    for r in listOfReactants:
                        if(e.attrib.get("reversible")=="true"):
                            all_atoms.add(Atom('product', ["\""+r.attrib.get("species").replace('"','')+"\"", "\""+reactionId+"rev\"", "\""+name+"\""])) #,"\""+name+"\""
                        all_atoms.add(Atom('reactant', ["\""+r.attrib.get("species").replace('"','')+"\"", "\""+reactionId+"\"", "\""+name+"\""])) #,"\""+name+"\""


                listOfProducts = get_listOfProducts(e)
                if listOfProducts != None:
                    for p in listOfProducts:
                        if(e.attrib.get("reversible")=="true"):
                            all_atoms.add(Atom('reactant', ["\""+p.attrib.get("species").replace('"','')+"\"", "\""+reactionId+"rev\"", "\""+name+"\""])) #,"\""+name+"\""
                        all_atoms.add(Atom('product', ["\""+p.attrib.get("species").replace('"','')+"\"", "\""+reactionId+"\"", "\""+name+"\""])) #,"\""+name+"\""
        
        for e in listofspecies:
            if e.tag[0] == "{":
                uri, tag = e.tag[1:].split("}")
            else: tag = e.tag
            if tag == "species":
                speciesId = e.attrib.get("id").replace('"','')
                all_atoms.add(Atom('species', ["\""+speciesId+"\"", "\""+name+"\""]))#,"\""+e.attrib.get("compartment")+"\""]))
                

    lpfacts = TermSet(all_atoms)
    lpfacts = all_atoms

    return lpfacts

    
def to_file(termset='',output=''):
    """ convert the termSet into file.

    Args:
        termset (str, optional): _description_. Defaults to ''.
        output (str, optional): _description_. Defaults to ''.

    Returns:
        File : _description_
    """    
    with open(output,'w+') as f:
        for element in termset:
            f.write(str(element) + '.\n')
    return output


def parse_frozenset(best_model, scope_info):
    """ Parsing function from the frozen set output of clingo

    Args:
        best_model (frozenSet): Descriptive vocabular
        scope_info (dict): descriptive vocabular

    Returns:
        dict : descriptive vocabular
    """    
    scope_info={}
    for frozenset_key in best_model:
        if isinstance(frozenset_key,str) and '/2' in frozenset_key:
            frozenset_key=frozenset_key[:-2]
            scope_info[frozenset_key]={}
            for element in best_model[frozenset_key]:
                if element[0] not in scope_info[frozenset_key]:
                    scope_info[frozenset_key][element[0]]=[element[1]]
                else:
                    scope_info[frozenset_key][element[0]].append(element[1])
                    
        if isinstance(frozenset_key,str) and 'escope/3' in frozenset_key:
            frozenset_key=frozenset_key[:-2]
            scope_info[frozenset_key]={}
            for element in best_model[frozenset_key]:
                if element[0] not in scope_info[frozenset_key]:
                    scope_info[frozenset_key][element[0]]={}
                
                if element[2] not in scope_info[frozenset_key][element[0]]:
                    scope_info[frozenset_key][element[0]][element[2]]={}
                
                if 'to' not in scope_info[frozenset_key][element[0]][element[2]]:
                    scope_info[frozenset_key][element[0]][element[2]]['to']=[]
                    
                scope_info[frozenset_key][element[0]][element[2]]['to'].append(element[1])
                    
    
                    
        if isinstance(frozenset_key,str) and '/3' in frozenset_key and 'escope' not in frozenset_key:
            frozenset_key=frozenset_key[:-2]
            scope_info[frozenset_key]={}
            for element in best_model[frozenset_key]:
                if element[0] not in scope_info[frozenset_key]:
                    scope_info[frozenset_key][element[0]]={}
                if element[1] not in scope_info[frozenset_key][element[0]]:
                    scope_info[frozenset_key][element[0]][element[1]]=[element[2]]
                else:
                    scope_info[frozenset_key][element[0]][element[1]].append(element[2])
            
            
        if isinstance(frozenset_key,str) and '/1' in frozenset_key:
            frozenset_key=frozenset_key[:-2]
            scope_info[frozenset_key]=[]
            for element in best_model[frozenset_key]:
                scope_info[frozenset_key].append(element[0])

    return scope_info

        
root = os.path.dirname(__file__)
score_prg = os.path.join(*[root, 'encodings', 'score.lp'])


def workAround_score(list_draft,seeds_sbml,all_atoms,lpfact,path,i=''):
    """ Compute the scope of a metabolic network draft in sbml format from a seed file

    Args:
        list_draft (List): SBML file which contains the metabolic network
        seeds_sbml (SBML): SBML file which contains seeds
        all_atoms (set): description of fact
        lpfact (TermSet):
        path (str): Output
        i (str, optional): _description_. Defaults to ''.
    """    

    draft = []
    seeds=read_MN(seeds_sbml,all_atoms,lpfact)
    for draft_sbml in list_draft:
        draft.append(read_MN(draft_sbml,all_atoms,lpfact))
    draft_f = to_file(termset=draft[-1],output=path+'draft'+i+'.lp')


def is_valid_dir(dirpath):
    """Return True if directory exists or can be created (then create it)
    
    Args:
        dirpath (str): path of directory
    Returns:
        bool: True if dir exists, False otherwise
    """
    if not os.path.isdir(dirpath):
        try:
            os.makedirs(dirpath)
            return True
        except OSError:
            return False
    else:
        return True


def check_valid_dir(dirpath):
    """Return True if directory exists or not
    
    Args:
        dirpath (str): path of directory
    Returns:
        bool: True if dir exists, False otherwise
    """
    if os.path.isdir(dirpath) == True:
        return True
    else:
        return False


def is_valid_file(filepath):
    """Return True if filepath exists
    Args:
        filepath (str): path to file
    Returns:
        bool: True if path exists, False otherwise
    """
    try:
        open(filepath, 'r').close()
        return True
    except OSError:
        return False
