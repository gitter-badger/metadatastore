# __author__ = 'arkilic'
import time
import datetime

from metadataStore.dataapi.metadataTools import *
from metadataStore.database.databaseTables import *
from metadataStore.database.databaseTables import BeamlineConfig, Header


# header = Header(_id=140, owner='arkilic', start_time=datetime.datetime.utcnow(),
#                 update_time=datetime.datetime.utcnow(), beamline_id='xyz')
#
# start = time.time()
# header = save_header(run_id=130, run_owner='arkilic', start_time=datetime.datetime.utcnow(),
#                      update_time=datetime.datetime.utcnow(), beamline_id='xyz')
# end = time.time()
# print 'It takes ' + str((end-start)*1000) + ' milliseconds'
#
#
#
header = save_header(run_id=237, run_owner='arkilic', start_time=datetime.datetime.utcnow(),
                     update_time=datetime.datetime.utcnow(), beamline_id='xyzaag')
#
#
# BeamlineConfig(_id=219, headers=[header]).save()
#
# bcfg = save_beamline_config(header_id=130, beamline_cfg_id=7)
#
#
# # bcfg = save_beamline_config()
#
# print Header.objects(owner__contains='ark')
# print BeamlineConfig.objects(author__owner='arkilic')
#
#
# print Event.objects(headers=1903)


# crsr1 = find(beamline_id="xyzaag")
# for i in xrange(crsr1.count()):
#     print crsr1.__getitem__(i)
# #
# print datetime.datetime.now()
# # #
# # crsr2 = find(header_id=[237, 130, 137], owner='ark*')
# # for i in xrange(crsr2.count()):
# #     print crsr2.__getitem__(i)
# #
#

# crsr3 = find(header_id={'start': 130, 'end': 137})
# for i in xrange(crsr3.count()):
#     print crsr3.__getitem__(i)

#
header = save_header(run_id=437, run_owner='arkilic', start_time=datetime.datetime(2012, 4, 10, 18, 34, 23, 574796),
                     update_time=datetime.datetime.utcnow(), beamline_id='xyzaag')


#
crsr4 = find(start_time=datetime.datetime(2010, 5, 17))
for i in xrange(crsr4.count()):
    print crsr4.__getitem__(i)




# db = Header._get_db()
# crsr3 = db['header'].find({'start_time': {'$lt': datetime.datetime(2040, 12, 17, 1, 1),
#                                           '$gte': datetime.datetime(2004, 1, 17, 0, 0)}})
# for i in xrange(crsr3.count()):
#     print crsr3.__getitem__(i)
