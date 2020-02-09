# !python

# Pull, build our github repository and start NodeJS server
# we use library Gitpython 
# https://gitpython.readthedocs.io/en/stable/intro.html
# for installation in the system need to write in the terminal: pip install gitpython

# import the os module
import os
import sys
from time import gmtime, strftime
from git import Repo,  InvalidGitRepositoryError

#log system
import logging
logging.basicConfig(filename='app.log')

# create logger
logger = logging.getLogger('script')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

#start script
logger.info('----------------')
logger.info('Script started')
logger.info('----------------')


# check current repository for github prefs
currentpath = os.getcwd();
try:
    repo = Repo(currentpath)
except InvalidGitRepositoryError:
    logger.error('Invalid git repopository')
    #sys.exit()


#check to pull new code from github
try:    
    gitpull = repo.git.pull()    
    logger.info('git pull was successed')        
except :
    logger.error('Error with git pull operation')
finally:
    result = gitpull.find('Already up to date.')    
    if ( result >= 0 ) : 
        logger.info('Repository is valid and up to date') 
    else:
        logger.error('There are the problem with pulling new code to our repository')         
        #sys.exit()

# build source
try: 
    newbuild = os.system('npm run build')    
    logger.info('Build was made successful')
except:
    logger.error('There was a problem to create new build')

#start NodeJS server with nohup
logger.info('NodeJS server starts now with new build')
startserver = os.system('node server.js > app.log &')        
 