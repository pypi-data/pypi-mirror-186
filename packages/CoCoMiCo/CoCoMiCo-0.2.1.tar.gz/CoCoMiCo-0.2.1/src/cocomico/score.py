import json
import os
import pandas as pd


def parsing_data(vocab_file):
    """_summary_
    This function allows to parse the descriptive vocabular of the community pre-generated with ASP. 
    usefull data for computing scores are well formated and divided into lists and dictionnaries.

    Args:
        vocab_file (json): descriptive vocabular of the community

    Returns:
        _list_,_dict_: appropriate format for computing score
    """
   
                
    f = open(vocab_file)
    data = json.load(f)
    f.close
    bacteria = data['bacteria']
    
    ################################## cooperation ############################## 
    ############## Individual 
    ## Metabolites
    iscope={bact:met for bact,met in data['indiv_producible'].items()}
    
    ## Reactions
    # rxn_occ = []
    
    reaction_activated_ind,reactions=[],[]
    abundance_idx,rxn_occ={},{}
        
    for bact,mets in data['indiv_producible'].items():
        for met,r in mets.items():
            reaction_activated_ind.append(r)
    reactions_formatted=[xs for s in reaction_activated_ind for xs in s]
    rxn_occ={rxn:reactions_formatted.count(rxn) for rxn in reactions_formatted}

    ############## Community  
    ## Metabolites
    # flat_list_met_com = []
    
    pscope={met:bact for met,bact in data['pscope'].items()}
    pscope_met_org=[str(x+' ')*len(y) for x,y in pscope.items()]
    pscope_commensalism=[i.split(' ') for i in pscope_met_org]
    flat_list = [item for sublist in pscope_commensalism for item in sublist]
    flat_list_met_com = [s for s in flat_list if s != '']

    ## Reactions
    # rxn_occ_com = []
    
    pscope_orgs={}
    
    for met,orgs in pscope.items():
        for b,bb in orgs.items():
            if b not in pscope_orgs:
                pscope_orgs[b]=[]
            pscope_orgs[b].append(bb)
            
        reaction_used_com=[reaction for met,orgs in pscope.items() for org,reaction in orgs.items()]  
        flat_list_com=[x for xs in reaction_used_com for x in xs] 
        rxn_occ_com={rxn:flat_list_com.count(rxn) for rxn in flat_list_com}
        

    
    ################################## competition ##############################  
    limiting_substrate_dict = data['limiting_subtrate']
    redondante_limiting=[str(x+' ')*len(y) for x,y in limiting_substrate_dict.items()]
    tmp_limiting=[i.split(' ') for i in redondante_limiting]
    redondante_limiting = [item for sublist in tmp_limiting for item in sublist if item != '']
    
    escope_org={}
    if 'escope' in data.keys(): # if cross-feeding between microbial community
        for met,org in data['escope'].items():
            escope_org[met] = {}
            for source in org.keys():
                if source not in escope_org[met]:
                    escope_org[met][source]=len(org[source]['to'])
    
    return flat_list_met_com,iscope,escope_org,redondante_limiting,rxn_occ,rxn_occ_com,bacteria

def compute_competition_score(list_with_occurence,bacteria):
    """ This function aims at calculating the competition score within a defined community.
        The exponential cost penalized species that can not give essential ressources for all bacteria in the community. 

    Args:
        list_with_occurence (_list_): List of all limiting substrates shared and consumed within the community.

    Returns:
        _tuple_: competition score and the metrics used for.
    """    
    met_count_ind={cpd:list_with_occurence.count(cpd) for cpd in list_with_occurence}
    competition=[]
    for cpd,val in met_count_ind.items():
        cpt=0  
        cpt+=val/bacteria
        competition.append(cpt)
    comp=sum(competition)
    comp_metrics = {'total number of limited subtrates':len(list_with_occurence)}
    return comp,comp_metrics

def compute_delta_score(list_with_occurence_com,dict_with_occurence_ind):
    """This function shows the added value in community of producible compounds

    Args:
        list_with_occurence_com (_list_): list of producible compounds in community
        dict_with_occurence_ind (_list_): union of producible compounds for each species in the community

    Returns:
        _int_,_dict_: intrinsic properties of the community 
    """   
    
    list_with_occurence_ind=[met for mets in dict_with_occurence_ind.values() for met in mets]
    
    delta=len(set(list_with_occurence_com))
    delta_metric={'added value community':len(set(list_with_occurence_com)) - len(set(list_with_occurence_ind)),
                  'all individual can produce': len(set(list_with_occurence_ind))}
    
    return delta,delta_metric

