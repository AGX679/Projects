//
//  ViewController.m
//  planeDetector
//
//  Created by Alan Xu on 2/22/19.
//  Copyright © 2019 Alan Xu. All rights reserved.
//

#import "ViewController.h"

@interface ViewController () <ARSCNViewDelegate>

@property (nonatomic, strong) IBOutlet ARSCNView *sceneView;
@property (strong, nonatomic) NSArray *objectsArray;
@property (nonatomic) NSUInteger objectCount;


@end


@implementation ViewController
#pragma mark - setup
- (void)setup
{
    self.objectCount = 0;
    [self setupScene];
    [self setupSession];
    [self setupObjectsArray];
}
- (void)setupScene
{
    // Set the view's delegate
    self.sceneView.delegate = self;
    
    // Show statistics such as fps and timing information
    self.sceneView.showsStatistics = YES;
    
    // Config debug options
    self.sceneView.debugOptions = ARSCNDebugOptionShowWorldOrigin;
    self.sceneView.debugOptions = ARSCNDebugOptionShowFeaturePoints;
    
    // Create a new scene
    SCNScene *scene = [SCNScene scene];
    
    // Set the scene to the view
    self.sceneView.scene = scene;
}
- (void)setupSession
{
    // Create a session configuration
    ARWorldTrackingConfiguration *configuration = [ARWorldTrackingConfiguration new];
    
    // Configure for plane detection
    configuration.planeDetection = ARPlaneDetectionVertical;
    
    // Run the view's session
    [self.sceneView.session runWithConfiguration:configuration];
}
- (void)setupObjectsArray
{
    SCNPlane *pic1 = [SCNPlane planeWithWidth:1.0 height:0.60];
    pic1.firstMaterial.diffuse.contents = [UIImage imageNamed:@"autism1"];
    pic1.firstMaterial.doubleSided = YES;
    SCNNode *pic1Node = [SCNNode nodeWithGeometry:pic1];

    SCNPlane *pic2 = [SCNPlane planeWithWidth:1.0 height:0.60];
    pic2.firstMaterial.diffuse.contents = [UIImage imageNamed:@"autism2"];
    pic2.firstMaterial.doubleSided = YES;
    SCNNode *pic2Node = [SCNNode nodeWithGeometry:pic2];

    SCNPlane *pic3 = [SCNPlane planeWithWidth:1.0 height:0.60];
    pic3.firstMaterial.diffuse.contents = [UIImage imageNamed:@"autism3"];
    pic3.firstMaterial.doubleSided = YES;
    SCNNode *pic3Node = [SCNNode nodeWithGeometry:pic3];

    SCNPlane *pic4 = [SCNPlane planeWithWidth: 1.0 height: 0.60];
    pic4.firstMaterial.diffuse.contents = [UIImage imageNamed:@"autism4"];
    pic4.firstMaterial.doubleSided = YES;
    SCNNode *pic4Node = [SCNNode nodeWithGeometry:pic4];
    
    SCNPlane *pic5 = [SCNPlane planeWithWidth: 1.0 height: 0.60];
    pic4.firstMaterial.diffuse.contents = [UIImage imageNamed:@"autism5"];
    pic4.firstMaterial.doubleSided = YES;
    SCNNode *pic5Node = [SCNNode nodeWithGeometry:pic5];
    
    self.objectsArray = [NSArray arrayWithObjects:pic1Node, pic2Node, pic3Node, pic4Node, pic5Node, nil];

}

//- (void)setupObjectsArray
//{
//    SCNPlane *pic1 = [SCNPlane planeWithWidth:0.6 height:1.0];
//    pic1.firstMaterial.diffuse.contents = [UIImage imageNamed:@"poc"];
//    pic1.firstMaterial.doubleSided = YES;
//    SCNNode *pic1Node = [SCNNode nodeWithGeometry:pic1];
//
//    SCNPlane *pic2 = [SCNPlane planeWithWidth:0.6 height:1.0];
//    pic2.firstMaterial.diffuse.contents = [UIImage imageNamed:@"poc"];
//    pic2.firstMaterial.doubleSided = YES;
//    SCNNode *pic2Node = [SCNNode nodeWithGeometry:pic2];
//
//
//    SCNPlane *pic3 = [SCNPlane planeWithWidth:0.6 height:1.0];
//    pic3.firstMaterial.diffuse.contents = [UIImage imageNamed:@"poc"];
//    pic3.firstMaterial.doubleSided = YES;
//    SCNNode *pic3Node = [SCNNode nodeWithGeometry:pic3];
//
//    self.objectsArray = [NSArray arrayWithObjects:pic1Node, pic2Node, pic3Node, nil];
//
//}

#pragma mark - actions
- (IBAction)userDidTap:(UITapGestureRecognizer *)sender
{
    CGPoint tapLocation = [sender locationInView:self.sceneView];
    NSArray *hitTestResults = [self.sceneView hitTest:tapLocation types:ARHitTestResultTypeExistingPlaneUsingExtent];
    
    ARHitTestResult *hitTestResult;
    
    if (hitTestResults.count > 0) {
        
        hitTestResult = hitTestResults[0];
        
        // grab an object from our array
        SCNNode *node = self.objectsArray[self.objectCount];
        
        node.simdTransform = hitTestResult.worldTransform;
        
        node.eulerAngles = SCNVector3Make(M_PI, M_PI , M_PI);
        
        [self.sceneView.scene.rootNode addChildNode:node];
        
        self.objectCount++;
        if (self.objectCount >= self.objectsArray.count) {
            self.objectCount = 0;
        }
    }
}
#pragma mark - inherited methods
- (void)viewDidLoad {
    [super viewDidLoad];
    [self setup];
}
#pragma mark - ARSCNViewDelegate

//// Override to create and configure nodes for anchors added to the view's session.
//- (SCNNode *)renderer:(id<SCNSceneRenderer>)renderer nodeForAnchor:(ARAnchor *)anchor {
//
//    if ([anchor isKindOfClass:[ARPlaneAnchor class]]) {
//
//        NSLog(@"PLACING IMAGE");
//
//        ARPlaneAnchor *planeAnchor = (ARPlaneAnchor *)anchor;
//
//        float xExtent = planeAnchor.extent.x;
//        float yExtent = planeAnchor.extent.y;
//
//        NSLog(@"xExtent = %f", xExtent);
//
////        SCNPlane *pic1 = [SCNPlane planeWithWidth:xExtent height:yExtent];
//        SCNPlane *pic1 = [SCNPlane planeWithWidth:1 height:0.5];
//        pic1.firstMaterial.diffuse.contents = [UIImage imageNamed:@"autism1"];
//        pic1.firstMaterial.doubleSided = YES;
//        SCNNode *pic1Node = [SCNNode nodeWithGeometry:pic1];
//
//        float x = planeAnchor.center.x;
//        float y = planeAnchor.center.y;
//        float z = planeAnchor.center.z;
//
//        pic1Node.position = SCNVector3Make(x, y, z);
//        pic1Node.eulerAngles = SCNVector3Make(M_PI, 0.0, 0.0);
//
//
//        return pic1Node;
//
//    } else {
//        return nil;
//    }
//
//}




@end
