This Repository is to implement the new default roles for openstack Nova API policies. openstack keystone provides new defaults including 'reader' role along with 'admin' & 'member' etc and 'scope' (system, project) checks also. This repo starts implementing those new defaults roles in Nova Policies rules so that operator and users can use them without overriding it or override in a minimum amount. 

Implementation is on top of openstack/nova master branch on 28th dec 2019. I cloned the complete nova repo as initial commit to test the policis changes properly.

During the OpenStack Ussuri cycle, all changes in this repo will be moved to openstack/nova repo to be available from OpenStack. 