def compute_rho_score(rxn_occ,rxn_occ_com):
    """ Added value of the community on reactions 

    Args:
        rxn_occ (list): List of occuring activated reaction at the genome-scale
        rxn_occ_com (list): List of occuring activated reaction at the cmmunity-scale

    Returns:
        tuple: intrinsic properties of the community 
    """    
    list_with_occ=[(k+' ')*v for k,v in rxn_occ.items()]
    list_with_occ_ind=[i.split(' ') for i in list_with_occ]
    list_with_occ_ind=[item for sublist in list_with_occ_ind for item in sublist if item != '']

    list_with_occ=[(k+' ')*v for k,v in rxn_occ_com.items()]
    list_with_occ_com=[i.split(' ') for i in list_with_occ]
    list_with_occ_com=[item for sublist in list_with_occ_com for item in sublist if item != '']
    
    rho = len(list_with_occ_com)
    rho_metric = {'added value comunity':len(list_with_occ_com) - len(list_with_occ_ind)}
    
    return rho,rho_metric

def compute_cooperation_score(met_cons_cpt):
    """ Computes cooperation potential of the community

    Args:
        met_org_cpt (dict): producers and consumers associated to a metabolites during a creoss-feeding

    Returns:
        tuple: cooperation potential of the community and contribution of producers and consumers during the cross-feeding
    """    
    pi_cons,pi_prod=0,0
    
    for met,orgs in met_cons_cpt.items():
        number_cons = list(met_cons_cpt[met].values())
        for n in number_cons:
            for j in range (1,n+1,1):
                pi_cons+=2**(-(j-1))
                
        for i in range(1,len(orgs.keys())+1,1):
            pi_prod+= 2**(-(i-1))  
            
                    

    pi=pi_cons+pi_prod
    pi_metric={'number of exchanged metabolites':len(met_cons_cpt),
               'pi producers':pi_prod,
               'pi consumers':pi_cons}  
    
    return pi,pi_metric

def write_score_json_file(delta,rho,pi,delta_metric,rho_metric,pi_metric,output,comp2,comp2_metrics,bacteria):
    """This function saves scores et intrinsic properties in a json file.

    Args:
        delta (_int_): added value on metabolite production
        rho (_int_): added value on reaction production
        pi (_int_): cooperation score
        delta_metric (_dict_): variables used explaining the delta value
        rho_metric (_dict_): variables used explaining the rho value
        pi_metric (_dict_): variables used explaining the pi value
        output (_str_): path of the json file
        comp2 (_int_): competition score
        comp2_metrics (_dict_): variables used explaining the competition score
        bacteria (_list_): bacteria in bacterial community
    """    
    listObj={}
    with open(output,'w+') as json_file:
        listObj["metabolite production value (delta)"]=delta
        listObj["metabolite production value_metric"]= delta_metric
        listObj["cooP"]= pi
        listObj["cooP_metric"]= pi_metric
        listObj["reaction production(rho)"]= rho
        listObj["reaction production_metric"]= rho_metric
        listObj["comP"]=comp2
        listObj["comP_metric"]=comp2_metrics
        listObj["bacteria"]=bacteria
        
        json.dump(listObj, json_file, indent=4)
        
            
def get_all_metrics(output_folder):
    """Save cooperation and competition potentials and sub-scores in a tsv file.

    Args:
        output_folder (str): Output path
    """    
    delta,pi,rho,comp2,size,nb_exc,pi_prod,pi_cons=[],[],[],[],[],[],[],[]
    
    
    ## get metrics files in the metrics directory
    metrics_files=[output_folder+'/community_scores/'+f for _,_,files in os.walk(output_folder+'/community_scores/') for f in files]
    for json_m in metrics_files:
        with open(json_m) as json_file:
            data=json.load(json_file)
        delta.append(data['metabolite production value (delta)'])
        pi.append(data['cooP'])
        rho.append(data['reaction production(rho)'])
        comp2.append(data['comP'])
        nb_exc.append(data["cooP_metric"]["number of exchanged metabolites"])
        pi_prod.append(data["cooP_metric"]["pi producers"])
        pi_cons.append(data["cooP_metric"]["pi consumers"])
        size.append(len(data["bacteria"]))
        
    ## save metrics
    dico={"delta":delta,"cooP":pi,"rho":rho,"comP":comp2,"com_size":size,"nb_exc_cpd":nb_exc,"cooP_producers":pi_prod,"cooP_consumers":pi_cons}
    data_as_table = pd.DataFrame(data=dico)
    data_as_table.to_csv(output_folder+"/scores.tsv",sep="\t")

