#coding=utf-8
import unittest
import requests
import re
import urllib3
urllib3.disable_warnings()

class DeleteTest(unittest.TestCase):
    '''博客园发帖删帖'''
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDelete(self):
        '''博客园删帖'''
        s = requests.session()
        c = requests.cookies.RequestsCookieJar()
        c.set(".CNBlogsCookie",
              "C44EC789082EC5EFE1DD3D7F84A628B5E9E38D53C6BB2263E62800F204A93522602FD4B73B43FA4879089EE755260F3EC518C934D3D917C5CC317CB0477F4F641118A7CFBF16026D86A153D787CD2D35CF9BFE5C")
        c.set(".Cnblogs.AspNetCore.Cookies",
              "CfDJ8Gf3jjv4cttDnEy2UYRcGZ3hfvWx9TTTjZPzuCMpppmkGqQlLvC7zwTkCxwC1kLUv2jHq_yXudid4ApM7ZoIITbtboe3wcw6dBwESDcBdGmowgjZM6cGTbHZrs2YACoJionwbGW7iP_oxTVhv7GkT42HCsAFCIgQjvi7ojspV8vJlUMQ8fZRWXVT0mIhVNbRdBAGE9o8PQ60ZyQUHDTndayT17mgl0WW1EryaZhzNd5flB-ZjAsOhzZeIzfpGk6OeMX7qH3AgOboi9OFE64BsQ7iXkSy5YOnI3jjheXNshtl")
        s.cookies.update(c)
        # 发帖
        url = "https://i.cnblogs.com/EditPosts.aspx"
        par = {"opt": "1"}
        body = {
            "__VIEWSTATE": "",
            "__VIEWSTATEGENERATOR": "FE27D343",
            "Editor$Edit$txbTitle": "ddddddddddd",
            "Editor$Edit$EditorBody": "<p>aaaaaaaaaaaaa</p>",
            "Editor$Edit$Advanced$ckbPublished": "on",
            "Editor$Edit$Advanced$chkDisplayHomePage": "on",
            "Editor$Edit$Advanced$chkComments": "on",
            "Editor$Edit$Advanced$chkMainSyndication": "on",
            "Editor$Edit$Advanced$txbEntryName": "",
            "Editor$Edit$Advanced$txbExcerpt": "",
            "Editor$Edit$Advanced$txbTag": "",
            "Editor$Edit$Advanced$tbEnryPassword": "",
            "Editor$Edit$lkbDraft": "存为草稿",
        }
        r = s.post(url, params=par, data=body, verify=False)
        a = re.findall("postid=(.+?)&", r.url)[0]
        # 删帖
        url1 = "https://i.cnblogs.com/post/delete"
        body1 = {"postId": a}
        r1 = s.post(url1, json=body1)
        self.assertEqual(True, r1.json()["isSuccess"])

if __name__ == "__main__":
    unittest.main()
