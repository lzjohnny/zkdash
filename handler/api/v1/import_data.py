#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
摘    要: import_data.py
创 建 者: liuzijian
创建日期: 2018-01-14
"""
from handler.bases import ApiBaseHandler
from handler.bases import ArgsMap
from service.account.authenticated import api_authenticated
from service.zookeeper import znode as ZnodeService
from service.zookeeper import zookeeper as ZookeeperService
from lib import route


@route(r'/api/v1/import')
class ApiImportDataHandler(ApiBaseHandler):
    """
    管理员导入配置数据接口
    """
    args_list = [
        ArgsMap('cluster_name', required=True),
        ArgsMap('parent_path', required=True),
        ArgsMap('node_name', required=True),

        ArgsMap('znode_type', default=0),
        ArgsMap('data', default=''),
        ArgsMap('business', default=''),
    ]

    @api_authenticated
    def response(self):
        if self.node_name and not ZnodeService.is_node_name_ok(self.node_name):
            return self.api_response(code=101, msg="节点名不允许包含特殊字符'/'！")

        zk_path = ""
        if not self.path:
            # 新增节点需要进行存在检验
            zk_path = "/{0}".format(self.node_name) if self.parent_path == "/" else "{0}/{1}".format(self.parent_path,
                                                                                                     self.node_name)
            if ZookeeperService.exists(self.cluster_name, zk_path):
                return self.api_response(code=102, msg="节点已经存在！")
        else:
            zk_path = self.path

        # znode_type, 0代表普通节点, 1代表文件节点
        zk_data = ""
        if self.znode_type == "1":
            if 'uploadfile' not in self.request.files:
                return self.ajax_popup(code=300, msg="请选择上传文件！")
            upload_file = self.request.files['uploadfile'][0]
            zk_data = upload_file['body']
        else:
            zk_data = self.data

        # 更新在zookeeper和mysql上存储的配置信息, 同时进行快照备份
        ZnodeService.set_znode(cluster_name=self.cluster_name,
                               path=zk_path,
                               data=zk_data,
                               znode_type=self.znode_type,
                               business=self.business)

        return self.api_response()
