import unittest
from contact_hysteresis_lab import run

def check(samples,**kw):return run(dict(release_threshold=2,engage_threshold=5,engage_duration=2,release_duration=1,samples=[{'time':t,'force':f} for t,f in samples],**kw))
class DomainTests(unittest.TestCase):
 def test_short_bounce_cancelled(self):self.assertEqual(check([(0,0),(1,6),(2,0)],until=5)['events'],[])
 def test_hold_confirmed_between_sparse_samples(self):
  r=check([(0,6),(5,0)],until=7);self.assertEqual(r['events'],[{'time':2,'contact':True},{'time':6,'contact':False}])
 def test_middle_band_retains_contact(self):
  r=check([(0,6),(3,3)],until=10);self.assertTrue(r['contact']);self.assertEqual(len(r['events']),1)
 def test_pending_disclosed(self):self.assertEqual(check([(0,6)])['pending'],{'due':2,'contact':True})
 def test_until_processes_final_hold(self):self.assertTrue(check([(0,6)],until=2)['contact'])
 def test_zero_duration_immediate(self):
  r=run(dict(release_threshold=2,engage_threshold=5,samples=[{'time':0,'force':6},{'time':1,'force':0}]));self.assertEqual(len(r['events']),2)
