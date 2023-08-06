import copy
import math
import os
from pathlib import Path
import shutil
import time
import unittest

import cv2
import geomapi.tools.progresstools as pt
import geomapi.utils.geometryutils as gt
import ifcopenshell
import numpy as np
import open3d as o3d
import pye57
import pytest
from ifcopenshell.util.selector import Selector
from rdflib import RDF, RDFS, Graph, Literal, URIRef


################################## SETUP/TEARDOWN MODULE ######################

# def setUpModule():
#     #execute once before the module 
#     print('-----------------Setup Module----------------------')

# def tearDownModule():
#     #execute once after the module 
#     print('-----------------TearDown Module----------------------')

class TestProgressutils(unittest.TestCase):

 ################################## SETUP/TEARDOWN CLASS ######################
  
    @classmethod
    def setUpClass(cls):
        #execute once before all tests
        print('-----------------Setup Class----------------------')
        st = time.time()
        cls.path= Path.cwd() / "test" / "testfiles" 
        
        #POINTCLOUD3
        cls.pcdPath1=cls.path / 'PCD' / "academiestraat week 22 a 20.pcd"     
        cls.pcd= o3d.io.read_point_cloud(str(cls.pcdPath1)) 

        #IFC2
        cls.ifcPath2=cls.path / 'IFC' / "Academiestraat_parking.ifc" 
        ifc2 = ifcopenshell.open(str(cls.ifcPath2))   
        ifcSlab=ifc2.by_guid('2qZtnImXH6Tgdb58DjNlmF')
        ifcWall=ifc2.by_guid('06v1k9ENv8DhGMCvKUuLQV')
        ifcBeam=ifc2.by_guid('05Is7PfoXBjhBcbRTnzewz' )
        ifcColumn=ifc2.by_guid('23JN72MijBOfF91SkLzf3a')
        # ifcWindow=ifc.by_guid(cls.slabGlobalid) 
        # ifcDoor=ifc.by_guid(cls.slabGlobalid)

        cls.slabMesh=gt.ifc_to_mesh(ifcSlab)
        cls.wallMesh=gt.ifc_to_mesh(ifcWall)
        cls.beamMesh=gt.ifc_to_mesh(ifcBeam)
        cls.columnMesh=gt.ifc_to_mesh(ifcColumn)
        
        #RESOURCES
        cls.resourcePath=os.path.join(cls.path,"resources")
        if not os.path.exists(cls.resourcePath):
            os.mkdir(cls.resourcePath)
   
        et = time.time()
        print("startup time: "+str(et - st))
        print('{:50s} {:5s} '.format('tests','time'))
        print('------------------------------------------------------')


    @classmethod
    def tearDownClass(cls):
        #execute once after all tests
        print('-----------------TearDown Class----------------------')
        if os.path.exists(cls.resourcePath):
            shutil.rmtree(cls.resourcePath)      

################################## SETUP/TEARDOWN ######################

    def setUp(self):
        #execute before every test
        self.startTime = time.time()   

    def tearDown(self):
        #execute after every test
        t = time.time() - self.startTime
        print('{:50s} {:5s} '.format(self._testMethodName,str(t)))

################################## FIXTURES ######################
    # # @pytest.fixture(scope='module')
    # # @pytest.fixture
    # def test_data(*args):
    #     here = os.path.split(__file__)[0]
    #     return os.path.join(here, "testfiles", *args)

    # @pytest.fixture
    # def e57Path1():
    #     return test_data("pointcloud.e57")

    # @pytest.fixture
    # def ifcData():
    #     ifcPath=os.path.join(os.getcwd(),"testfiles", "ifcfile.ifc")
    #     classes= '.IfcBeam | .IfcColumn | .IfcWall | .IfcSlab'
    #     ifc = ifcopenshell.open(ifcPath)   
    #     selector = Selector()
    #     dataList=[]
    #     for ifcElement in selector.parse(ifc, classes): 
    #         dataList.append(ifcElement)
    #     return dataList

################################## TEST FUNCTIONS ######################


    def test_create_visible_point_cloud_from_meshes(self):
        referenceMesh1= copy.deepcopy(self.slabMesh)
        referenceMesh1.translate([1,0,0])
        referenceMesh2= copy.deepcopy(self.slabMesh)
        referenceMesh2.translate([0,1,0])
        
        # 1 geometry
        identityPointClouds1, percentages1=pt.create_visible_point_cloud_from_meshes(geometries=self.slabMesh,
                                                references=referenceMesh1)
        self.assertEqual(len(identityPointClouds1),1)
        self.assertGreater(len(identityPointClouds1[0].points),10)
        self.assertEqual(len(percentages1),1)        
        self.assertLess(percentages1[0],0.2)

        # multiple geometries 
        list=[self.slabMesh,self.wallMesh]
        references=[referenceMesh1,referenceMesh2]
        identityPointClouds2, percentages2=pt.create_visible_point_cloud_from_meshes(geometries=list,
                                                references=references)
        self.assertEqual(len(identityPointClouds2),2)
        self.assertLess(len(identityPointClouds2[0].points),len(identityPointClouds1[0].points))
        self.assertEqual(len(percentages2),2)        
        self.assertLess(percentages2[0],percentages1[0])
    
    def test_determine_percentage_of_coverage(self):
        reference=self.pcd
        sources=[self.slabMesh,self.wallMesh,self.columnMesh,self.beamMesh]
        percentages=pt.determine_percentage_of_coverage(sources=sources,reference=reference)
        self.assertEqual(len(percentages), len(sources))
        self.assertLess(percentages[0],0.005)
        self.assertLess(percentages[1],0.001)
        self.assertLess(percentages[2],0.5)
        self.assertLess(percentages[3],0.001)
