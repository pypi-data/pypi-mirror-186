'''
@Author  :   顾一龙 
@Time    :   2023/01/16 19:10:33
@Version :   1.0
@Contact :   世界那么大，你不想走走吗
'''
# Hard to write shit mountain.......


from .base import base

# 用户组


class cjdgUserGroup(base):
    def __init__(self, token, app_secret=None):
        super().__init__(token, app_secret)

    # 用户组查询
    def list(self, data):
        api_name = "usergroup/getlist"
        return self.request(api_name=api_name, data=data)

    # 用户组名字和编码查询
    def list_code(self, data):
        api_name = "usergroup/getlist"
        return self.request(api_name=api_name, data=data)

    # 删除用户组
    def delete(self, data):
        api_name = "usergroup/delete"
        return self.request(api_name=api_name, data=data)

    # 用户详情
    def listGroupMem(self, data):
        api_name = "usergroup/listGroupMem"
        return self.request(api_name=api_name, data=data)

    # 用户组新增

    def eidt(self, data):
        api_name = "usergroup/eidt"
        return self.request(api_name=api_name, data=data)

    # 用户组刷新
    def groupmem(self, data):
        api_name = "usergroup/groupmem"
        return self.request(api_name=api_name, data=data)
