from cocomico import  score, utils
import json
import clyngor
import datetime

from clyngor.as_pyasp import TermSet
import os
import time
import shutil

scope_info={}
root = os.path.dirname(__file__)
score_prg = os.path.join(*[root, 'encodings', 'score.lp'])

def get_vocab(instance_lp):
    """From metabolic network represented as a set of facts, this function computes 
    descriptive vocabulary.

    Args:
        instance_lp (Instance): Metabolic network as a list of facts

    Returns:
        dict : descriptive vocabulary
    """    
    ## lp program and instance file for clingo
    prg = [score_prg, instance_lp]
    options = ''
    best_model = None
    models = clyngor.solve(prg, options=options) 
    for model in models.discard_quotes.by_arity:
        best_model = model
        
    ## parse clingo solution
    dico_general=utils.parse_frozenset(best_model,scope_info)
    return dico_general

def write_lp(list_draft,seed_sbml,path_bench='',i=''):
    """ Write list of SBML files in Instance lp

    Args:
        list_draft (list): List of SBML files
        seed_sbml (SBML): Nutrient in SBML file
        path_bench (str, optional): Output  Defaults to ''.
        i (str, optional): index for label output file  Defaults to ''.
    """    
    all_atoms = set()
    lpfact = TermSet()
    utils.workAround_score(list_draft,seed_sbml,all_atoms,lpfact,path_bench,i=i)
        
def to_json_benchmarks(dico_general,output):
    """Save descriptive vocabulary in json file

    Args:
        dico_general (dict): descriptive vocabulary
        output (str): output path
    """    
    with open(output+'.json','w+') as outputfile:
        json.dump(dico_general,outputfile,indent=4)

def generate_lp_file(path,seed_file,list_files,path_to_write='',i=''):
    """ Preparing SBML data for writting lp file
Args:
    path (str): path of sbml files
    seed_file (SBML): nutrient as SBML file
    list_files (list): List of SBML models
    path_to_search (str, optional): Path of community json file. Defaults to ''.
    path_to_write (str, optional): Output. Defaults to ''.
    i (int, optional): Index for label output file. Defaults to 0.
    data (str, optional): Data name. Defaults to ''.
"""


    toy_list=[path+'/'+sbml for sbml in list_files if ".json" not in sbml]
    write_lp(toy_list,seed_file,path_bench=path_to_write,i=i)
           


def run_mode(models,seed,output):
    """ Runs mode : It enables the characterization 
    from a community folder containing SBML/SML files.

    Args:
        models (str): Path of the community directory
        seed (str): Path the the seed file
        output (str): Path of the output file
    """    
    ## build json community file
    list_sbml = [files for _,_,files in os.walk(models)][0]
    name = models.split('/')[-2]
    dico={name: list_sbml}

    with open(models+'/'+name+'.json', 'w') as fp:
        json.dump(dico, fp,indent=4)
        
    ## apply benchmarks
    benchmark_mode(models+'/'+name+'.json',seed,models,output)

def benchmark_mode(models,seed_file,sbml_path,output):
    
    """_summary_

    Args:
    models (_type_): _description_
    seed_file (_type_): _description_
    data (_type_): _description_
    string (_type_): _description_
    sbml_path (_type_): _description_
    """    


    path_to_write_lp=output+"/instance_community/"
    path_to_write_vocab=output+"/community_description/"
    path_to_write_metrics=output+"/community_scores/"

    if not os.path.isdir(path_to_write_lp):
        os.mkdir(path_to_write_lp)

    if not os.path.isdir(path_to_write_vocab):
        os.mkdir(path_to_write_vocab)

    if not os.path.isdir(path_to_write_metrics):
        os.mkdir(path_to_write_metrics)
        
        
    with open(models) as json_file:
        data_communities = json.load(json_file)


    for idx,com in enumerate(data_communities):

        writting_start_time=time.time()
        generate_lp_file(sbml_path,seed_file,data_communities[com],path_to_write=path_to_write_lp,i=str(idx))

        td = round(time.time()-writting_start_time,3) 
        m, s = divmod(td, 60)
        h, m = divmod(m, 60)
        if h == 0.0 and m == 0.0:
            print('lp file for community',com,'(', s,'s)',)
        elif h == 0.0 and m != 0.0:
            print('lp file for community',com,'(',m,'m ',s,'s)')
        else:
            print('lp filefor community',com,'(',h,'h ',m,'m ',s,'s)')


        vocab_start_time=time.time()
        instance_lp=path_to_write_lp+'draft'+str(idx)+'.lp'
        dico_general=get_vocab(instance_lp)
        to_json_benchmarks(dico_general,path_to_write_vocab+'vocab_'+com)
            
        td = round(time.time()-vocab_start_time,3)
        m, s = divmod(td, 60)
        h, m = divmod(m, 60)
        
        if h == 0.0 and m == 0.0:
            print('vocab file for community',com,'(' , s,'s)',)
        elif h == 0.0 and m != 0.0:
            print('vocab file for community',com,'(', m,'m ',s,'s)')
        else:
            print('vocab filefor community',com,'(', h,'h ',m,'m ',s,'s)')
        
        
        utils.write_metrics(path_to_write_vocab,path_to_write_metrics,'_'+com)
    score.get_all_metrics(output)

    #removing directory
    shutil.rmtree(path_to_write_lp)

