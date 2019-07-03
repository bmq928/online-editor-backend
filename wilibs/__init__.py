# import os
# import requests
#
# class Wilibs:
#     def __init__(self):
#         self.HEADERS = {
#             'Content-Type': 'application/json',
#             'Reference-Policy': 'no-referrer',
#             'Authorization': ''
#         }
        # self.USER_RELATED_ROOT_URL = os.environ.get('USER_RELATED_ROOT_URL', 'http://localhost:3000')
        # self.PROJECT_RELATED_ROOT_URL = os.environ.get('PROJECT_RELATED_ROOT_URL', 'http://localhost:3000')

    # def login(self, username, password):
    #     url = self.USER_RELATED_ROOT_URL + '/login'
    #     print("login", url)
    #     payload = {
    #         "username": str(username),
    #         "password": str(password),
    #         "whoami": 'main-service'
    #     }
    #     headers = {
    #         'Content-Type': 'application/json',
    #         'Reference-Policy': 'no-referrer'
    #     }
    #     r = requests.post(url, json=payload, verify=False, headers=headers).json()['content']
    #     self.HEADERS['Authorization'] = r['token']
    #     return r
    #
    # def list_project(self):
    #     url = self.PROJECT_RELATED_ROOT_URL + '/project/list'
    #     payload = {}
    #     r = requests.post(url, json=payload, verify=False, headers=self.HEADERS).json()['content']
    #     return r
    #
    # def list_well_of_project(self, idProject, start, limit, forward, match):
    #     url = self.PROJECT_RELATED_ROOT_URL + '/project/well/list'
    #     payload = {
    #         "idProject": idProject,
    #         "start": start,
    #         "limit": limit,
    #         "forward": forward,
    #         "match": match
    #     }
    #     r = requests.post(url, json=payload, verify=False, headers=self.HEADERS).json()['content']
    #     return r
    #
    # def list_reference_curve(self):
    #     url = self.PROJECT_RELATED_ROOT_URL + '/project/well/reference-curve/list'
    #     payload = {}
    #     r = requests.post(url, json=payload, verify=False, headers=self.HEADERS).json()['content']
    #     return r
    #
    # def get_curve_info(self, idReferenceCurve):
    #     url = self.PROJECT_RELATED_ROOT_URL + '/project/well/reference-curve/info'
    #     payload = {
    #         "idReferenceCurve": idReferenceCurve
    #     }
    #     r = requests.post(url, json=payload, verify=False, headers=self.HEADERS).json()['content']
    #     return r
    
   

   