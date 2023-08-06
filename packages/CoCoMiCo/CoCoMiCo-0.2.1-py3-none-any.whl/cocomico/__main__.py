import argparse
from cocomico.pipeline import benchmark_mode , run_mode
from cocomico.utils import is_valid_dir , is_valid_file, check_valid_dir
import os
import time
import pkg_resources
import sys

VERSION = pkg_resources.get_distribution("cocomico").version
LICENSE = """ Copyright (C) 2022 Maxime Lecomte - David Sherman - Clémence Frioux - Inria BSO - Pleiade
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>\n.
"""
REQUIRES = """
Requires Clingo and clyngor package: "pip install clyngor clyngor-with-clingo"
"""

def main():
    """Run programm.
    """

    
    parser_general=argparse.ArgumentParser()

    ############# CREATE COMMUNITY DATA ##########
    config_generate_file_path=argparse.ArgumentParser(add_help=False)
    config_generate_file_path.add_argument("-config_file", "--config_file", help='path of the config file')


    ############## community_benchmark ###############
    com_path_bench=argparse.ArgumentParser(add_help=False)
    com_path_bench.add_argument("-json_com", "--json_com", "-j",help='path of list of json files or a folder. each json representes a set of community. path1 path2 path3')
    
    seed_path_bench=argparse.ArgumentParser(add_help=False)
    seed_path_bench.add_argument("-seed_path", "--seed_path", "-s",help='path of seed file')
    
    sbml_path=argparse.ArgumentParser(add_help=False)
    sbml_path.add_argument('-sbml_path',"--sbml_path","-i",help='folder path to find sbml model')

    output = argparse.ArgumentParser(add_help=False)
    output.add_argument('-output',"--output", "-o",help='output path')

    ############## run ###############
    dir_path=argparse.ArgumentParser(add_help=False)
    dir_path.add_argument("-folder_path", "--folder_path", "-i",help='Directory path of a community composed of sbml or xml files.')

    seed_path_samples=argparse.ArgumentParser(add_help=False)
    seed_path_samples.add_argument("-seed_path", "--seed_path","-s",help='path of seed file')
    
    
    ######################################### subparser parser #######################################
    parser = parser_general.add_subparsers(title='command',description='valid subcommands:',dest="cmd")
 

    parser_toy=parser.add_parser("toys",help="simulation on toy example",parents=[output])
    parser_samples=parser.add_parser("run",help="Simulates community from folder",parents=[dir_path,seed_path_samples,output])
    parser_bench=parser.add_parser("benchmark",help="Simulates communities from json file",parents=[com_path_bench,seed_path_bench,sbml_path,output])

    # Error gestion 1 : if one or more arguments are wrong print help
    # ex: cocomico
    try:
        parser_general.parse_args()
    except:
        parser_general.print_help()
        print("ERROR: one or more arguments are missing or badly written")
        sys.exit(1)
    

    # Error gestion 2 : If zero argument print the help.
    # ex : cocomico
    if len(sys.argv) == 1:
        parser_general.print_help()
        print("ERROR: Arguments are missing")
        sys.exit(1)
    
    
    # Error gestion 3 : If zero argument print the help.
    # ex : cocomico run
    if len(sys.argv) == 2:
        parser_general.print_help()
        print("ERROR:  Arguments are missing")
        sys.exit(1)



    ##### Test conformity : existence of the output file + validity of input files
    
    args = parser_general.parse_args()
    # Test writing in out_directory if a subcommand is given else print version and help
    if args.cmd:
        if not is_valid_dir(args.output):
            print("ERROR: Impossible to access/create output directory")
            sys.exit(1)
    
    # Test input paths are valids:
    if "seed_path" in args and args.seed_path is not None:
        if not is_valid_file(args.seed_path):
            print("ERROR: " ,args.seed_path + " is not a correct filepath")
            sys.exit(1)

    if "json_com" in args and args.json_com is not None:
        if not is_valid_file(args.json_com):
            print("ERROR: " ,args.json_com + " is not a correct filepath")
            sys.exit(1)

    if "sbml_path" in args and args.sbml_path is not None:
        if not check_valid_dir(args.sbml_path):
            print("ERROR: " ,args.sbml_path + " is not a correct directory path")
            sys.exit(1)

    if "folder_path" in args and args.folder_path is not None:
        if not check_valid_dir(args.folder_path):
            print("ERROR: " ,args.folder_path + " is not a correct directory path")
            sys.exit(1)
    

    if args.cmd == 'toys':
        package_path = os.path.dirname(os.path.realpath(__file__))

        workflow_data_path = os.path.join(package_path, 'toys')
        print("Launching workflow on test data")
        models_benchmarks=os.path.join(workflow_data_path,'communities.json')
        seed_file=os.path.join(workflow_data_path,'seeds.sbml')
        sbml_paths_benchmarks=os.path.join(workflow_data_path,'sbml/')
        output=args.output
        benchmark_mode(models_benchmarks,seed_file,sbml_paths_benchmarks,output)


    elif args.cmd == 'run':
        models=args.folder_path
        seed_file=args.seed_path
        output=args.output
        start = time.time()
        run_mode(models,seed_file,output)
        td = round(time.time() - start,3)
        m, s = divmod(td, 60)
        h, m = divmod(m, 60)
        if h == 0.0 and m == 0.0:
            print('runs done in ',s,'s')
        elif h == 0.0 and m != 0.0:
            print('runs done in ',m,'m ',s,'s')
        else:
            print('runs done in ',h,'h ',m,'m ',s,'s')

    
    elif args.cmd == 'benchmark':
        models=args.json_com
        seed_file=args.seed_path
        sbml_path=args.sbml_path
        output=args.output
        global_start_time = time.time()
        benchmark_mode(models,seed_file,sbml_path, output)
        td = round(time.time() - global_start_time,3)
        m, s = divmod(td, 60)
        h, m = divmod(m, 60)
        if h == 0.0 and m == 0.0:
            print('runs done in ',s,'s')
        elif h == 0.0 and m != 0.0:
            print('runs done in ',m,'m ',s,'s')
        else:
            print('runs done in ',h,'h ',m,'m ',s,'s')