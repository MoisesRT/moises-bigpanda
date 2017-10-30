#! /usr/bin/python2.7

import argparse
import os

APPS = ['img-panda', 'smart-panda']

# Initialize the argparser
def create_parser():
    parser = argparse.ArgumentParser(
        description='The script that you should use in order to deploy panda-service or big-panda')
    parser.add_argument('-a', '--app', nargs='+', choices=APPS + ['ALL'], required=True,
                        help='Which service will be deployed'
                             '(multiple choice is available by spacing)')
    parser.add_argument('-i', '--inventory', required=False,
                        help='<OPTIONAL> The path of the Ansible Inventory will be used')
    parser.add_argument('-k', '--key', required=False, help="<OPTIONAL> Which key will be used in order to SSH")
    parser.add_argument('-u', '--user', required=False, help="<OPTIONAL> Which user will be used in order to SSH")
    return parser


# Create the ansible command
def command_build():
    PLAYBOOK_NAME = 'base.yml'
    # If the user chooses all it will add all the apps and if not it will be the one that he choose
    required_app = APPS if 'ALL' in args.app else args.app
    cmd = 'ansible-playbook -e \'{"required_services": %s}\'' % required_app
    if args.inventory is not None:
        cmd += ' -i %s' % args.inventory
    if args.key is not None:
        cmd += ' --private-key=%s' % args.key
    if args.user is not None:
        cmd += ' -u %s' % args.user
    cmd += ' %s' % PLAYBOOK_NAME
    return cmd


parser = create_parser()
args = parser.parse_args()
# Runs the Ansible command in a simple way
os.system(command_build())
