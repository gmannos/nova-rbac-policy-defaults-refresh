# Copyright 2012 Nebula, Inc.
# Copyright 2013 IBM Corp.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from nova.tests.functional.api_sample_tests import test_servers


class AdminPasswordJsonTest(test_servers.ServersSampleBase):
    sample_dir = 'os-admin-password'

    def test_server_password(self):
        uuid = self._post_server()
        subs = {"password": "foo"}
        response = self._do_post('servers/%s/action' % uuid,
                                 'admin-password-change-password',
                                 subs)
        self.assertEqual(202, response.status_code)
        self.assertEqual("", response.text)
