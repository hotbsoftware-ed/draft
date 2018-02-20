import sys, unittest, src.QA.QaAdpqShell as QaAdpqShell, requests

## @package smoke test
#

'''
    ADPQ v1 - All end points.
    
    Purpose - Will test all end points for their status. 200 status 
              indicates that the end point is active and running 
              properly. 

    Test cases
        Test end point get agencies by extracting a status code.
        Test end point get tags by extracting a status code.
        Test end point get articles by extracting a status code.
        Test end point search articles by extracting a status code.
'''
class SmokeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass
        try:
            # Create shell class objects.
            cls.user = QaAdpqShell.QaADPQShell()
            cls.BaseUrl = QaAdpqShell.QaADPQShell.BaseURL
            assert(cls.user != None)
            assert(cls.BaseUrl != None)
        except:
            print("Unexpected error during setUp:", sys.exc_info()[0])
            raise

     
     
    ## Get the status of the get agencies end point.
    def test_GetAgenciesStatus(self):
        # Build the URL for this end point.
        url = self.BaseUrl + QaAdpqShell.QaADPQShell.GetAgencies
        
        # Assign the header parameters.
        headers = {
            'Content-Type' : 'application/json',
            'Cache-Control': 'no-cache'
        }
        
        # Assign the body parameters.
        body = {}
        
        # Make the call and return the save the results.
        response = requests.request('GET', url, json=body, 
                                    headers=headers, verify=False)
        
        # Ensure that the end point is live.
        self.assertEqual(response.status_code, 200, 
                         msg='test_GetAgenciesStatus assert#1 failed.')
         
         
         
    # Get the status of the get tags end point.
    def test_GetTagStatus(self):
        # Build the URL for this end point.
        url = self.BaseUrl + QaAdpqShell.QaADPQShell.GetTags
         
        # Assign the header parameters.
        headers = {
            'Content-Type' : 'application/json',
            'Cache-Control': 'no-cache'
        }
         
        # Assign the body parameters.
        body = {}
         
        # Make the call and return the save the results.
        response = requests.request('GET', url, json=body, 
                                    headers=headers, verify=False)
         
        # Ensure that the end point is live.
        self.assertEqual(response.status_code, 200, 
                         msg='test_GetTagStatus assert#1 failed.')
         
         
         
    # Get the status of the get articles end point.
    def test_GetArticleStatus(self):
        # Build the URL for this end point.
        url = self.BaseUrl + QaAdpqShell.QaADPQShell.GetArticles
         
        # Assign the header parameters.
        headers = {
            'Content-Type' : 'application/json',
            'Cache-Control': 'no-cache'
        }
         
        # Assign the body parameters.
        body = {}
         
        # Make the call and return the save the results.
        response = requests.request('GET', url, json=body, 
                                    headers=headers, verify=False)
         
        # Ensure that the end point is live.
        self.assertEqual(response.status_code, 200, 
                         msg='test_GetArticleStatus assert#1 failed.')
          
          
          
    # Get the status of the search articles end point.
    def test_GetSearchArticleStatus(self):
        # Build the URL for this end point.
        url = self.BaseUrl + QaAdpqShell.QaADPQShell.SearchArticles + QaAdpqShell.QaADPQShell.searchKeyWord
         
        # Assign the header parameters.
        headers = {
            'Content-Type' : 'application/json',
            'Cache-Control': 'no-cache'
        }
         
        # Assign the body parameters.
        body = {}
         
        # Make the call and return the save the results.
        response = requests.request('GET', url, json=body, 
                                    headers=headers, verify=False)
         
        # Ensure that the end point is live.
        self.assertEqual(response.status_code, 200, 
                         msg='test_GetSearchArticleStatus assert#1 failed.')
         
         
         
    # Get the status of the end point.
    def test_UserLoginStatus(self):
        pass
#         url = QaADPQShell.BaseURL + QaADPQShell.UsersLogin
         
         
         
        

        
#     @classmethod
#     def tearDownClass(cls):
#         pass
#         try:
#             pass
# #             cls.user.remove_user(cls.user.testEmail)
#         except:
#             print("Unexpected error during setUp:", sys.exc_info()[0])
#             #raise
#         #cls.user.remove_user(cls.user.testEmail)
    
    
    
def suite():
    suite = unittest.TestSuite()
    
    suite.addTest(SmokeTest('test_GetAgenciesStatus'))
    suite.addTest(SmokeTest('test_GetTagStatus'))
    suite.addTest(SmokeTest('test_GetArticleStatus'))
    suite.addTest(SmokeTest('test_GetSearchArticleStatus'))
#     suite.addTest(SmokeTest('test_UserLoginStatus'))
    
    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())