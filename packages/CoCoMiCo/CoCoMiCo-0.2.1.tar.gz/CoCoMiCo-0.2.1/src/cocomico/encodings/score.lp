%%%%% scope %%%%%%%%
scope(M) :- seed(M).
scope(M) :- bacteria(B), product(M,R,B), reaction(R,B), scope(M2) : reactant(M2,R,B).

%%%%% all putative metabolites consumed  
cscope(M,B) :- scope(M), reactant(M,R,B),isActivated(R).

%%%%%% Reaction is activated
isActivated(R) :- reaction(R,_), scope(M2) : reactant(M2,R,_).

%%%%%% all putative metabolites produced  
pscope(M,B,R) :- isActivated(R), scope(M), product(M,R,B).

%%%%%% putative exchanged metabolite : cooperation
escope(M,T,S) :- pscope(M,S,R), reactant(M,_,T), not indiv_producible(T,M,_),S!=T. %% S is source organism, T is target organism

%%%%%% scope reactions %%%%%
scope_reaction(R,B) :- reaction(R,B).

%%%%%% Total reactions activated 
% tot_reaction_activated(R,B) :- scope_reaction(R,B), isActivated(R).

%%%%%% pscope in pure culture
iscope(M,D) :- seed(M), target_species(D).
iscope(M,D) :- target_species(D), product(M,R,D), reaction(R,D), iscope(M2,D) : reactant(M2,R,D). 
iactiv(R,D) :- target_species(D), reaction(R,D), iscope(M2,D) : reactant(M2,R,D).
indiv_producible(D,M,R) :- product(M, R, D), iactiv(R,D).

%%%%% pi 
commensalism(S) :- S = #count{X:escope(X,_,_)}.

%%%%% putative limiting substrate
limiting_subtrate(M,B) :- seed(M), reaction(R,B), reactant(M,R,B).
limiting_subtrate(M,B) :- escope(M,B,_).

#show scope/1.
#show bacteria/1.
#show seed/1.
#show scope_reaction/2.
#show indiv_producible/3.
% #show tot_reaction_activated/2.
#show pscope/3.
#show escope/3.
#show commensalism/1.
#show limiting_subtrate/2.
#show cscope/2.
