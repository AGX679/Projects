//
//  ViewController.h
//  transformWithSliders
//
//  Created by Abraham Avnisan on 4/10/16.
//  Copyright © 2016 Abraham Avnisan. All rights reserved.
//

#import <UIKit/UIKit.h>
#import <AVFoundation/AVFoundation.h>
@interface ViewController : UIViewController

// IMAGE VIEW WE ARE TRANSFORMING
@property (weak, nonatomic) IBOutlet UIImageView *imageView;
@property (weak, nonatomic) IBOutlet UIImageView *garbageExample;
@property (weak, nonatomic) IBOutlet UIImageView *garbageExample2;
@property (weak, nonatomic) IBOutlet UIImageView *garbageExample3;
@property (weak, nonatomic) IBOutlet UIImageView *garbageExample4;
@property (weak, nonatomic) IBOutlet UIImageView *garbageExample5;
@property (weak, nonatomic) IBOutlet UIImageView *garbageExample6;
@property (weak, nonatomic) IBOutlet UIImageView *garbageExample7;
@property (weak, nonatomic) IBOutlet UIImageView *garbageExample8;
@property (weak, nonatomic) IBOutlet UIImageView *garbageExample9;
@property (weak, nonatomic) IBOutlet UIImageView *border;


@property (strong, nonatomic) NSMutableArray *garbageObjects;


// CURRENT AND PREVIOUS TRANSLATE, SCALE AND ROTATION

@property (nonatomic) float translateX;
@property (nonatomic) float translateXPrev;
@property (nonatomic) float translateY;
@property (nonatomic) float translateYPrev;

@property (nonatomic) float xStartLocation;
@property (nonatomic) float yStartLocation;

@property (nonatomic) float scale;
@property (nonatomic) float scalePrev;
@property (nonatomic) float scaleDiffPrev;

@property (nonatomic) float rotation;
@property (nonatomic) float rotationPrev;

// LABELS
@property (weak, nonatomic) IBOutlet UILabel *translateXLabel;
@property (weak, nonatomic) IBOutlet UILabel *translateYLabel;
@property (weak, nonatomic) IBOutlet UILabel *scaleLabel;
@property (weak, nonatomic) IBOutlet UILabel *rotationLabel;





@end
NSTimer *garbageMovementTimer; 
